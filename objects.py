import numpy as np
import random

n = random.randint(1, 10)
arbitrary_matrix = np.random.randint(0, 256, (n, n))

image = 'image.png'

message = "чіназес!"
key_matrix = np.random.randint(0, 256, (len(message), len(message)))
