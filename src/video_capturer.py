"""
This module contains the function to capture frames from the input video file.
"""

from typing import Generator

import cv2
import numpy as np


def capture_frames(video_file: str) -> Generator[np.ndarray, None, None]:
    """Capture frames from the input"""
    # Open the video file
    cap = cv2.VideoCapture(video_file)

    # Check if the video file is opened
    if not cap.isOpened():
        print('Error: Could not open video file')
        return

    # Read the video file frame by frame
    while True:
        ret, frame = cap.read()

        # Check if the video file is read successfully
        if not ret:
            break

        # Return the frame
        yield frame

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file
    cap.release()
