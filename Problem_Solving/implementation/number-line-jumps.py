# Problem: Number Line Jumps
# https://www.hackerrank.com/challenges/kangaroo

def kangaroo(x1, v1, x2, v2):
    """
    Determine if two kangaroos starting at positions x1 and x2 with jump distances
    v1 and v2 respectively will land at the same location after the same number of jumps.

    Parameters:
    x1 (int): Starting position of kangaroo 1.
    v1 (int): Jump distance for kangaroo 1.
    x2 (int): Starting position of kangaroo 2.
    v2 (int): Jump distance for kangaroo 2.

    Returns:
    str: "YES" if there exists a non-negative integer n such that
         x1 + n*v1 == x2 + n*v2; otherwise, "NO".
    """
    # If they start at the same position, they already meet at n=0
    if x1 == x2:
        return "YES"
        
    # Identify which kangaroo is behind
    if x1 < x2:
        behind_p, behind_v = x1, v1
        front_p,  front_v  = x2, v2
    else:
        behind_p, behind_v = x2, v2
        front_p,  front_v  = x1, v1
    
    # If the one behind doesn't jump farther, it can never catch up
    if behind_v <= front_v:
        return "NO"
    
    # Compute the distance to close and the extra distance per jump
    distance_to_catch = front_p - behind_p       # positive integer
    step_difference   = behind_v - front_v       # positive integer
    
    # They meet if and only if the distance is an exact multiple of step_difference
    if distance_to_catch % step_difference == 0:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    # Example test case
    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    result = kangaroo(x1, v1, x2, v2)
    print(result)  # Expected output: "YES"