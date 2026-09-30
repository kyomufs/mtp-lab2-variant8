"""Tests for the string reversal task."""

import unittest

from lab2.reverse import reverse_string


class ReverseStringTests(unittest.TestCase):
    """Checks for :func:`reverse_string`."""

    def test_regular_string(self) -> None:
        """Characters change their order."""
        self.assertEqual(reverse_string("lab2"), "2bal")

    def test_empty_string(self) -> None:
        """Empty input stays empty."""
        self.assertEqual(reverse_string(""), "")

    def test_palindrome(self) -> None:
        """A palindrome maps onto itself."""
        self.assertEqual(reverse_string("шалаш"), "шалаш")


if __name__ == "__main__":
    unittest.main()
