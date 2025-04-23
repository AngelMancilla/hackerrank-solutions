# Problem: Apple and Orange
# https://www.hackerrank.com/challenges/apple-and-orange

def count_falling_in_range(tree_pos, fruits, s, t):
    """
    Count how many fruits fall within the house range.

    Parameters:
    tree_pos (int): The position of the tree on the x‑axis.
    fruits (Iterable[int]): Distances each fruit falls from tree_pos.
    s (int): Start point of Sam's house.
    t (int): End point of Sam's house (inclusive).

    Returns:
    int: Number of fruits that land on the house (i.e., between s and t).
    """
    # For each distance d in fruits, compute absolute position (tree_pos + d)
    # and count it if it lies within the inclusive range [s, t].
    return sum(
        1
        for d in fruits
        if s <= tree_pos + d <= t
    )

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Calculate and print the number of apples and oranges that land on Sam's house.

    Parameters:
    s (int): Start point of Sam's house.
    t (int): End point of Sam's house (inclusive).
    a (int): Position of the apple tree.
    b (int): Position of the orange tree.
    apples (Iterable[int]): Distances each apple falls from the apple tree.
    oranges (Iterable[int]): Distances each orange falls from the orange tree.

    Side Effects:
    Prints two lines:
      1) Number of apples that land on the house.
      2) Number of oranges that land on the house.
    """
    # Count apples landing on the house
    apples_on_house = count_falling_in_range(a, apples, s, t)
    # Count oranges landing on the house
    oranges_on_house = count_falling_in_range(b, oranges, s, t)

    # Print results as required by the problem statement
    print(apples_on_house)
    print(oranges_on_house)

if __name__ == "__main__":
    # Example test case
    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges) 