import imageio.v2 as iio

img = iio.imread("python.jpg")
iio.imwrite("python.jpg", img)