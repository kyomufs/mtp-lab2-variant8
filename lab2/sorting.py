"""Task 1 (advanced): bubble sort."""


def bubble_sort(items: list) -> list:
    """Return a new list with ``items`` sorted in ascending order.

    Adjacent elements are swapped until no swap is needed, so the
    loop stops early on already sorted input.

    Args:
        items: source sequence of mutually comparable elements.

    Returns:
        A new sorted list; the input stays untouched.
    """
    result = list(items)
    size = len(result)
    for pass_number in range(size):
        swapped = False
        last = size - 1 - pass_number
        for index in range(last):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = (
                    result[index + 1],
                    result[index],
                )
                swapped = True
        if not swapped:
            break
    return result
