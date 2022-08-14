import pytest

from decorators import retry, MaxRetriesException, MAX_RETRIES


@retry
def sum_numbers(numbers):
    """
    Sum numbers, if not all ints raise a ValueError
    (bit silly but justs to test the decorator)
    """
    if not all(type(i) == int for i in numbers):
        raise ValueError('not all ints')
    return sum(numbers)


def test_bad_data_max_retries_and_exception(capfd):
    with pytest.raises(MaxRetriesException):
        sum_numbers(['a', 'b'])
    output = capfd.readouterr()[0]
    assert output.count('not all ints') == MAX_RETRIES


def test_good_data_no_retry_and_no_exception(capfd):
    sum_numbers([1, 2, 3])
    output = capfd.readouterr()[0]
    assert output.count('not all ints') == 0


def test_decorated_function_preserves_docstring(capfd):
    docstring = sum_numbers.__doc__
    assert docstring is not None
    assert "Sum numbers, if not all ints raise a ValueError" in docstring
    assert "(bit silly but justs to test the decorator)" in docstring


def test_decorator_returns_function():
    ret = sum_numbers([1, 2, 3])
    assert ret == 6