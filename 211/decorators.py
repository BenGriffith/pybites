from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #

    retry = 0
    @wraps(func)
    def wrapper(*args):
        nonlocal retry
        try:
            for arg in args[0]:
                print(arg)
                if not isinstance(arg, int):
                    raise ValueError

        except ValueError:
            print("not all ints")
            retry += 1
            if retry >= MAX_RETRIES:
                raise MaxRetriesException()
            else:
                return wrapper(*args)
        return func(*args)
            
    return wrapper