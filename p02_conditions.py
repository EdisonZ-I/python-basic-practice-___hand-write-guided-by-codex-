def grade(score):
    if score >= 90: return "A"
    elif score >= 80 : return "B"
    elif score >= 70 : return "C"
    elif score >= 60 : return "D"
    else: return "F"

def is_even(n):
    return (n%2==0)

def max_of_three(a, b, c):
    MOT = a
    if b > MOT: MOT = b
    if c > MOT: MOT = c
    return MOT

if __name__ == "__main__":
    assert grade(95) == "A"
    assert grade(80) == "B"
    assert grade(59) == "F"
    assert is_even(10) is True
    assert is_even(7) is False
    assert max_of_three(3, 9, 5) == 9
    assert max_of_three(-1, -3, -2) == -1
    print ("all past")