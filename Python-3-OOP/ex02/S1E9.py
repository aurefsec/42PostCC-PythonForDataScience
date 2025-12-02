from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for all characters"""

    # Methods
    @abstractmethod
    def __init__(self, first_name, is_alive=True):  # is_alive is non mandatory
        """Character init"""
        pass  # Attributes will be init from child

    def die(self):
        """Kill the character if he's alive"""
        if self.is_alive is True:
            self.is_alive = False

    # Special Methods
    def __str__(self):
        """Return informations in string type"""
        return f"Vector : ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Return informations in string type"""
        return f"Vector : ({self.family_name}, {self.eyes}, {self.hairs})"


class Stark(Character):
    """Representing a Baratheon family"""

    # Methods
    def __init__(self, first_name, is_alive=True):
        """Stark init"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Stark"
        self.eyes = "Gray"
        self.hairs = "Brown"

    # Decorator
    @classmethod  # For cls
    def create_stark(cls, first_name, is_alive=True):
        """Create a Stark instance"""
        return cls(first_name, is_alive)  # Create an instance of this class
