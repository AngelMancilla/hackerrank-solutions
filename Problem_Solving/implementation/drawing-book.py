# Problem: Drawing Book
# https://www.hackerrank.com/challenges/drawing-book

def pageCount(n, p):
    """
    Calculates the minimum number of pages to turn to reach a specific page
    in a book, either starting from the front or the back.

    Args:
        n (int): The total number of pages in the book.
        p (int): The target page number to reach.

    Returns:
        int: The minimum number of pages that must be turned.
    """
    # Calculate page turns from the front
    front_turns = p // 2

    # Calculate page turns from the back
    back_turns = n // 2 - p // 2

    # Return the smaller of the two options
    return min(front_turns, back_turns)


if __name__ == '__main__':
    # Example test cases
    print(pageCount(6, 5))  # Expected: 1
    print(pageCount(5, 4))  # Expected: 0
    print(pageCount(7, 3))  # Expected: 1
    print(pageCount(4, 4))  # Expected: 0
    print(pageCount(100, 99))  # Expected: 0
