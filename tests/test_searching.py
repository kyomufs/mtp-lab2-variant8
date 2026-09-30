"""Tests for the binary search task."""

import unittest

from lab2.searching import binary_search


class BinarySearchTests(unittest.TestCase):
    """Checks for :func:`binary_search`."""

    def setUp(self) -> None:
        """Prepare a sorted sample sequence."""
        self.data = [1, 3, 5, 7, 9, 11]

    def test_existing_value(self) -> None:
        """An existing value reports its index."""
        self.assertEqual(binary_search(self.data, 7), 3)

    def test_missing_value(self) -> None:
        """A missing value reports minus one."""
        self.assertEqual(binary_search(self.data, 4), -1)

    def test_empty_sequence(self) -> None:
        """An empty sequence never contains anything."""
        self.assertEqual(binary_search([], 1), -1)


if __name__ == "__main__":
    unittest.main()
