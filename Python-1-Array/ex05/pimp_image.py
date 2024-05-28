from PIL import Image, ImageOps
import numpy as np


def colorFilter(blackc: str, array):
    print(array)
    img = Image.fromarray(array)
    img = ImageOps.colorize(img.convert('L'), black= blackc, white="white")
    img.show()

def ft_invert(array) -> np.array:
    print(array)
    img = Image.fromarray(array)
    imgInverted = ImageOps.invert(img)
    imgInverted.show()
    arrayA = np.array(imgInverted)
    return arrayA


def ft_red(array) -> np.array:
    


# def ft_green(array) -> array:



# def ft_blue(array) -> array:



# def ft_grey(array) -> array: