# Problem: Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference

def diagonalDifference(arr):
    """
    Calculates the absolute difference between the sums of the matrix's two diagonals.

    Parameters:
    arr (list of list of int): A square matrix of integers.

    Returns:
    int: Absolute difference between the primary and secondary diagonal sums.
    """
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        primary_sum += arr[i][i]             # Top-left to bottom-right
        secondary_sum += arr[i][n - i - 1]    # Top-right to bottom-left

    return abs(primary_sum - secondary_sum)

if __name__ == '__main__':
    # Example tests
    print(diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: 0
    print(diagonalDifference([[1, 2], [3, 4]]))  # Output: 2
    print(diagonalDifference([[1]]))  # Output: 0
    print(diagonalDifference([[1, 2], [3, 4]]))  # Output: 2
    print(diagonalDifference([[5, 3], [2, 4]]))  # Output: 0
