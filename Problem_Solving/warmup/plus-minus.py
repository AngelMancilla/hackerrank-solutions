# Problem: Plus Minus
# https://www.hackerrank.com/challenges/plus-minus

def plusMinus(arr):
    """
    Prints the ratios of positive, negative, and zero values in the array.
    
    Parameters:
    arr (list of int): The input array of integers.

    Output:
    Prints 3 lines, each showing the ratio of positive, negative, and zero values (respectively)
    with 6 digits after the decimal.
    """
    n = len(arr)
    pos = neg = zero = 0

    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zero/n:.6f}")

if __name__ == '__main__':
    # Example tests
    plusMinus([-4, 3, -9, 0, 4, 1])  # Output: 0.500000, 0.333333, 0.166667
    plusMinus([1, 1, 0, -1, -1])      # Output: 0.400000, 0.400000, 0.200000
    plusMinus([1])                    # Output: 1.000000, 0.000000, 0.000000
    plusMinus([-1])                   # Output: 0.000000, 1.000000, 0.000000
    plusMinus([0])                    # Output: 0.000000, 0.000000, 1.000000