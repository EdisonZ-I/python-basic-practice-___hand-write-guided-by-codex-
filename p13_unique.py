def unique_keep_order(items):
    result = []
    for i in items:
        if i not in result: result.append(i)
    return result

if __name__ == "__main__":
    assert unique_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert unique_keep_order(["a", "b", "a"]) == ["a", "b"]
    assert unique_keep_order([]) == []
