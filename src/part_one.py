import numpy as np
from src.objects import arbitrary_matrix


# Function to check if the given matrix is a square matrix
def is_square_matrix(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Matrix is not square.")
        return False
    return True


# Function to find the eigenvalues and eigenvectors of a given square matrix
def find_eigenvalues_eigenvectors(matrix):
    if not is_square_matrix(matrix):
        return

    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


# Function to check the equality A * v = λ * v for each eigenvalue and its corresponding eigenvector
def check_equality(matrix, eigenvalues, eigenvectors):
    for i in range(len(eigenvalues)):
        eigenvalue = eigenvalues[i]
        eigenvector = eigenvectors[:, i]
        left_side = np.dot(matrix, eigenvector)
        right_side = np.dot(eigenvalue, eigenvector)

        if np.allclose(left_side, right_side):  # Normalized eigenvectors are used because they have nice mathematical
            # properties and make computations easier
            print(
                f"Eigenvalue λ = {np.round(eigenvalue, 2)} and corresponding eigenvector "
                f"v = {np.round(eigenvector, 2)} satisfy equality A * v = λ * v")
        else:
            print(
                f"Equality A * v = λ * v does not hold for λ = {np.round(eigenvalue, 2)} and eigenvector "
                f"v = {np.round(eigenvector, 2)}")


# Output
print("Matrix: ")
for row in arbitrary_matrix:
    print(row)
print()

result = find_eigenvalues_eigenvectors(arbitrary_matrix)
if result:
    eigenvalues, eigenvectors = result
    for i in range(len(eigenvalues)):
        print(f"Eigenvalue {i + 1}: {eigenvalues[i]}")
        print(f"Eigenvector {i + 1}: {eigenvectors[:, i]}")
    print()

    check_equality(arbitrary_matrix, eigenvalues, eigenvectors)
