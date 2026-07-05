def min_max_normalize(values):
    if not values:
        return []
    min_value = min(values)
    diff = max(values) - min(values)
    if diff != 0:
        result = [None for _ in values]
        for i in range(len(values)):
            result[i] = (values[i] - min_value)/diff
    else: 
        result = [0 for _ in values]
    return result

if __name__ == "__main__":
    min_max_normalize([10, 20, 30]) == [0.0, 0.5, 1.0]
    assert min_max_normalize([5, 5, 5]) == [0, 0, 0]
    assert min_max_normalize([]) == []