import numpy as np
import random


arbitrary_matrix = np.random.randint(0, 256, (lambda n=random.randint(1, 5): (n, n))())

image = 'assets/image.png'

message = 'чіназес!'
key_matrix = np.random.randint(0, 256, (len(message), len(message)))
