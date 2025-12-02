from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing Joffrey Baratheon, a child from Baratheon and Lannister"""

    # Properties (Python style)
    @property
    def p_eyes(self):
        """King eyes property getter"""
        return self.eyes

    @p_eyes.setter
    def p_eyes(self, value):
        """King eyes property setter"""
        self.eyes = value

    @property
    def p_hairs(self):
        """King hairs property getter."""
        return self.hairs

    @p_hairs.setter
    def p_hairs(self, value):
        """King hairs property setter"""
        self.hairs = value

    # Setters/Getters (C++ style)
    def get_eyes(self):
        """King eyes getter"""
        return self.eyes

    def set_eyes(self, value):
        """King eyes setter"""
        self.eyes = value

    def get_hairs(self):
        """King hairs getter"""
        return self.hairs

    def set_hairs(self, value):
        """King hairs setter"""
        self.hairs = value
