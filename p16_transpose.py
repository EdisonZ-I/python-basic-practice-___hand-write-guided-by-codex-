def transpose(matrix):
    temp = []
    result = []
    if matrix:
        for i in range(len(matrix[0])):
            for j in matrix:
                temp.append( j[i] )
            result.append(temp)
            temp=[]
    return result

if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(m) == [[1, 4], [2, 5], [3, 6]]
    assert m == [[1, 2, 3], [4, 5, 6]]
    assert transpose([]) == []
