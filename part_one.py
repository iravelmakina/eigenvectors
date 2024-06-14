import numpy as np


def is_square_matrix(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Matrix is not square")
        return False
    return True


def find_eigenvalues_eigenvectors(matrix):
    if not is_square_matrix(matrix):
        return

    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors
