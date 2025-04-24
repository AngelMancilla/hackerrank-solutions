# Problem: Between Two Sets
# https://www.hackerrank.com/challenges/between-two-sets

import math
from functools import reduce

def mcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers.

    Parameters:
        a: First integer.
        b: Second integer.

    Returns:
        The GCD of a and b.
    """
    return math.gcd(a, b)


def mcm(a: int, b: int) -> int:
    """
    Compute the least common multiple (LCM) of two integers.

    Parameters:
        a: First integer.
        b: Second integer.

    Returns:
        The LCM of a and b.
    """
    return abs(a * b) // math.gcd(a, b)


def mcd_array(arr: list[int]) -> int:
    """
    Compute the GCD of a list of integers.

    Parameters:
        arr: List of integers.

    Returns:
        The GCD of all elements in arr.
    """
    return reduce(mcd, arr)


def mcm_array(arr: list[int]) -> int:
    """
    Compute the LCM of a list of integers.

    Parameters:
        arr: List of integers.

    Returns:
        The LCM of all elements in arr.
    """
    def _lcm_pair(x: int, y: int) -> int:
        """Helper to compute LCM of two integers."""
        return abs(x * y) // math.gcd(x, y)

    return reduce(_lcm_pair, arr)


def getTotalX(a: list[int], b: list[int]) -> int:
    """
    Count the integers that are multiples of all elements in a
    and divisors of all elements in b.

    Parameters:
        a: List of ‘lower-bound’ integers (each must divide the candidate).
        b: List of ‘upper-bound’ integers (candidate must divide each).

    Returns:
        The number of integers x such that:
          - every element in a divides x, and
          - x divides every element in b.
    """
    # smallest step that satisfies all of a
    L = mcm_array(a)
    # largest common target that must be divisible by x
    G = mcd_array(b)

    count = 0
    k = 1
    # iterate multiples of L up to G
    while (candidate := k * L) <= G:
        if G % candidate == 0:
            count += 1
        k += 1

    return count

if __name__ == '__main__':
    # Example usage
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = getTotalX(a, b)
    print(result)