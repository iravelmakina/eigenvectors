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


def check_equality(matrix, eigenvalues, eigenvectors):
    for i in range(len(eigenvalues)):
        eigenvalue = eigenvalues[i]
        eigenvector = eigenvectors[:, i]
        left_side = np.dot(matrix, eigenvector)
        right_side = np.dot(eigenvalue, eigenvector)

        if np.allclose(left_side, right_side): # normalized eigenvectors are used because they have nice mathematical properties and make computations easier
            print(
                f"Eigenvalue λ = {np.round(eigenvalue, 2)} and corresponding eigenvector v = {np.round(eigenvector, 2)} "
                f"satisfy equality A * v = λ * v")
        else:
            print(
                f"Equality A * v = λ * v does not hold for λ = {np.round(eigenvalue, 2)} and eigenvector v = {np.round(eigenvector, 2)}")
