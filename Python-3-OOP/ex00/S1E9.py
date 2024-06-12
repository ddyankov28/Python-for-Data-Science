from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract Class Character'''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Doc for the Constructor of Abstract Class'''
        self.first_name = first_name
        self.is_alive = is_alive if is_alive is not True else is_alive

    def die(self):
        '''Doc for the Die method'''
        self.is_alive = False


class Stark(Character):
    '''Doc for the Stark Class'''
    def __init__(self, first_name, is_alive=True):
        '''Doc for the Constructor of Stark Class'''
        super().__init__(first_name, is_alive)

# NOTES:
# - The __init__() function is called automatically every time
#              the class is being used to create a new object.
# - The self parameter is a reference to the current instance
#              of the class, and is used to access variables that
#              belong to the class.

# resources
# - https://www.w3schools.com/python/python_classes.asp
# - https://docs.python.org/3/library/abc.html
# - https://www.geeksforgeeks.org/abstract-classes-in-python/
