from load_image import ft_load
from PIL import Image
import numpy as np


def main():
    '''
    Loads image, cuts a square part from it and rotates
    it 90°. Displays it and prints the new shape and data
    of the image after the transpose
    '''
    try:
        imgArr = ft_load("animal.jpeg")
        img = Image.fromarray(imgArr)
        grey = img.convert('L')
        croppedGrey = grey.crop((450, 100, 850, 500))
        croppedGreyArr = np.array(croppedGrey)
        reshapedCroppedGreyArr = croppedGreyArr[:, :, np.newaxis]
        print(f"The shape of image is: {reshapedCroppedGreyArr.shape}"
              f" or {croppedGreyArr.shape}")
        print(reshapedCroppedGreyArr)
        rotated = np.array([[croppedGreyArr[y][x]
                            for y in range(len(croppedGreyArr))]
                            for x in range(len(croppedGreyArr[0]))])
        print(f"New shape after Transponse: {rotated.shape}")
        rotatedimg = Image.fromarray(rotated)
        rotatedimg.show()
        print(rotated)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()


# resources
# - https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
# - https://en.wikipedia.org/wiki/Transpose
