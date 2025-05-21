# Problem: Counting Valleys
# https://www.hackerrank.com/challenges/counting-valleys

def countingValleys(steps, path):
    """
    Counts the number of valleys in a given hike.

    A valley is a sequence of steps below sea level, starting with a step down 
    from sea level and ending with a step up to sea level.

    Args:
        steps (int): The total number of steps taken during the hike.
        path (str): A string of 'U' (up) and 'D' (down) representing the hike path.

    Returns:
        int: The number of valleys traversed.
    """
    sea_level = 0
    elevation = 0
    valleys = 0

    for step in path:
        if step == 'U':
            elevation += 1
            if elevation == 0:
                valleys += 1  # just came up from a valley
        else:  # step == 'D'
            elevation -= 1

    return valleys


if __name__ == '__main__':
    # Example test case from problem description
    print(countingValleys(8, "UDDDUDUU"))  # Expected: 1

    # Additional test cases
    print(countingValleys(12, "DDUUDDUDUUUD"))  # Expected: 2
    print(countingValleys(10, "DUDDDUUDUU"))    # Expected: 2
    print(countingValleys(5, "DUUDD"))          # Expected: 1
    print(countingValleys(4, "DDUU"))           # Expected: 1
