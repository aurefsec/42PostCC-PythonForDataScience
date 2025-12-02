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


class Stark(Character):
    """A character that inherits from Character abstract class """

    # Methods
    def __init__(self, first_name, is_alive=True):
        """Stark init"""
        self.first_name = first_name
        self.is_alive = is_alive
