def NULL_not_found(object: any) -> int:
    if object == None:
        print(f"Nothing: None {type(object)}")
    elif type(object) == float and object != object:
        print(f"Cheese: nan {type(object)}")
    elif type(object) == int and object == 0:
        print(f"Zero: 0 {type(object)}")
    elif (type(object) == str and object == ''):
        print(f"Empty: {type(object)}")
    elif (type(object) == bool):
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0


# any comparison involving NaN should return false
# including comparisons with itself
# This is because NaN represents the result of operations that are 
# mathematically undefined or in situations where a computation results 
# in a quantity that cannot be accurately represented as a number


# resource:
#       - https://www.w3schools.com/python/ref_keyword_none.asp
#       - https://www.geeksforgeeks.org/python-check-if-nonetype-or-empty/
#       - https://www.geeksforgeeks.org/check-if-the-value-is-infinity-or-nan-in-python/
#       - https://www.w3schools.com/python/ref_func_isinstance.asp