"""Task 4 (medium): greatest common divisor."""


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of ``a`` and ``b``.

    The divisor is found by checking every candidate from 1 up to
    the smaller absolute value, which keeps the solution simple and
    independent from the advanced Euclidean algorithm task.

    Args:
        a: first integer.
        b: second integer.

    Returns:
        The largest positive integer dividing both values.

    Raises:
        ValueError: if both values are zero.
    """
    if a == 0 and b == 0:
        raise ValueError("GCD of two zero values is undefined")
    first, second = abs(a), abs(b)
    if first == 0:
        return second
    if second == 0:
        return first
    divisor = 1
    for candidate in range(1, min(first, second) + 1):
        if first % candidate == 0 and second % candidate == 0:
            divisor = candidate
    return divisor
