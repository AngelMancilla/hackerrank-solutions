# Problem: Day of the Programmer
# https://www.hackerrank.com/challenges/day-of-the-programmer

def dayOfProgrammer(year):
    """
    Determines the Day of the Programmer (the 256th day of the year)
    in Russia, for a given year between 1700 and 2700.

    Russia used the Julian calendar from 1700 to 1917, 
    transitioned in 1918, and adopted the Gregorian calendar from 1919 onward.

    Leap year rules:
        - Julian (1700–1917): leap year if divisible by 4.
        - Gregorian (1919–2700): leap year if divisible by 400, 
          or divisible by 4 and not divisible by 100.
        - Year 1918: February had only 15 days (transition year), so the 256th day is on 26 September.

    Args:
        year (int): A year between 1700 and 2700.

    Returns:
        str: The Day of the Programmer in the format "dd.mm.yyyy".

    Example:
        >>> dayOfProgrammer(2017)
        '13.09.2017'
    """
    # Handle the transition year (1918) separately
    if year == 1918:
        return f"26.09.{year}"

    # Determine if it's a leap year using Julian or Gregorian rules
    is_julian_leap = (year < 1918 and year % 4 == 0)
    is_gregorian_leap = (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)))

    # Set the correct day in September depending on leap year status
    if is_julian_leap or is_gregorian_leap:
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"


if __name__ == '__main__':
    # Example test cases
    print(dayOfProgrammer(2017))  # Expected: '13.09.2017'
    print(dayOfProgrammer(2016))  # Expected: '12.09.2016'
    print(dayOfProgrammer(1800))  # Expected: '12.09.1800'
    print(dayOfProgrammer(1918))  # Expected: '26.09.1918'
