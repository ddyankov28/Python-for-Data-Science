class calculator:
    '''Docstring calculator Class'''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Returns the dot product of the vectors'''
        result = 0
        i = 0
        for number in V1:
            result += number * V2[i]
            i += 1
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        add_vector = []
        i = 0
        for number in V1:
            result = number + V2[i]
            i += 1
            add_vector.append(float(f"{result:.1f}"))
        print(f"Add vector is: {add_vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sous_vector = []
        i = 0
        for number in V1:
            result = number - V2[i]
            i += 1
            sous_vector.append(float(f"{result:.1f}"))
        print(f"Sous Vector is: {sous_vector}")


# NOTES:
# - The dot product (also known as the scalar product) is an operation
#   that takes two vectors and returns a scalar (a single number).

# resources
# -https://www.kdnuggets.com/8-built-in-python-decorators-to-write-elegant-code
