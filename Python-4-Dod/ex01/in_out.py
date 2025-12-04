def square(x: int | float) -> int | float:
    """Return a square of int or float"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return a power of int or float"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a function that applies 'function' to stored value (closure)"""

    count = 0

    def inner() -> float:
        """Applies 'function' to the stores value, updates and returns it"""

        nonlocal count  # 'nonlocal' to use count
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner
