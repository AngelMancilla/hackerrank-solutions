# Problem: Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets

def compareTriplets(a, b):
    """
    Compares elements of two triplets and returns the comparison points.

    Parameters:
    a (list of int): Alice's ratings (length 3)
    b (list of int): Bob's ratings (length 3)

    Returns:
    list of int: [Alice's score, Bob's score]
    """
    alice_score = 0
    bob_score = 0

    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
        # If equal, no points are awarded

    return [alice_score, bob_score]

if __name__ == '__main__':
    # Example tests
    print(compareTriplets([5, 6, 7], [3, 6, 10]))  # Output: [1, 1]
    print(compareTriplets([17, 28, 30], [99, 16, 8]))  # Output: [2, 1]
    print(compareTriplets([1, 2, 3], [1, 2, 3]))  # Output: [0, 0]
    print(compareTriplets([10, 20, 30], [30, 20, 10]))  # Output: [1, 1]