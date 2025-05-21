# Problem: Electronics Shop
# https://www.hackerrank.com/challenges/electronics-shop

def getMoneySpent(keyboards, drives, b):
    """
    Finds the maximum amount of money that can be spent on one keyboard and one USB drive
    without exceeding the given budget.

    Args:
        keyboards (list of int): The prices of available keyboard models.
        drives (list of int): The prices of available USB drives.
        b (int): The maximum budget available to spend.

    Returns:
        int: The maximum amount that can be spent on one keyboard and one USB drive,
             or -1 if no combination is affordable within the budget.
    """
    max_spent = -1  # Start with -1 to indicate no valid combination found

    # Try all combinations of keyboards and drives
    for k in keyboards:
        for d in drives:
            total = k + d

            # If the total is within budget, update max_spent
            if total <= b:
                max_spent = max(max_spent, total)

    return max_spent


if __name__ == '__main__':
    # Sample test case 0
    print(getMoneySpent([3, 1], [5, 2, 8], 10))  # Expected: 9

    # Sample test case 1
    print(getMoneySpent([4], [5], 5))  # Expected: -1

    # Additional test cases
    print(getMoneySpent([2, 3], [1, 2], 3))  # Expected: 3
    print(getMoneySpent([10, 20, 30], [5, 10], 40))  # Expected: 40
    print(getMoneySpent([5, 6], [7, 8], 9))  # Expected: -1
