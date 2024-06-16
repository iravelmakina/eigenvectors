import numpy as np

message = "чіназес!"
key_matrix = np.random.randint(0, 256, (len(message), len(message)))


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


# Check
print("Original message:", message)
encrypted_message = encrypt_message(message, key_matrix)
print("Encrypted message:")
print(encrypted_message)
decrypted_message = decrypt_message(encrypted_message, key_matrix)
print("Decrypted message: ", decrypted_message)
