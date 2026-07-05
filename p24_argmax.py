def argmax(values):
    max_value = values[0]
    place = 0
    for i in range(len(values)):
        if max_value < values[i]:
            max_value = values[i]
            place = i
    return place

def predict_classes(logits):
    result = [None for _ in logits]
    for i in range(len(logits)):
        result[i] = argmax(logits[i])
    return result

if __name__ == "__main__":
    assert argmax([0.1, 0.7, 0.2]) == 1
    assert argmax([5, 5, 1]) == 0
    assert predict_classes([[0.1, 0.7], [3, 2], [1, 4]]) == [1, 0, 1]


