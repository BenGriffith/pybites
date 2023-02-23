def original_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die."""
    expected_value = 0
    for i in range(1, n + 1):
        expected_value += (1/n) * i
    return round(expected_value, 1)


def new_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die when the player simultaneously rolls
    two dice and chooses the larger value.
    """
    expected_value = 0
    numerator = 1
    for i in range(1, n + 1):
        expected_value += (numerator/(n * n)) * i
        numerator += 2
    return round(expected_value, 3)