import sys

NESTED_MORSE = {" ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. ",
                "0": "----- "}


def checkInput(S):
    '''
    Checks the input string if contains only space and alphanumeric chars
    '''
    for char in S:
        if not char.isalnum() and not char == ' ':
            return False
        else:
            continue
    return True


def main():
    '''
    Encodes string into Morse Code
    '''
    if len(sys.argv[1:]) != 1:
        print("AssertionError: the arguments are bad")
    else:
        morseString = ""
        if checkInput(sys.argv[1]):
            upperString = sys.argv[1].upper()
            for char in upperString:
                morseString += NESTED_MORSE[char]
            print(morseString)
        else:
            print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
