from load_image import ft_load
from PIL import Image
import numpy as np

def main():
    imgArr = (ft_load("animal.jpeg"))
    zoomedImg = Image.fromarray(imgArr)
    grey = zoomedImg.convert('L')
    croppedGrey = grey.crop((440,100,840,500))
    croppedGrey.show()
    croppedGreyArr = np.array(croppedGrey)
    print(f"New shape after slicing: {croppedGreyArr.shape}")
    print(croppedGreyArr)


if __name__ == "__main__":
    main()


# resources
# - 