from time import sleep


def ft_tqdm(lst: range) -> None:  # type: ignore
    '''
    tqdm = Instantly make your loops show a smart progress meter
    just wrap any iterable with ft_tqdm(lst: range), and you're done!
    '''
    totalIterations = len(lst)
    for i, elem in enumerate(lst, 1):
        progress = int(i / totalIterations * 61)
        bar = '#' * progress + ' ' * (61 - progress)
#        print(f"Element value {elem}")
#        print(f"Counter value {i}")
        percent = (elem / totalIterations) * 100
        print(f"{percent:>3.0f}%|{bar}| {i}/{totalIterations}  ", end='\r')
        yield elem


def main():
    '''
    The main function
    '''
    try:
        for elem in ft_tqdm(range(3333)):
            sleep(0.0005)
        print()
    except KeyboardInterrupt as ki:
        print(f"\nKeyboardInterrupt: {ki}")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()

# resources:
# - https://www.geeksforgeeks.org/enumerate-in-python/
# - https://www.geeksforgeeks.org/python-yield-keyword/
# - https://tqdm.github.io/
