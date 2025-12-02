class calculator:
    """A calculator thats can add, multiply, substract or divide"""

    def __init__(self, vector):
        """Calculator init"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds "object" to all elements of "vector and prints"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplies "object" to all elements of "vector and prints"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """substracts "object" to all elements of "vector and prints"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divides "object" to all elements of "vector and prints"""
        if object == 0:
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
