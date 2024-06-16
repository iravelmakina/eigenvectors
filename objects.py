import numpy as np

arbitrary_matrix = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

image = 'image.png'

message = "чіназес!"
key_matrix = np.random.randint(0, 256, (len(message), len(message)))
