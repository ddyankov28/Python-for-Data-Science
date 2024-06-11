from abc import ABC, abstractmethod

class Character(ABC):
    '''
    Abstract Class Character
    '''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''
        Object initialization with name 
        and var for life status
        '''
        self.first_name = first_name
        self.is_alive = is_alive if is_alive is not True else is_alive
        

class Stark(Character):
    '''
    asd
    '''
    def __init__(self, first_name, is_alive=True):
        '''
        abc
        '''
        super().__init__(first_name, is_alive)

# NOTES:
# - The __init__() function is called automatically every time
#              the class is being used to create a new object.

# resources
# - https://docs.python.org/3/library/abc.html
# - https://www.geeksforgeeks.org/abstract-classes-in-python/