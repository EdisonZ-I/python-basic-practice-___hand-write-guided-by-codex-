def matrix_shape(matrix):
    if not matrix: return (0, 0)
    else: return (len(matrix), len(matrix[0]))

def is_rectangular(matrix):
    if matrix:
        num = len( matrix[0] )
        for i in matrix:
            if len( i ) != num: return False
    return True

if __name__ == "__main__":
    assert matrix_shape([[1, 2], [3, 4]]) == (2, 2)
    assert matrix_shape([]) == (0, 0)
    assert is_rectangular([[1, 2], [3, 4]]) is True
    assert is_rectangular([[1], [2, 3]]) is False

