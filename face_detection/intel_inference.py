"""
Copyright (c) 2018 Intel Corporation.
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import sys
from misc import logging as log

try:
    # Preferred import path for OpenVINO 2025.0+
    from openvino import Core
except ImportError:
    # Fallback import path for OpenVINO 2022.1 - 2024.x
    from openvino.runtime import Core


class Network:
    """
    Load and configure inference plugins for the specified target devices
    and performs synchronous and asynchronous modes for the specified infer requests.
    """

    def __init__(self):
        self.model = None
        self.core = None
        self.input_blob = None
        self.out_blob = None
        self.compiled_model = None
        self.infer_request = None

    def load_model(
        self,
        model,
        device,
        input_size,
        output_size,
        num_requests,
        cpu_extension=None,
        plugin=None,
    ):
        """
         Loads a network and an image to the Inference Engine plugin.
        :param model: .xml file of pre trained model
        :param cpu_extension: extension for the CPU device
        :param device: Target device
        :param input_size: Number of input layers
        :param output_size: Number of output layers
        :param num_requests: Index of Infer request value. Limited to device capabilities.
        :param plugin: Plugin for specified device
        :return:  Shape of input layer
        """

        model_xml = model
        model_bin = os.path.splitext(model_xml)[0] + ".bin"
        
        # Initialize Core
        if not plugin:
            log.info("Initializing plugin for {} device...".format(device))
            self.core = Core()
        else:
            self.core = plugin

        if cpu_extension and "CPU" in device:
            self.core.add_extension(cpu_extension, "CPU")

        # Read IR
        log.info("Reading IR...")
        self.model = self.core.read_model(model=model_xml)
        log.info("Loading IR to the plugin...")

        # Compile model for the specified device
        self.compiled_model = self.core.compile_model(self.model, device)
        
        # Get input and output names (store as names for compatibility)
        self.input_blob = list(self.model.inputs)[0].get_any_name()
        self.out_blob = list(self.model.outputs)[0].get_any_name()

        return self.core, self.get_input_shape()

    def get_input_shape(self):
        """
        Gives the shape of the input layer of the network.
        :return: None
        """
        return self.model.input(self.input_blob).shape

    def performance_counter(self, request_id):
        """
        Queries performance measures per layer to get feedback of what is the
        most time consuming layer.
        :param request_id: Index of Infer request value. Limited to device capabilities
        :return: Performance of the layer
        """
        if self.infer_request:
            perf_count = self.infer_request.get_perf_counts()
            return perf_count
        return None

    def exec_net(self, request_id, frame):
        """
        Starts asynchronous inference for specified request.
        :param request_id: Index of Infer request value. Limited to device capabilities.
        :param frame: Input image
        :return: Instance of Executable Network class
        """
        self.infer_request = self.compiled_model.create_infer_request()
        self.infer_request.start_async(inputs={self.input_blob: frame})
        return self.compiled_model

    def wait(self, request_id):
        """
        Waits for the result to become available.
        :param request_id: Index of Infer request value. Limited to device capabilities.
        :return: Timeout value
        """
        if self.infer_request:
            self.infer_request.wait()
        return 0

    def get_output(self, request_id, output=None):
        """
        Gives a list of results for the output layer of the network.
        :param request_id: Index of Infer request value. Limited to device capabilities.
        :param output: Name of the output layer
        :return: Results for the specified request
        """
        if self.infer_request:
            if output:
                res = self.infer_request.get_tensor(output).data
            else:
                res = self.infer_request.get_tensor(self.out_blob).data
            return res
        return None

    def clean(self):
        """
        Deletes all the instances
        :return: None
        """
        del self.compiled_model
        del self.core
        del self.model