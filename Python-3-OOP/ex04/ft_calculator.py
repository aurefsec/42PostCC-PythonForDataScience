class calculator:

    @staticmethod  # To use methods without create an instance of calculator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product between two lists of floats"""

        res = sum(x * y for x, y in zip(V1, V2))  # Zip : two list on same size
        print("Dot product is :", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two lists of floats"""

        V3 = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is :", V3)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substract two lists of floats"""

        V3 = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is :", V3)
