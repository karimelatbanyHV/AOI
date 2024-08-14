# ROI Selection Tool

This project contains a function that extracts Region of Interest (ROI) coordinates from images or videos. It is designed to help in various computer vision tasks by providing accurate ROI extraction.

## Features
- Extracts ROI coordinates from images
- Extracts ROI coordinates from videos
- Supports multiple input formats
- Easy integration with other computer vision tasks

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/roi-selection-tool.git
    cd roi-selection-tool
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install opencv-python numpy
    ```

## Usage
Run the tool by passing the path to your video file as an argument to the `vid_roi()` function in the script.

```python
import cv2
from roi_selection import vid_roi
```
vid_roi('path_to_your_video.mp4')

## How to Use
Select Points: Click on the video to select points for the ROI. You need to select four points to form a rectangular ROI.
Press 's': After selecting the ROI, press 's' to save it. You will be prompted to enter a name for the ROI.
Press 'c': Reset the current selection and start over if needed.
Press 'q': Quit the application.
All the saved ROIs will be stored in rois.txt with their names and coordinates.

