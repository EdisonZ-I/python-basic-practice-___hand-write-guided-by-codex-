def one_hot(labels, num_classes):
    result = []
    for i in labels:
        temp = [0 for _ in range(num_classes)]
        temp[i] = 1
        result.append(temp)
    return result

if __name__ == "__main__":
    assert one_hot([2, 0, 1], 3) == [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    assert one_hot([], 3) == []
