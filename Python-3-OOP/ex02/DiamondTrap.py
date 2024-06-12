from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Docstring King(Baratheon, Lannister) Class'''
    def __init__(self, first_name, is_alive=True):
        '''Docstring Constructor King(Baratheon, Lannister) Class'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_color):
        '''Sets the new color of the King's eyes'''
        self.eyes = new_color

    def set_hairs(self, new_color):
        '''Sets the new color of the King's hairs'''
        self.hairs = new_color

    def get_eyes(self):
        '''Returns the eye color'''
        return self.eyes

    def get_hairs(self):
        '''Returns the hairs color'''
        return self.hairs

# resources
# - https://en.wikipedia.org/wiki/C3_linearization
