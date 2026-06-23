'''
def find_index(items, target):
    place=-1
    for i in range(len(items)):
        if items[i] == target:
            place = i
            break
    return place'''

def find_index(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
    
def contains(items, target):
    return find_index(items, target) != -1

if __name__ == "__main__":
    assert find_index([5, 3, 7, 3], 3) == 1
    assert find_index([5, 3, 7], 9) == -1
    assert contains(["a", "b"], "b") is True
    assert contains(["a", "b"], "c") is False
