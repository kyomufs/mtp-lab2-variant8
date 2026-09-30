"""Tests for the greatest common divisor task."""

import unittest

from lab2.gcd import gcd


class GcdTests(unittest.TestCase):
    """Checks for :func:`gcd`."""

    def test_coprime_values(self) -> None:
        """Coprime values have no common divisor above one."""
        self.assertEqual(gcd(17, 5), 1)

    def test_shared_divisor(self) -> None:
        """A regular pair reports its greatest divisor."""
        self.assertEqual(gcd(48, 18), 6)

    def test_zero_operand(self) -> None:
        """Zero with a number gives that number's magnitude."""
        self.assertEqual(gcd(0, 7), 7)
        self.assertEqual(gcd(-7, 0), 7)

    def test_both_zero(self) -> None:
        """Two zeros have no defined divisor."""
        with self.assertRaises(ValueError):
            gcd(0, 0)


if __name__ == "__main__":
    unittest.main()
