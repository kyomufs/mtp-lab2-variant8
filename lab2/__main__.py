"""Demo entry point: run ``python -m lab2``."""

from lab2.gcd import gcd
from lab2.reverse import reverse_string
from lab2.searching import binary_search
from lab2.sorting import bubble_sort
from lab2.squares import squares_dict


def main() -> None:
    """Print results of every variant task."""
    print("Medium tasks")
    print('reverse_string("lab2") ->', reverse_string("lab2"))
    print("squares_dict(5) ->", squares_dict(5))
    print("gcd(48, 18) ->", gcd(48, 18))
    numbers = [1, 3, 5, 7, 9, 11]
    print("binary_search(7) ->", binary_search(numbers, 7))
    print("bubble_sort([5, 1, 4, 2]) ->", bubble_sort([5, 1, 4, 2]))


if __name__ == "__main__":
    main()
