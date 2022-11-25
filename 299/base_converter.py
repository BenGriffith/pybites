from string import ascii_uppercase

def convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """
    if base < 2 or base > 36:
        raise ValueError

    lookup = [str(num) for num in range(10)] + list(ascii_uppercase)
    remainder = []

    while number >= base:
        remainder.insert(0, number % base)
        number = number // base
    remainder.insert(0, number % base)
    return "".join([lookup[i] for i in remainder])