from PIL import Image, ImageOps
import numpy as np


def colorFilter(color: str, array) -> np.array:
    '''
    Converts to grayscale image and puts the color argument
    as the color for white
    '''
    print(array)
    img = Image.fromarray(array)
    img = ImageOps.colorize(img.convert('L'), black="black", white=color)
    img.show()
    arrayA = np.array(img)
    return arrayA


def ft_invert(array) -> np.array:
    '''
    Inverts the color of the image received
    '''
    print(array)
    img = Image.fromarray(array)
    imgInverted = ImageOps.invert(img)
    imgInverted.show()
    arrayA = np.array(imgInverted)
    return arrayA


def ft_red(array) -> np.array:
    '''
    Converts to grayscale image and puts red color
    '''
    return colorFilter("red", array)


def ft_green(array) -> np.array:
    '''
    Converts to grayscale image and puts green color
    '''
    return colorFilter("green", array)


def ft_blue(array) -> np.array:
    '''
    Converts to grayscale image and puts blue color
    '''
    return colorFilter("blue", array)


def ft_grey(array) -> np.array:
    '''
    Converts to grayscale image and puts grey color
    '''
    return colorFilter("grey", array)


# resources
# - https://www.geeksforgeeks.org/python-pil-imageops-colorize-method/
# - https://www.geeksforgeeks.org/python-color-inversion-using-pillow/
