def matrix_add(a, b):
    # test if same size
    if len(a) != len(b): return None
    for i in range( len(a) ):
        if ( len(a[0]) != len(a[i]) ) or ( len(a[0]) != len(b[i]) ): return None
    # add
    result = [[] for _ in range(len(a))]
    for i in range( len(a) ):
        for j in range( len(a[i])):
            result[i].append(a[i][j] + b[i][j])
    return result

if __name__ =="__main__":
    assert matrix_add([[1, 2], [3, 4]], [[10, 20], [30, 40]]) == [[11, 22], [33, 44]]
    assert matrix_add([[1, 2]], [[1], [2]]) is None
    assert matrix_add([], []) == []
