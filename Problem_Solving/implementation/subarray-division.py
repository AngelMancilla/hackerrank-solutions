# Problem: Subarray Division
# https://www.hackerrank.com/challenges/the-birthday-bar

def birthday(s, d, m):
    """
    Determines how many ways Lily can divide the chocolate bar such that:
    - The segment length equals Ron's birth month (m), and
    - The sum of the segment equals Ron's birth day (d)

    Parameters:
    s (list of int): The numbers on the chocolate squares
    d (int): Ron's birth day
    m (int): Ron's birth month

    Returns:
    int: Number of valid ways to divide the chocolate
    """

    count = 0  # Counter for valid segments

    # Calculate the sum of the first segment of length 'm'
    current_sum = sum(s[0:m])

    # Check if the first segment meets the condition
    if current_sum == d:
        count += 1

    # Slide the window through the array
    for i in range(1, len(s) - m + 1):
        # Update the sum by removing the leftmost element and adding the new rightmost one
        current_sum = current_sum - s[i - 1] + s[i + m - 1]

        # Check if the updated segment meets the condition
        if current_sum == d:
            count += 1

    return count  # Return the total count of valid segments


if __name__ == '__main__':
    # example test
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    print(birthday(s, d, m)) # expected output: 2