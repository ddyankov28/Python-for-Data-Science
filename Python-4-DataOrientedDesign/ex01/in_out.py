def square(x: int | float) -> int | float:
    '''
    Returns the square of the argument x
    '''
    return x * x


def pow(x: int | float) -> int | float:
    '''
    Returns the exponentiation of the argument x by himself
    '''
    return x**x


def outer(x: int | float, function) -> object:
    '''
    Returns an object that when called returns the result of
    the arguments calculation
    '''
    count = 0

    def inner() -> float:
        '''
        The closure (inner function)
        '''
        nonlocal x
        x = function(x)
        return x
    count += 1
    return inner


# NOTES
# - Python closure is a nested function that allows us to access
#       variables of the outer function even after the outer
#       function is closed.
# resources
# - https://www.geeksforgeeks.org/python-inner-functions/
# - https://www.programiz.com/python-programming/closure
