def task_88v(_number: int)\
        -> int:
    """
    Task 88 в)
    :param: int _number - natural number
    :return: Integer with swapped first and last digits of a number
    :raises ValueError: if number is negative
    :raises ValueError: if parameter's datatype doesn't match
    """
    if _number < 0:
        raise ValueError("Can't convert negative number")
    _number = str(_number)
    return int(_number) if len(_number) == 1 else int(_number[-1] + _number[1:-1] + _number[0])


def task_88g(_number: int)\
        -> int:
    """
    Task 88 г)
    :param: int _number - natural number
    :return: Integer with two 1s concatenated with this number
    :raises ValueError: if number is negative
    :raises ValueError: if parameter's datatype doesn't match
    """
    if _number < 0:
        raise ValueError("Can't convert negative number")

    _number = str(_number)
    return int("1" + _number + "1")


def task_332(_number: int)\
        -> tuple:
    """
    Find numbers which match expression:
    n = x**2 + y**2 + z**2 + t**2
    :param: int _number - natural number
    :return: First 4 numbers which match the expression
    :raises ValueError: if number is negative
    :raises ValueError: if parameter's datatype doesn't match
    """
    if _number < 0:
        raise ValueError("Can't convert negative number")

    _sqr = int(_number ** 0.5) + 1

    for x in range(_sqr):
        for y in range(_sqr):
            for z in range(_sqr):
                for t in range(_sqr):
                    if x*x + y*y + z*z + t*t == _number:
                        return x, y, z, t
