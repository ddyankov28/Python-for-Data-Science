def all_thing_is_obj(object: any) -> int:
    if (type(object) == list):
        print(f"List : {type(object)}")
    elif (type(object) == tuple):
        print(f"Tuple : {tuple}")
    elif (type(object) == set):
        print(f"Set : {set}")
    elif (type(object) == dict):
        print(f"Dict : {dict}")
    elif (type(object) == str):
        print(f"{object} is in the kitchen : {str}")
    else:
        print("Type not found")
    return 42
        

# resource:
#       - https://www.w3schools.com/python/python_functions.asp
#       - https://www.w3schools.com/python/python_datatypes.asp