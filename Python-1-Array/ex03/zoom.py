from load_image import ft_load
from PIL import Image
import numpy as np


def main():
    '''
    Loads an image, prints some info about it and displays it
    after "zooming"
        - the size in pixle on both X and Y axis
        - the number of channel
        - pixel content of the image
        - the scale on the x and y axis on the image
    '''
    try:
        imgArr = ft_load("animal.jpeg")
        print(imgArr)
        zoomedImg = Image.fromarray(imgArr)
        grey = zoomedImg.convert('L')
        croppedGrey = grey.crop((450, 100, 850, 500))
        croppedGrey.show()
        croppedGreyArr = np.array(croppedGrey)
        reshapedCroppedGreyArr = croppedGreyArr[:, :, np.newaxis]
        print(f"New shape after slicing: {reshapedCroppedGreyArr.shape}"
              f" or {croppedGreyArr.shape}")
        print(reshapedCroppedGreyArr)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()


# resources
# - https://pillow.readthedocs.io/en/stable/reference/Image.html
# - https://www.geeksforgeeks.org/python-pil-image-crop-method/
