"""Task 8 (medium): reverse a string."""


def reverse_string(text: str) -> str:
    """Return ``text`` with its characters in reverse order.

    Args:
        text: source string, may be empty.

    Returns:
        The reversed string.
    """
    result = ""
    for char in text:
        result = char + result
    return result
