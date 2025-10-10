import numpy as np
import matplotlib.image as mpimg  # To load image
import os


def ft_load(path: str) -> np.ndarray:
    """Check input file, loads and returns it"""

    if not os.path.isfile(path):
        raise FileNotFoundError(path, "file not found")
    if not os.path.splitext(path)[1].lower() in [".jpeg", ".jpg"]:
        raise TypeError("Image type must be 'jpeg' or 'jpg'")

    try:
        image = mpimg.imread(path)  # Load image
    except Exception as e:
        raise ValueError("Error loading image :", path, ":", e)

    if not isinstance(image, np.ndarray):
        raise TypeError("Loaded file is not a numpy array")
    if image.ndim < 2:
        raise ValueError("Loaded file is not an image")

    return image
