def count_items(items):
    result={}
    for i in items:
        if i not in result.keys(): result[i]=1
        else: result[i] += 1
    return result

def most_frequent(items):
    if not items: return None
    else: 
        data=count_items(items)
        result=items[0]
        max_count=data[items[0]]
        for i in items:
            if data[i] > max_count:
                result = i
                max_count = data[i]
        return result

if __name__ == "__main__":
    assert count_items(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert most_frequent(["x", "y", "x", "z"]) == "x"
    assert most_frequent(["a", "b"]) == "a"
    assert most_frequent([]) is None