def bubble_sort(numbers):
    result = numbers.copy()
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if result[j] > result[j+1]: result[j], result[j+1] = result[j+1], result[j]
    return result

if __name__ == "__main__":
    data = [5, 1, 4, 2]
    assert bubble_sort(data) == [1, 2, 4, 5]
    assert data == [5, 1, 4, 2]
    assert bubble_sort([]) == []
    assert bubble_sort([3]) == [3]

