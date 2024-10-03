"""
Main module to capture frames from a video file and process them using a set of filters
"""

import sys

import cv2
import numpy as np

from src.filters import resize_filter, black_and_white_filter, mirror_filter, rotate_filter
from src.video_capturer import capture_frames


def main():
    """Main function to capture frames from a video file and process them using a set of filters"""
    # Define the filters to apply
    filters = [
        resize_filter,
        black_and_white_filter,
        mirror_filter,
        rotate_filter
    ]

    # Capture frames from the video file and process them using the filters
    video_file = sys.argv[1] if len(sys.argv) > 1 else "data/video.mp4"
    for frame in capture_frames(video_file):
        process_frame(frame, filters)


def process_frame(source_frame: np.ndarray, filters: list) -> np.ndarray:
    """Process the input frame using a set of filters"""
    # Apply the filters using pipes pattern
    frame = source_frame
    cv2.imshow("source", frame)
    for f in filters:
        frame = f(frame)
        cv2.imshow(f.__name__, frame)
    return frame



if __name__ == "__main__":
    main()
