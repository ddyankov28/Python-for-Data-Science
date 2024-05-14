import sys
from ft_filter import ft_filter


def checkSpecialChars(S):
    '''
    Checks if there are special characters in a string
    '''
    for char in S:
        if not char.isalnum() and not char.isspace():
            return False
        else:
            continue
    return True


def outputWords(S, N):
    '''
    Outputs a list of words from S that have a length greater than N
    '''
    splitedString = S.split()
    output = ft_filter(lambda word: len(word) > N, splitedString)
    print(output)


def main():
    '''
    The main function
    '''
    if len(sys.argv[1:]) != 2:
        print("Assertion Error: the arguments are bad")
    elif not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
        print("Assertion Error: the arguments are bad")

    else:
        if checkSpecialChars(sys.argv[1]):
            outputWords(sys.argv[1], int(sys.argv[2]))
        else:
            print("Special characters are not allowed")


if __name__ == "__main__":
    main()

# resource:
# - https://www.w3schools.com/python/python_lists_comprehension.asp
# - https://www.w3schools.com/python/python_lambda.asp
# - https://www.w3schools.com/python/ref_string_split.asp
