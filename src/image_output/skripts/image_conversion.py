from cv2 import cvtColor, COLOR_BGR2RGB
import numpy as np


def data_to_image(data, width, height):
    """
    Converts the data field of a ROS Image message to an OpenCV image

    Args:
        data: Contains the bytes of the image in utf-8 encoding
        width: width of the image
        height: height of the image
    """
    img = np.fromstring(data, np.uint8).reshape(height, width, 3)
    return cvtColor(img, COLOR_BGR2RGB)
