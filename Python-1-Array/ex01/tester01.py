from array2D import slice_me


def main():
    '''
    Creates 2D Array and uses the slice_me function on it
    '''
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]

        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
