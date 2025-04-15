# Problem: Simple Array Sum
# https://www.hackerrank.com/challenges/simple-array-sum

def simpleArraySum(ar):
    """
    Returns the sum of all integers in the array.

    Parameters:
    ar (list of int): List of integers to sum.

    Returns:
    int: The total sum of all elements in the array.
    """
    return sum(ar)


if __name__ == '__main__':
    # Example tests
    print(simpleArraySum([1, 2, 3, 4, 5]))  # Output: 15
    print(simpleArraySum([-1, -2, -3]))     # Output: -6
    print(simpleArraySum([0, 0, 0]))        # Output: 0
    print(simpleArraySum([100, 200, 300]))  # Output: 600
