"""This module with help functions."""


def is_natural_number(number: int) -> bool:
    """
    Returns true if number is natural, else - False
    """
    
    return isinstance(number, int) and number > 0