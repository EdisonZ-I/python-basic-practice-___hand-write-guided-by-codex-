def is_positive(n):
    return n > 0

def count_positive(numbers):
    count = 0
    for i in numbers:
        if is_positive(i): count += 1
    return count

def positive_ratio(numbers):
    if numbers == []: return 0
    else: return ( count_positive(numbers) / float(len(numbers)) )


if __name__ == "__main__":
    assert is_positive(3) is True
    assert is_positive(0) is False
    assert count_positive([-1, 0, 2, 5]) == 2
    assert positive_ratio([-1, 0, 2, 5]) == 0.5
    assert positive_ratio([]) == 0
    print ("1")