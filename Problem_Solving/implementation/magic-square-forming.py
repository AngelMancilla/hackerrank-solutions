# Problem: Forming a Magic Square
# https://www.hackerrank.com/challenges/magic-square-forming

def formingMagicSquare(s):
    """
    Calculates the minimal cost to convert a 3x3 matrix into a magic square.

    A magic square is a 3x3 matrix with distinct integers from 1 to 9
    such that the sum of each row, column, and both diagonals is equal (magic constant = 15).

    Args:
        s (list[list[int]]): A 3x3 matrix with integers from 1 to 9.

    Returns:
        int: Minimum cost to convert s into a magic square.
    """

    # List of all 8 possible 3x3 magic squares using numbers 1 to 9
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    min_cost = float('inf')

    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])
        min_cost = min(min_cost, cost)

    return min_cost


if __name__ == '__main__':
    # Read input from the user: 3 lines of 3 space-separated integers
    s = []
    for _ in range(3):
        row = list(map(int, input().strip().split()))
        s.append(row)

    # Compute and print the minimal cost
    result = formingMagicSquare(s)
    print(result)
