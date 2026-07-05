def accuracy(predictions, labels):
    if len(predictions) != len(labels):
        return None
    else:
        count = 0
        ttl = len(predictions)
        for i in range(ttl):
            if predictions[i] == labels[i]:
                count += 1
        try:
            return count/ttl
        except:
            return 0
        
if __name__ == "__main__":
    assert accuracy([1, 0, 1], [1, 1, 1]) == 2 / 3
    assert accuracy([], []) == 0
    assert accuracy([1], [1, 0]) is None


