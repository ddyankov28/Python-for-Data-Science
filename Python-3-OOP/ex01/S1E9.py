from abc import ABC, abstractmethod


class Character(ABC):
    '''Character Abstract Class'''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Docstring Constructor Abstract Class'''
        self.first_name = first_name
        self.is_alive = is_alive if is_alive is not True else is_alive

    def die(self):
        '''Docstring Die method'''
        self.is_alive = False

    def __str__(self):
        '''User friendly description of object'''
        obj_tuple = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {obj_tuple}"

    def __repr__(self):
        '''Developer friendly description of object'''
        return self.__str__()


class Stark(Character):
    '''Docstring Stark(Character) Class'''
    def __init__(self, first_name, is_alive=True):
        '''Docstring Constructor Stark(Character) Class'''
        super().__init__(first_name, is_alive)

# NOTES:
# - The __init__() function is called automatically every time
#              the class is being used to create a new object.
# - The self parameter is a reference to the current instance
#              of the class, and is used to access variables that
#              belong to the class.
# - The __str__() method returns a human-readable, or informal,
#              string representation of an object.
# - The __repr__() method returns a more information-rich, or
#               official, string representation of an object.
#               If possible, the string returned should be a valid
#               Python expression that can be used to recreate the object.
# - In general, the __str__() string is intended for users and
#               the __repr__() string is intended for developers.

# resources
# - https://www.w3schools.com/python/python_classes.asp
# - https://docs.python.org/3/library/abc.html
# - https://www.geeksforgeeks.org/abstract-classes-in-python/
# - https://www.digitalocean.com/community/tutorials/python-str-repr-functions
