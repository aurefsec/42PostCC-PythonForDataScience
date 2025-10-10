import matplotlib.pyplot as mppyplot  # To show image
import numpy as np
from load_image import ft_load


def main() -> int:
    """Load an image, zoom, rotate, print informations and shows it"""

    image = ft_load("animal.jpeg")

    # Check the pixel number of image
    height, width = image.shape[0:2]
    if height < 564 or width < 712:
        raise ValueError("Not enough pixels in the image")

    # Slice to zoom and keep only one channel
    image_zoom = image[164:564, 312:712, 0:1]

    # Print image informations before rotating
    print("The shape of image is :", image_zoom.shape)
    print(image_zoom)

    # Rotate image.
    rows = len(image_zoom)
    cols = len(image_zoom[0])
    rotate = np.array([[0 for _ in range(rows)] for _ in range(cols)])
    for i in range(rows):
        for j in range(cols):
            rotate[j][i] = image_zoom[i][j].item()

    # Print image informations after rotating
    print("New shape after transpose :", rotate.shape)
    print(rotate)

    mppyplot.imshow(rotate, cmap="gray")  # Prepare before showing
    mppyplot.show()

    return 1


if __name__ == "__main__":
    main()
