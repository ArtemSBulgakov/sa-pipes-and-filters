"""
This module contains the filters that can be applied to the input frame.
"""

import cv2
import numpy as np


def black_and_white_filter(input_frame: np.ndarray) -> np.ndarray:
    """Filter to convert the input frame to black and white"""
    return cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)


def mirror_filter(input_frame: np.ndarray) -> np.ndarray:
    """Filter to mirror the input frame"""
    return cv2.flip(input_frame, 1)


def resize_filter(input_frame: np.ndarray) -> np.ndarray:
    """Filter to resize the input frame"""
    width, height = 600, 400
    return cv2.resize(input_frame, (width, height))


def rotate_filter(input_frame: np.ndarray) -> np.ndarray:
    """Filter to rotate the input frame"""
    angle = 45
    rows, cols = input_frame.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(input_frame, rotation_matrix, (cols, rows))
