import numpy as np

from objects import key_matrix
from objects import message


# Function to encrypt message
def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector


# Function to decrypt message
def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    inv_diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(1 / eigenvalues)), np.linalg.inv(eigenvectors))
    decrypted_vector = np.dot(inv_diagonalized_key_matrix, encrypted_vector)
    decrypted_message = ''.join([chr(int(np.round(num.real))) for num in decrypted_vector])
    return decrypted_message


# Output
print(f"Key matrix: ")
for row in key_matrix:
    print(row)
print()

encrypted_message = encrypt_message(message, key_matrix)
print(f"Encrypted message: \n{encrypted_message}")
print()

decrypted_message = decrypt_message(encrypted_message, key_matrix)
print(f"Decrypted message: {decrypted_message}")
