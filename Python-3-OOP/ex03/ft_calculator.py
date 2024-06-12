class calculator:
    '''Docstring calculator Class'''
    def __init__(self, numbers):
        '''Docstring Constructor calculator Class'''
        self.numbers = numbers

    def __add__(self, object) -> None:
        '''Adds the object to every number and returns a new list'''
        self.numbers = [number + object for number in self.numbers]
        print(self.numbers)
        return self.numbers

    def __mul__(self, object) -> None:
        '''Multiplies the object with every number and returns a new list'''
        self.numbers = [number * object for number in self.numbers]
        print(self.numbers)
        return [self.numbers]

    def __sub__(self, object) -> None:
        '''Subtracts the object from every number and returns a new list'''
        self.numbers = [number - object for number in self.numbers]
        print(self.numbers)
        return self.numbers

    def __truediv__(self, object) -> None:
        '''Divides every number with the object and returns a new list'''
        try:
            if object == 0:
                raise Exception("Division by 0")
            self.numbers = [number / object for number in self.numbers]
            print(self.numbers)
        except Exception as e:
            print("Error: ", e)
        return self.numbers
