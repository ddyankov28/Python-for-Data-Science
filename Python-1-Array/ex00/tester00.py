from give_bmi import give_bmi, apply_limit


def main():
    '''
    Creates a list of BMI Values, prints it and its type
    and prints a list if values are above a given limit
    '''
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
