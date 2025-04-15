# Problem: Mini-Max Sum
# https://www.hackerrank.com/challenges/mini-max-sum

def miniMaxSum(arr):
    """
    Prints the minimum and maximum sum of exactly four out of five integers.

    Parameters:
    arr (list of int): A list of five positive integers.

    Output:
    Prints two space-separated integers: the minimum sum and the maximum sum.
    """
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    # Example tests
    miniMaxSum([1, 2, 3, 4, 5])  # Expected output: 10 14
    miniMaxSum([7, 69, 2, 221, 8974])  # Expected output: 299 9271
    miniMaxSum([1, 1, 1, 1, 1])  # Expected output: 4 4
    miniMaxSum([0, 0, 0, 0, 0])  # Expected output: 0 0