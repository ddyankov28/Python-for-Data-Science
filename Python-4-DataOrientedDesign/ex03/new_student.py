import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''
    Generates a string with 15 char len that is random generated
    from lowercase letters
    '''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''
    Dataclass Student that contains of items corresponding to a
    profile of a student
    '''
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False, repr=True)
    id: str = field(init=False, repr=True)

    def __post_init__(self):
        '''
        The post initialization method which assigns values to
        the items which are not initialized during the __init__ method
        '''
        self.login = self.name[0] + self.surname
        self.id = generate_id()

# NOTES
# - RANDOM can be used to perform random actions such as generating
#       random numbers, printing random value for a list or string, etc.
# - DATACLASS holds only data values and store information
# - FIELD function used to customize one attribute of a data class
#       individually, which allows to define new attributes that will
#       depend on another attribute
# - __POST_INIT__ can initialize class items after the original init
#       in the case where the field(init= is set to False)
# resources
# - https://www.geeksforgeeks.org/python-random-module/
# - https://www.geeksforgeeks.org/data-classes-in-python-an-introduction/
# - https://www.dataquest.io/blog/how-to-use-python-data-classes/
