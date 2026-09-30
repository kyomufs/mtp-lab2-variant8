"""Task 8 (advanced): binary search in a sorted sequence."""


def binary_search(items: list, target) -> int:
    """Return the index of ``target`` in sorted ``items`` or ``-1``.

    Args:
        items: sequence sorted in ascending order.
        target: value to look for.

    Returns:
        Index of the first matching element, or ``-1`` when absent.
    """
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
