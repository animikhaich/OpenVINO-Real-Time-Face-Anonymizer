from .intel_inference import Network
from misc import logging, download_file
import numpy as np
import cv2, os


class OpenVINOFaceDetector:
    def __init__(self, config):
        self.config = config

        weights_path, message = self.download_weights()

        self.infer_network = Network()
        self.n, self.c, self.h, self.w = self.infer_network.load_model(
            model=weights_path,
            device=config.get("processing_device", "CPU"),
            input_size=1,
            output_size=1,
            num_requests=1,
        )[1]

    def download_weights(self):
        folder = self.config.get("weights_folder", "weights")

        # Hardcoded URLs
        bin_url = "https://download.01.org/opencv/2020/openvinotoolkit/2020.3/open_model_zoo/models_bin/1/face-detection-0104/FP16/face-detection-0104.bin"
        xml_url = "https://download.01.org/opencv/2020/openvinotoolkit/2020.3/open_model_zoo/models_bin/1/face-detection-0104/FP16/face-detection-0104.xml"

        # Get Filenames
        bin_filename = os.path.basename(bin_url)
        xml_filename = os.path.basename(xml_url)

        # Generate Path
        bin_path = os.path.join(folder, bin_filename)
        xml_path = os.path.join(folder, xml_filename)

        # Check if weights already exist
        bin_exists = os.path.exists(bin_path)
        xml_exists = os.path.exists(xml_path)

        if not bin_exists or not xml_exists:
            # If weights does not exist
            try:
                bin_success, bin_message, bin_path = download_file(
                    source_url=bin_url, filename=bin_filename, folder=folder
                )
                xml_success, xml_message, xml_path = download_file(
                    source_url=xml_url, filename=xml_filename, folder=folder
                )
            except Exception as e:
                logging.error(f"Failed to Download Weights. Error: {e}")
                logging.info(f"The Program will exit.")
                exit(1)
        else:
            # If weights exists
            return (
                xml_path,
                f"Found existing weights. Skipping download.",
            )

        # If downloading fails, exit the program
        if not bin_success or not xml_success:
            logging.error(
                f"Failed to Download Weights. Messages: bin_message: {bin_message} | xml_message: {xml_message}"
            )
            logging.info(f"The Program will exit.")
            exit(1)

        return (
            xml_path,
            f"Weights Downloaded Successfully. Messages: bin_message: {bin_message} | xml_message: {xml_message}",
        )

    def detect(self, frame, channel_mode="bgr"):
        # Make sure the channel is in BGR foramt
        if channel_mode == "rgb":
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        elif channel_mode == "gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # local declarations
        frame_h, frame_w, _ = frame.shape
        request_id = 0
        boxes = []

        # Preprocessing Frame
        input_frame = cv2.resize(frame, (self.w, self.h))
        input_frame = input_frame.transpose((2, 0, 1))
        input_frame = np.expand_dims(input_frame, axis=0)

        # Run inference and wait for response
        self.infer_network.exec_net(request_id=request_id, frame=input_frame)
        self.infer_network.wait(request_id=request_id)

        # Get detection outputs and remove extra dimensions
        detections = self.infer_network.get_output(request_id=request_id)
        detections = np.squeeze(detections)

        # Iterate over each detection and append coords to boxes with some sanity checks
        for image_id, label, conf, x1, y1, x2, y2 in detections:
            if conf < self.config.get("detection_confidence", 0.75):
                continue

            x1 = max(int(x1 * frame_w), 0)
            y1 = max(int(y1 * frame_h), 0)
            x2 = min(int(x2 * frame_w), frame_w)
            y2 = min(int(y2 * frame_h), frame_h)

            boxes.append([x1, y1, x2, y2])

        return boxes