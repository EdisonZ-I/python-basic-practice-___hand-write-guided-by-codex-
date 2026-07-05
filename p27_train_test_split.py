def train_test_split(items, test_ratio):
    num_test = int(len(items) * test_ratio)
    return (items[:len(items)-num_test], items[len(items)-num_test:])

if __name__ == "__main__":
    train, test = train_test_split([1, 2, 3, 4, 5], 0.4)
    assert train == [1, 2, 3]
    assert test == [4, 5]

    train, test = train_test_split([1, 2, 3], 0)
    assert train == [1, 2, 3]
    assert test == []
