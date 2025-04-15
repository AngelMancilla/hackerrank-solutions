# Problem: Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles

def birthdayCakeCandles(candles):
    """
    This function takes a list of integers representing the heights of birthday cake candles.
    It returns the number of candles that have the tallest height.

    Parameters:
    candles (list of int): A list where each element represents the height of a candle.

    Returns:
    int: The count of the tallest candles in the list.

    Logic:
    - The function iterates through the list to find the tallest candle.
    - It keeps track of the number of candles that share the maximum height.
    """
    tallest = 0
    total_tallest = 0

    for candle in candles:
        if candle > tallest:
            tallest = candle
            total_tallest = 1
        elif candle == tallest:
            total_tallest += 1

    return total_tallest

if __name__ == '__main__':
    # Example tests
    print(birthdayCakeCandles([3, 2, 1, 3]))  # Output: 2
    print(birthdayCakeCandles([1, 1, 1, 1]))  # Output: 4 (All are the tallest)
    print(birthdayCakeCandles([5, 4, 4, 2, 3]))  # Output: 1 (Only one candle is the tallest)
    print(birthdayCakeCandles([10]))  # Output: 1 (Single candle)


