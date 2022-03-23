from functools import lru_cache

@lru_cache(maxsize=32)
def cached_fib(n):
    if n in [0, 1]:
        return n
    else:
        return cached_fib(n - 2) + cached_fib(n - 1)


if __name__ == "__main__":
    print(cached_fib(6))