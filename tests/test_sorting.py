"""Tests for the bubble sort task."""

import unittest

from lab2.sorting import bubble_sort


class BubbleSortTests(unittest.TestCase):
    """Checks for :func:`bubble_sort`."""

    def test_unordered_values(self) -> None:
        """Values come out sorted ascending."""
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_input_is_untouched(self) -> None:
        """The source list keeps its original order."""
        source = [3, 1, 2]
        bubble_sort(source)
        self.assertEqual(source, [3, 1, 2])

    def test_empty_sequence(self) -> None:
        """An empty sequence stays empty."""
        self.assertEqual(bubble_sort([]), [])


if __name__ == "__main__":
    unittest.main()
