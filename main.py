from misc import CustomVideoWriter, display_frame, blur_frame, calc_fps
from face_detection import OpenVINOFaceDetector
from misc import logging, load_config
from imutils.video import VideoStream
import cv2, time, os

# Configs and Initializations
config = load_config("config.json")
video_source = config.get("input", 0)
face_detector = OpenVINOFaceDetector(config=config)

# Determine Video Input Type
if "rtsp" in video_source.lower() or "http" in video_source.lower():
    live_stream = True
else:
    live_stream = False

# Initialize Video Input
if live_stream:
    cap = VideoStream(video_source).start()
    temp_cap = cv2.VideoCapture(video_source)  # Just to get the video meta
    width = int(temp_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(temp_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(temp_cap.get(cv2.CAP_PROP_FPS))
    temp_cap.release()
else:
    cap = cv2.VideoCapture(video_source)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

# Initialize Video Writer
if config.get("write_video", False):
    video_writer = CustomVideoWriter(
        output_path=config.get("output", "output.mp4"),
        width=width,
        height=height,
        fps=fps,
    )

while True:
    start_time = time.time()

    # Read the frame
    if live_stream:
        frame = cap.read()
    else:
        _, frame = cap.read()

    # If frame is not received
    if frame is None and live_stream:
        logging.warning("Broken Stream, attempting to reconnect...")
        time.sleep(30)
        cap = VideoStream(video_source).start()
        continue
    elif frame is None and not live_stream:
        break

    try:
        # Run Face Detection
        boxes = face_detector.detect(frame)
    except Exception as e:
        logging.error(f"Failed to detect: {e}")

    # Blur Faces
    for x1, y1, x2, y2 in boxes:
        face = frame[y1:y2, x1:x2]
        blurred_face = blur_frame(face, kernel_size=config.get("blur_strength", 99))
        frame[y1:y2, x1:x2] = blurred_face

    # Calculate FPS
    frame, fps = calc_fps(start_time, frame)

    # Write Frame
    if config.get("write_video", False):
        video_writer.write_frame(frame)

    # Display frame
    if config.get("display_live", False):
        terimate = display_frame(frame)
        if terimate:
            break

# Release the Video Writer
if config.get("write_video", False):
    video_writer.close()
cv2.destroyAllWindows()