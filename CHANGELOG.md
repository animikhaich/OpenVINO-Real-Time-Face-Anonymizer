# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Version 1.0.2 - 2021-01-16

### Modified

-   Bugfix - Fixed Image Dimension Checks in `image_utils.py`

## Version 1.0.1 - 2020-09-27

### Added

-   Signature to `detect.py`
-   Intel Licensing information for `intel_inference.py`
-   Additional Comment on `main.py`

### Modified

-   Bugfix - Fixed Detector to accept gray scale images in `detect.py`
-   Changed Default Detector Confidence to 0.75 in `config.json` to avoid false positives

## Version 1.0.0 - 2020-09-22

### Added

-   First Release
-   Face Detection using Intel OpenVINO [face-detection-0104](https://docs.openvinotoolkit.org/latest/omz_models_intel_face_detection_0104_description_face_detection_0104.html) model
-   Face Blurring using OpenCV
-   Performance Optimizations
-   Automatic Weights Download
-   Logging
