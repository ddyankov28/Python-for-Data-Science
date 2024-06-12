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
    def __init__(self, first_name, is_alive=True):
        '''Docstring Constructor Lannister(Character) Class'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        '''Class Method to create Lannister Characters in a chain'''
        new_lannister = cls(first_name, is_alive)
        return new_lannister

# resources
# - https://www.digitalocean.com/community/tutorials/python-str-repr-functions
