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

# resources
# - https://www.w3schools.com/python/python_classes.asp
# - https://docs.python.org/3/library/abc.html
# - https://www.geeksforgeeks.org/abstract-classes-in-python/
