# Problem: A Very Big Sum
# https://www.hackerrank.com/challenges/a-very-big-sum

def aVeryBigSum(arr):
    """
    Computes the sum of an array of large integers.

    Parameters:
    arr (list of int): An array of integers

    Returns:
    int: The sum of the array elements
    """
    return sum(arr)

if __name__ == '__main__':
    # Example tests
    print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))  # Output: 5000000015
    print(aVeryBigSum([1, 2, 3]))  # Output: 6
    print(aVeryBigSum([-1, -2, -3]))  # Output: -6
    print(aVeryBigSum([0, 0, 0]))  # Output: 0
    print(aVeryBigSum([1000000000, 2000000000, 3000000000]))  # Output: 6000000000