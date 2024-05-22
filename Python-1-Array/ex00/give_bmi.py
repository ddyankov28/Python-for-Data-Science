def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''
    Takes 2 lists of integers or floats in input and
    returns a list of BMI values
    '''
    assert all(isinstance(heightValue, (int, float))
               for heightValue in height), "Height value not int or float"
    assert all(isinstance(weightValue, (int, float))
               for weightValue in weight), "Weight value not int or float"
    assert len(height) == len(weight), "Height and weight lists not same size"
    bmiList = []
    for i in range(len(height)):
        bmiList.append(weight[i] / (height[i] * height[i]))
    return bmiList


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    Takes a list of integers or floats and an int representing
    limit as parameters. Returns list of booleans(True if above limit)
    '''
    assert all(isinstance(bmiValue, (int, float))
               for bmiValue in bmi), "BMI value not int or float"
    assert isinstance(limit, int), "Limit value not int"
    boolList = [bmiValue > limit for bmiValue in bmi]
    return boolList


def main():
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


# resources
# BMI = Body mass index
# https://numpy.org/doc/stable/user/absolute_beginners.html
# BMI = WEIGHT / (HEIGHT * HEIGHT)
# https://www.w3schools.com/python/ref_func_all.asp
