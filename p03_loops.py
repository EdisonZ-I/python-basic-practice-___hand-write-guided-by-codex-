def sum_to_n(n):
    Sum = 0
    for i in range(n+1):
        Sum += i
    return Sum

def factorial (n):
    Fac = 1
    for i in range(1, n+1):
        Fac *= i
    return Fac

def count_even_numbers(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0: count +=1
    return count

if __name__ == "__main__":
    assert sum_to_n(5) == 15
    assert sum_to_n(1) == 1
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert count_even_numbers([1, 2, 3, 4, 6]) == 3
    assert count_even_numbers([]) == 0
    print ("1")
