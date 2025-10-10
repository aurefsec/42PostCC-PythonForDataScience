import numpy as np
import matplotlib.pyplot as mppyplot  # To show image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""

    invert_image = 255 - array

    print("The shape of invert image is :", invert_image.shape)

    mppyplot.imshow(invert_image)
    mppyplot.title("Figure VIII.2: Invert")
    mppyplot.show()

    return invert_image


def ft_red(array: np.ndarray) -> np.ndarray:
    """Change the color of the image received in red."""

    red_image = array[:, :, 0:3].copy()
    red_image[:, :, 1] = 0
    red_image[:, :, 2] = 0

    print("The shape of red image is :", red_image.shape)

    mppyplot.imshow(red_image)
    mppyplot.title("Figure VIII.3: Red")
    mppyplot.show()

    return red_image


def ft_green(array: np.ndarray) -> np.ndarray:
    """Change the color of the image received in green."""

    green_image = array[:, :, 0:3].copy()
    green_image[:, :, 0] = 0
    green_image[:, :, 2] = 0

    print("The shape of green image is :", green_image.shape)

    mppyplot.imshow(green_image)
    mppyplot.title("Figure VIII.4: Green")
    mppyplot.show()

    return green_image


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Change the color of the image received in blue."""

    blue_image = array[:, :, 0:3].copy()
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0

    print("The shape of blue image is :", blue_image.shape)

    mppyplot.imshow(blue_image)
    mppyplot.title("Figure VIII.5: Blue")
    mppyplot.show()

    return blue_image


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Change the color of the image received in grey."""

    grey_values = np.array([0.2989, 0.5870, 0.1140])

    # Apply grey_values for any dimensions and return 2D array
    grey_2d = np.dot(array[:, :, 0:3], grey_values)

    # Create final image in 3D
    grey_image = array[:, :, 0:3].copy()
    for i in range(3):
        grey_image[:, :, i] = grey_2d

    grey_image = grey_image.astype(np.uint8)

    print("The shape of grey image is :", grey_image.shape)

    mppyplot.imshow(grey_image)
    mppyplot.title("Figure VIII.6: Grey")
    mppyplot.show()

    return grey_image
