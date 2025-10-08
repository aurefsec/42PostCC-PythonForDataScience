import matplotlib.pyplot as mppyplot  # To show image
from load_image import load_image


def main() -> int:
    """Load an image, zoom, print informations and shows it"""

    image = load_image("animal.jpeg")

    # Print informations before zoom
    print("The shape of image is :", image.shape)
    print(image)

    # Slice to zoom and keep only one channel
    image_zoom = image[164:564, 312:712, 0:1]

    # Print informations after zoom
    print("New shap after slicing :", image_zoom.shape)
    print(image_zoom)

    mppyplot.imshow(image_zoom, cmap="gray")  # Prepare before showing
    mppyplot.show()

    return 1


if __name__ == "__main__":
    main()
