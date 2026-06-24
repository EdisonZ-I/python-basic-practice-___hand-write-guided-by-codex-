def dot_product(a, b):
    if len(a) != len(b): return None
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

if __name__ == "__main__":
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert dot_product([1, 2], [3]) is None
    assert dot_product([], []) == 0
