from S1E9 import Character


class Baratheon(Character):
    """Representing a Baratheon family"""

    # Methods
    def __init__(self, first_name, is_alive=True):
        """Baratheon init"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "Black"

    # Decorator
    @classmethod  # For cls
    def create_baratheon(cls, first_name, is_alive=True):
        """Create a Baratheon instance"""
        return cls(first_name, is_alive)  # Create an instance of this class


class Lannister(Character):
    """Representing a Lannister family"""

    # Methods
    def __init__(self, first_name, is_alive=True):
        """Lannister init"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "Blue"
        self.hairs = "Blonde"

    # Decorator
    @classmethod  # For cls
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister instance"""
        return cls(first_name, is_alive)  # Create an instance of this class
