import hashlib

def hash_query(query: str, length: int = 32) -> str:
    """Return a hash value for a given query.

    Args:
        query (str): An SQL query.
        length (int, optional): Length of the hash value. Defaults to 32.

    Raises:
        ValueError: Parameter length has to be greater equal 1.
        TypeError: Parameter length has to be of type integer.

    Returns:
        str: String representation of the hashed value.
    """
    if not isinstance(length, int):
        raise TypeError

    if length < 1:
        raise ValueError

    query = query.replace("\"", "").lower().strip()
    query = " ".join(sorted(query.split()))
    result = hashlib.blake2b(query.encode()).hexdigest()
    return result[:length]