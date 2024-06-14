def is_square_matrix(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Matrix is not square")
        return False
    return True
