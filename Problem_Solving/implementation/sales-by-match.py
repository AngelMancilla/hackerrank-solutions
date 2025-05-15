# Problem: Sales by Match
# https://www.hackerrank.com/challenges/sock-merchant

def sockMerchant(n, ar):
    """
    Counts how many pairs of socks with matching colors there are in a pile.

    Args:
        n (int): The total number of socks (not used in the function logic).
        ar (List[int]): A list of integers representing the color of each sock.

    Returns:
        int: The total number of matching pairs of socks.
    """
    # Dictionary to count how many socks of each color
    color_counts = {}
    for color in ar:
        color_counts[color] = color_counts.get(color, 0) + 1

    # Count how many full pairs can be made from each color
    pairs = 0
    for count in color_counts.values():
        pairs += count // 2

    return pairs


if __name__ == '__main__':
    # Example test cases
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))  # Expected: 3
    print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))                # Expected: 2
    print(sockMerchant(4, [1, 1, 1, 1]))                         # Expected: 2
    print(sockMerchant(0, []))                                   # Expected: 0
                               # Expected: 0