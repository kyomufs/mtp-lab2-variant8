"""Tests for the squares dictionary task."""

import unittest

from lab2.squares import squares_dict


class SquaresDictTests(unittest.TestCase):
    """Checks for :func:`squares_dict`."""

    def test_first_five_numbers(self) -> None:
        """Every number is mapped to its square."""
        self.assertEqual(
            squares_dict(5),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25},
        )

    def test_zero_limit(self) -> None:
        """A zero limit produces an empty mapping."""
        self.assertEqual(squares_dict(0), {})

    def test_negative_limit(self) -> None:
        """A negative limit is rejected."""
        with self.assertRaises(ValueError):
            squares_dict(-1)


if __name__ == "__main__":
    unittest.main()
