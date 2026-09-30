"""Task 10 (medium): dictionary of squares."""


def squares_dict(limit: int) -> dict:
    """Build ``{i: i * i}`` mapping for every ``i`` from 1 to ``limit``.

    Args:
        limit: upper bound of the range, inclusive and non-negative.

    Returns:
        Dictionary mapping each number to its square.

    Raises:
        ValueError: if ``limit`` is negative.
    """
    if limit < 0:
        raise ValueError("limit must be non-negative")
    squares = {}
    for number in range(1, limit + 1):
        squares[number] = number * number
    return squares
