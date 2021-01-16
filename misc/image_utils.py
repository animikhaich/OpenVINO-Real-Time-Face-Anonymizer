__author__ = "Animikh Aich"
__copyright__ = "Copyright 2020, Animikh Aich"
__credits__ = ["Animikh Aich"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Animikh Aich"
__email__ = "animikhaich@gmail.com"

import cv2, imutils, time, os
import numpy as np


def display_frame(frame, window_name="Frame", width=None, height=None):
    if width is not None or height is not None:
        frame_show = imutils.resize(frame, width=width, height=height)
    else:
        frame_show = frame.copy()

    cv2.imshow(window_name, frame_show)
    key = cv2.waitKey(1)
    if key == ord(" "):
        key = cv2.waitKey(0)
    elif key == ord("q"):
        return True
    return False


def blur_frame(frame, kernel_size=5, blur_algo=None):
    # Automatically handle if a wrong (even) kernel size is given
    if kernel_size % 2 == 0:
        kernel_size += 1

    # Choose Blur Algorithm as per the argument
    if blur_algo is not None and "gaussian" in blur_algo.lower():
        frame_blur = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)
    elif blur_algo is not None and "median" in blur_algo.lower():
        frame_blur = cv2.medianBlur(frame, kernel_size)
    else:
        frame_blur = cv2.blur(frame, (kernel_size, kernel_size))

    return frame_blur


def calc_fps(start_time, frame=None, print_on_console=False):
    fps = 1 / (time.time() - start_time)
    fps_str = f"FPS: {fps:.2f}"
    if print_on_console:
        print(fps_str)
    if (
        frame is not None
        and isinstance(frame, np.ndarray)
        and min(frame.shape[:-1]) > 50
    ):
        cv2.putText(
            frame, fps_str, (20, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1
        )
        return frame, fps
    return fps


class CustomVideoWriter:
    def __init__(self, output_path, width, height, fps):
        output_path = self.__pre_checks(output_path)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    def __pre_checks(self, output_path):
        folder, filename = os.path.split(output_path)

        if len(folder) > 0 and not os.path.isdir(folder):
            os.makedirs(folder)

        if len(filename) < 1:
            output_path = os.path.join(folder, "output.mp4")

        if not output_path.endswith(".mp4"):
            output_path += ".mp4"

        return output_path

    def write_frame(self, frame):
        self.out.write(frame)

    def close(self):
        self.out.release()
