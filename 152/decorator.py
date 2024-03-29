from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            result = list(kwargs.get("text"))

            if start < end:
                for i in range(start, end):
                    if i < 0:
                        continue
                    try:
                        result[i] = DOT
                    except IndexError:
                        break
            return "".join(result)

        return wrapper
    return decorator