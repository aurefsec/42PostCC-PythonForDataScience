import sys


def mean(data: list) -> None:
    """Calcul and print the mean of the list"""

    nb = 0
    for value in data:
        nb += value
    mean = nb / len(data)
    print("mean :", mean)


def median(data: list) -> None:
    """Calcul and print the median of the list"""

    if len(data) % 2 != 0:
        median = data[len(data) // 2]  # "//" avoids conversion to float
        print("median :", median)
    else:
        median = (data[len(data) // 2 - 1] + data[len(data) // 2]) // 2
        print("median :", median)


def quartile(data: list) -> None:
    """Calcul and print the quartile of the list : 25% and 75%"""

    list_result = [0] * 2
    quartile = int(len(data) * 0.25)
    list_result[0] = float(data[quartile])
    quartile = int(len(data) * 0.75)
    list_result[1] = float(data[quartile])
    print("quartile :", list_result)


def var_std(data: list, varstd: str) -> None:
    """Calcul and print the stantard deviation of the list"""

    # Calcul the mean of the list
    nb = 0
    for value in data:
        nb += value
    mean = nb / len(data)

    # For each number, calcul (number - mean)^2
    list_result = [(value - mean) ** 2 for value in data]  # '**' for power

    # Calcul de the mean of the new list
    nb = 0
    for value in list_result:
        nb += value
    mean = nb / len(data)

    if varstd == "var":
        print("var :", mean)
    elif varstd == "std":
        root = mean ** 0.5  # Calcul the root of mean
        print("std :", root)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Applies the corresponding function to a tuple of numbers"""

    # Error handling
    for element in args:
        if type(element) is not int and type(element) is not float:
            print("ERROR", file=sys.stderr)
            return

    # Sort the tuple into a list
    if args:
        data = sorted(args)

    # Call functions
    for key, value in kwargs.items():  # .item() to access value key values
        if not args:
            print("ERROR", file=sys.stderr)
        elif value == "mean":
            mean(data)
        elif value == "median":
            median(data)
        elif value == "quartile":
            quartile(data)
        elif value == "std" or value == "var":
            var_std(data, value)
