from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    '''
    Loads image, prints the shape and the pixels content
    as an NumPy array
    -------
    @param
        - path: str
    -------
    @rtype
        - NumPy array
    -------
    @return
        - Image Pixels represented in RGB format
    '''
    img = Image.open(path)
    # print(f"The image format is: {img.format}")
    # print(f"The image mode is: {img.mode}")
    assert img.mode == "RGB", "Image mode should be RGB"
    imgArray = np.array(img)
    print(f"The shape of image is: {imgArray.shape}")
    return imgArray


# resources
# - https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
# - https://www.geeksforgeeks.org/python-pil-image-convert-method/
# - https://pillow.readthedocs.io/en/stable/handbook/concepts.html
# - https://www.geeksforgeeks.org/how-to-convert-images-to-numpy-array/
