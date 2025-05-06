# Problem: Bill Division
# https://www.hackerrank.com/challenges/bon-appetit

def bonAppetit(bill, k, b):
    """
    Determines whether Brian correctly charged Anna for her share of the bill.
    Anna did not eat item at index k, and Brian split the rest of the bill.

    Args:
        bill (List[int]): List of item prices.
        k (int): Index of the item Anna did not eat.
        b (int): The amount of money Brian charged Anna.

    Returns:
        None: Prints "Bon Appetit" if Anna was correctly charged.
              Otherwise, prints the overcharged amount (an integer).

    Example:
        >>> bonAppetit([3, 10, 2, 9], 1, 12)
        5
        >>> bonAppetit([3, 10, 2, 9], 1, 7)
        Bon Appetit
    """
    # Calculate Anna's fair share, excluding item k
    actual_share = (sum(bill) - bill[k]) // 2

    # Print result based on comparison
    if b == actual_share:
        print("Bon Appetit")
    else:
        print(b - actual_share)


if __name__ == '__main__':
    # Example test cases
    bonAppetit([3, 10, 2, 9], 1, 12)  # Expected: 5
    bonAppetit([3, 10, 2, 9], 1, 7)   # Expected: Bon Appetit