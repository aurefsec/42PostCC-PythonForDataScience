import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return a randomly generated ID"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class using '@dataclass' that allows certain values to be init"""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """This function init the values that can't be init by user"""
        self.login = self.name[0] + self.surname
        self.id = generate_id()
