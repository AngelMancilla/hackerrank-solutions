# Problem: Divisible Sum Pairs
# https://www.hackerrank.com/challenges/divisible-sum-pairs

def divisibleSumPairs(n, k, ar):
    """
    Counts the number of pairs (i, j) in the array such that i < j 
    and (ar[i] + ar[j]) is divisible by k.

    Args:
        n (int): The length of the array.
        k (int): The integer divisor.
        ar (List[int]): A list of integers.

    Returns:
        int: The number of valid (i, j) pairs where the sum is divisible by k.

    Example:
        >>> divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
        5
    """
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    # Example test case
    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    print(divisibleSumPairs(n, k, ar))  # Expected output: 5