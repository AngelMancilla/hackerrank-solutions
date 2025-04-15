# Problem: Staircase
# https://www.hackerrank.com/challenges/staircase

def staircase(n):
    """
    Prints a right-aligned staircase of size `n` using '#' characters.

    Parameters:
    n (int): The height and base width of the staircase.

    Output:
    Prints the staircase with n lines, right-aligned, using spaces and '#' symbols.
    """
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)
        
if __name__ == '__main__':
    # Example tests
    staircase(6)  # Expected output: a staircase of height 6
    staircase(4)  # Expected output: a staircase of height 4
    staircase(1)  # Expected output: a staircase of height 1
    staircase(0)  # Expected output: no staircase (empty)