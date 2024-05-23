def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''
    Calculates Body Mass Index values with the
    BMI formula:\n
    weight / (height * height)
    ------
    @param:
        - height: int / float list
        - weight: int / float list
    -------
    @rtype
        - int / float list
    -------
    @returns
        - list with BMI values
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
    Checks if BMI value is biger than a given limit
    @params
        - bmi: int/float list
        - limit: int
    -------
    @rtype
        - bool list
    -------
    @returns
        - list with True / False
    '''
    assert all(isinstance(bmiValue, (int, float))
               for bmiValue in bmi), "BMI value not int or float"
    assert isinstance(limit, int), "Limit value not int"
    boolList = [bmiValue > limit for bmiValue in bmi]
    return boolList


# resources
# BMI = Body mass index
# https://numpy.org/doc/stable/user/absolute_beginners.html
# BMI = WEIGHT / (HEIGHT * HEIGHT)
# https://www.w3schools.com/python/ref_func_all.asp
