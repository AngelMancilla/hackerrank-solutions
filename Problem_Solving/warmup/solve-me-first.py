# Problem: Solve Me First
# https://www.hackerrank.com/challenges/solve-me-first

def solveMeFirst(a, b):
    """
    Computes the sum of two integers.

    Parameters:
    a (int): the first value
    b (int): the second value

    Returns:
    int: the sum of a and b
    """
    return a + b

if __name__ == '__main__':
    # Example tests
    print(solveMeFirst(2, 3))  # Output: 5
    print(solveMeFirst(10, 20))  # Output: 30
    print(solveMeFirst(-1, 1))  # Output: 0
    print(solveMeFirst(0, 0))  # Output: 0 (Both inputs are zero)