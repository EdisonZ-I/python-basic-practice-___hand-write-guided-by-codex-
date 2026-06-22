def square_all(numbers):
    result=[]
    for i in numbers:
        result.append(i**2)
    return result

def filter_greater_than(numbers, threshhold):
    result=[]
    for i in numbers:
        if i > threshhold: result.append(i)
    return result

def reverse_list(items):
    result=[]
    for i in range(1,len(items)+1):
        result.append(items[-i])
    return result

if __name__ == "__main__":
    data = [1, 2, 3]
    assert square_all(data) == [1, 4, 9]
    assert data == [1, 2, 3]
    assert filter_greater_than([1, 5, 2, 8], 3) == [5, 8]
    assert reverse_list(["a", "b", "c"]) == ["c", "b", "a"]
    print('1')