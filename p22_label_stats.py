def label_counts(lables):
    result = {}
    for i in lables:
        try: 
            result[i] += 1
        except:
            result[i] = 1
    return result

def label_distribution(lables):
    result = label_counts(lables)
    for i in result.keys():
        result[i] /= len(lables)
    return result

if __name__ == "__main__":
    assert label_counts([0, 1, 1, 2]) == {0: 1, 1: 2, 2: 1}
    assert label_distribution([0, 1, 1, 2]) == {0: 0.25, 1: 0.5, 2: 0.25}
    assert label_distribution([]) == {}
            
