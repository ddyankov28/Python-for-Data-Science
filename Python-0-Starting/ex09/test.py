from ft_package import count_in_list


def main():
    try:
        print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
        print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
