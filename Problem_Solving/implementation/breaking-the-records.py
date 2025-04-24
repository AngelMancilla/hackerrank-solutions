# Problem: Breaking the Records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

def breakingRecords(scores):
    """
    Determines how many times a record is broken for both highest and lowest scores.

    Parameters:
    scores (list of int): A list of integers representing the scores.

    Returns:
    list of int: A list with two integers:
        - The first is the count of times the highest score is broken.
        - The second is the count of times the lowest score is broken.
    """
    highest_score = lowest_score = scores[0] 
    highest_count = lowest_count = 0

    for score in scores[1:]:
        if score > highest_score:
            highest_score = score
            highest_count += 1
        elif score < lowest_score:
            lowest_score = score
            lowest_count += 1
    
    return [highest_count, lowest_count]

if __name__ == '__main__':
    # example test
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    result = breakingRecords(scores)
    print(result)  # Output: [2, 4]