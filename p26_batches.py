from math import ceil


def make_batches(items, batch_size):
    if batch_size <= 0:
        return None
    result = []
    for i in range(ceil(len(items)/batch_size)):
        result.append(items[i*batch_size:(i+1)*batch_size])
    return result

if __name__ == "__main__":
    assert make_batches([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert make_batches([1, 2, 3], 3) == [[1, 2, 3]]
    assert make_batches([], 2) == []
    assert make_batches([1, 2], 0) is None

