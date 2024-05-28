from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
# from pimp_image import ft_green
# from pimp_image import ft_blue
# from pimp_image import ft_grey


def main():
    try:
        array = ft_load("landscape.jpg")

        ft_invert(array)
        ft_red(array)
        # ft_green(array)
        # ft_blue(array)
        # ft_grey(array)

        # print(ft_invert.__doc__)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
