def binary_search(sorted_numbers, target):
    lower = 0
    upper = len(sorted_numbers)
    while lower < upper:
        test = (lower + upper)//2
        if sorted_numbers[test] == target: return test
        if sorted_numbers[test] > target: upper = test
        if sorted_numbers[test] < target: lower = test + 1
    return -1

if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([], 1) == -1
    assert binary_search([2], 2) == 0
