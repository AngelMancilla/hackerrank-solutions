# Problem: Cats and a Mouse
# https://www.hackerrank.com/challenges/cats-and-a-mouse

def catAndMouse(x, y, z):
    """
    Determines which cat will catch the mouse first based on their positions.

    Args:
        x (int): The position of Cat A.
        y (int): The position of Cat B.
        z (int): The position of the Mouse.

    Returns:
        str: 'Cat A' if Cat A reaches the mouse first,
             'Cat B' if Cat B reaches the mouse first,
             or 'Mouse C' if both cats reach at the same time.
    """
    dist_cat_a = abs(x - z)
    dist_cat_b = abs(y - z)

    if dist_cat_a < dist_cat_b:
        return "Cat A"
    elif dist_cat_b < dist_cat_a:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    # Sample test cases from problem description
    print(catAndMouse(1, 2, 3))  # Expected: Cat B
    print(catAndMouse(1, 3, 2))  # Expected: Mouse C

    # Additional test cases
    print(catAndMouse(5, 1, 3))  # Expected: Mouse C
    print(catAndMouse(2, 6, 4))  # Expected: Mouse C
    print(catAndMouse(2, 5, 4))  # Expected: Cat B
    print(catAndMouse(6, 2, 4))  # Expected: Mouse C
