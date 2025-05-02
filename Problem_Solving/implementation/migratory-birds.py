# Problem: Migratory Birds
# https://www.hackerrank.com/challenges/migratory-birds

import math

def migratoryBirds(arr):
    """
    Determines the most frequently sighted bird type from a list of sightings.
    Bird types are represented as integers in the range 1 to 5.

    In case of a tie (multiple types with the same highest count), 
    the function returns the bird type with the smallest numerical ID.

    Args:
        arr (List[int]): A list of integers representing bird type sightings.

    Returns:
        int: The bird type (1 to 5) that has the highest frequency.

    Example:
        >>> migratoryBirds([1, 1, 2, 2, 3])
        1
    """
    # Initialize a list of 5 elements to count bird sightings (index 0 = type 1, ..., index 4 = type 5)
    arr_type = [0] * 5

    # Count each bird type's occurrences
    for num in arr:
        arr_type[num - 1] += 1

    # Find the index of the maximum value (most frequent bird type)
    # Add 1 to convert from 0-based index to bird type number
    max_value = arr_type.index(max(arr_type)) + 1

    # Return the most frequently sighted bird type
    return max_value

if __name__ == '__main__':
    # Example test case
    arr = [1, 1, 2, 2, 3]
    print(migratoryBirds(arr))  # Expected output: 1
