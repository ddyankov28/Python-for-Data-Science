from S1E9 import Character


class Baratheon(Character):
    '''Docstring Baratheon(Character) Class'''
    def __init__(self, first_name, is_alive=True):
        '''Docstring Constructor Baratheon(Character) Class'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


class Lannister(Character):
    '''Docstring Lannister(Character) Class'''

# resources
# - https://www.digitalocean.com/community/tutorials/python-str-repr-functions
