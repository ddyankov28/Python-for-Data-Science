import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Prints the current shape of the 2Darray, slices it
    and prints the new shape of it
    -------
    @param
        - family: list
        - start: int
        - end: int
    -------
    @rtype
        - list
    -------
    @return
        - Sliced list
    '''
    assert isinstance(family, list), "First argument to slice_me not a list"
    assert all(len(sublist) == len(family[0]) for sublist in family), "Sublists not same size"
    fam = np.array(family)
    print(f"My shape is : {fam.shape}")
    print(f"My new shape is: {fam[start:end].shape}")
    return family[start:end]

# resources
# - https://numpy.org/devdocs/user/absolute_beginners.html
# - https://www.w3schools.com/python/numpy/numpy_array_shape.asp
# - https://www.w3schools.com/python/numpy/numpy_array_slicing.asp