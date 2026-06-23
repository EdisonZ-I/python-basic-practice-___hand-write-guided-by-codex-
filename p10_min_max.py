def find_min(numbers):
    if not numbers: return None
    else:
        minnum=numbers[0]
        for i in numbers:
            if minnum > i: minnum = i
        return minnum
    
def find_max(numbers):
    if not numbers: return None
    else:
        maxnum=numbers[0]
        for i in numbers:
            if maxnum < i: maxnum = i
        return maxnum

def min_max(numbers):
    if not numbers: return None
    else: return (find_min(numbers), find_max(numbers))

if __name__ == "__main__":
    assert find_min([3, 1, 5]) == 1
    assert find_max([3, 1, 5]) == 5
    assert min_max([3, 1, 5]) == (1, 5)
    assert find_min([]) is None
    assert min_max([]) is None