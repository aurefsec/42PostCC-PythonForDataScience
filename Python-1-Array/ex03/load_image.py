import numpy as np
import matplotlib.image as mpimg  # To load image
import os


def load_image(image_name: str) -> np.ndarray:
    """Check input file, loads and returns it"""

    if not os.path.isfile(image_name):
        raise FileNotFoundError(image_name, "file not found")

    try:
        image = mpimg.imread(image_name)  # Load image
    except Exception as e:
        raise ValueError("Error loading image :", image_name, ":", e)

    if not isinstance(image, np.ndarray):
        raise TypeError("Loaded file is not a numpy array")
    if image.ndim < 2:
        raise ValueError("Loaded file is not an image")

    height, width = image.shape[0:2]
    if height < 564 or width < 712:
        raise ValueError("Not enough pixels in the image")

    return image
