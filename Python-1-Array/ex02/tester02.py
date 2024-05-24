from load_image import ft_load


def main():
    try:
        print(ft_load("landscape.jpg"))
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
