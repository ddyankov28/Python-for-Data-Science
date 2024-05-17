def ft_filter(function, iterable):
    '''
    Return an iterator yielding those items of iterable for
    which function(item) is true. If function is None,
    return the items that are true.
    '''
    if function is None:
        return [item for item in iterable]
    return [item for item in iterable if function(item)]


def myFunc(x):
    '''
    Checks if a number is bigger than 18 or not
    '''
    if x < 18:
        return False
    else:
        return True


def main():
    '''
    The main function
    '''
    try:
        ages = [5, 12, 17, 18, 24, 32]

        adults = filter(myFunc, ages)
        print("⬇️ Original filter⬇️")
        for x in adults:
            print(x)

        adults1 = ft_filter(myFunc, ages)
        print("⬇️ My filter⬇️")
        for y in adults1:
            print(y)
        print(filter.__doc__)
    except Exception as exc:
        print(f"Error: Something went wrong: {exc}")


if __name__ == "__main__":
    main()

# resource:
# - https://www.youtube.com/watch?v=f-iYWG8ouvI&ab_channel=b001
# - https://www.w3schools.com/python/ref_func_filter.asp
# - https://www.w3schools.com/python/python_lists_comprehension.asp
# - https://www.w3schools.com/python/ref_keyword_yield.asp
