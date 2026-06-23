def prefix_sum(numbers):
    result=[]
    if numbers: result.append(numbers[0])
    for i in numbers[1:]:
        result.append(result[-1]+i)
    return result

def range_sum(prefix, left, right):
    if left == 0: return prefix[right]
    else: return prefix[right]-prefix[left-1]

if __name__ == "__main__":
    p = prefix_sum([2, 4, 6, 8])
    assert p == [2, 6, 12, 20]
    assert range_sum(p, 0, 1) == 6
    assert range_sum(p, 1, 3) == 18
    assert range_sum(p, 2, 2) == 6

    

