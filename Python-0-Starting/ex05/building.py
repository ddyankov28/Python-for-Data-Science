import sys


def sumChars(sumString):
    '''
    Counting Characters
    '''
    totalChars = len(sumString)
    upperLetters = sum(char.isupper() for char in sumString)
    lowerLetters = sum(char.islower() for char in sumString)
    spaces = sum(char.isspace() for char in sumString)
    punctMarks = sum(not char.isalnum() and not char.isspace() for char in sumString)
    digits = sum(char.isdigit() for char in sumString)
    print(f"The text contains {totalChars} characters:")
    print(f"{upperLetters} upper letters")
    print(f"{lowerLetters} lower letters")
    print(f"{punctMarks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    '''
    The main function
    '''
    try:
        if len(sys.argv[1:]) > 1:
            print("AssertionError")
        elif len(sys.argv[1:]) == 0:
            sumString = input("What is the text to count?\n")
            sumChars(sumString)
        else:
            sumString = sys.argv[1]
            sumChars(sumString)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user!")
    except Exception:
        print("Error!")
    


if __name__ == "__main__":
    main()

# resource:
# - https://realpython.com/if-name-main-python/
# - https://www.freecodecamp.org/news/if-name-main-python-example/git
# - https://www.youtube.com/watch?v=0YUdYk5E-w4&ab_channel=Programiz
# - https://www.youtube.com/watch?v=NIWwJbo-9_8&ab_channel=CoreySchafer
# - https://www.geeksforgeeks.org/taking-input-in-python/
