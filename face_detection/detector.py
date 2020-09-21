from face_detection import Network
from misc import logging
import numpy as np
import cv2, os



class OpenVINOFaceDetector:
    def __init__(self, config):
        self.config = config

        weights_path = 'weights/face-detection-0104.xml'

        self.infer_network = Network()
        self.n, self.c, self.h, self.w = self.infer_network.load_model(
            model=weights_path,
            device=config.get("processing_device", "CPU"),
            input_size=1,
            output_size=1,
            num_requests=1
        )[1]

    def detect(self, frame, channel_mode="bgr"):
        if channel_mode == "rgb":
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        elif channel_mode == "gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        frame_h, frame_w, _ = frame.shape
        request_id = 0
        boxes = []

        input_frame = cv2.resize(frame, (self.w, self.h))
        input_frame = input_frame.transpose((2, 0, 1))
        input_frame = np.expand_dims(input_frame, axis=0)

        self.infer_network.exec_net(request_id=request_id)
        self.infer_network.wait(request_id=request_id)

        detections = self.infer_network.get_output(request_id=request_id)
        detections = np.squeeze(detections)

        for image_id, label, conf, x1, y1, x2, y2 in detections:
            if conf < self.config.get("detection_confidence", 0.75):
                continue
                
            x1 = max(int(x1 * frame_w), 0)
            y1 = max(int(y1 * frame_h), 0)
            x2 = min(int(x2 * frame_w), frame_w)
            y2 = min(int(y2 * frame_h), frame_h)

            boxes.append([x1, y1, x2, y2])
        
        return boxes