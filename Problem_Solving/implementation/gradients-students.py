# Problem: Grading Students
# https://www.hackerrank.com/challenges/grading

import math
 
def get_distance(grade):
    """
    Calculates the difference between a grade and the next multiple of 5.

    Parameters:
    grade (int): The original grade

    Returns:
    int: The difference between the grade and the next multiple of 5
    """
    multiplo_5 = 5 * math.ceil(grade / 5)
    return multiplo_5 - grade


def gradingStudents(grades):
    """
    Applies HackerLand University's grading policy to a list of student grades.

    Rules:
    - Any grade less than 38 is a failing grade and is not rounded.
    - If the difference between the grade and the next multiple of 5 is less than 3, 
      the grade is rounded up to that multiple.
    - If the difference is 3 or more, the grade is not changed.

    Parameters:
    grades (list of int): List of original student grades

    Returns:
    list of int: List of grades after applying the rounding policy
    """
    new_grades = []
    
    for grade in grades:
        distance = get_distance(grade)
        
        if grade < 38 or distance >= 3:
            new_grades.append(grade)
        else:
            new_grades.append(grade + distance)
    
    return new_grades

if __name__ == "__main__":
    # example tests
    print(gradingStudents([73, 67, 38, 33]))  # Output: [75, 67, 40, 33]
    print(gradingStudents([84, 29, 57, 38]))  # Output: [85, 29, 57, 40]
    print(gradingStudents([38, 39, 40]))  # Output: [40, 40, 40]
    print(gradingStudents([0, 1, 2]))  # Output: [0, 1, 2]