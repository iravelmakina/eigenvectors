import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from objects import image

# Load the image
image_raw = plt.imread(image)
print("Original image shape and color canals:", image_raw.shape)

# Display the original image
plt.imshow(image_raw)
plt.title("Original image")
plt.show()

# Convert the image to black and white
image_sum = image_raw.sum(axis=2)
image_bw = image_sum / image_sum.max()
print("Black-white image shape:", image_bw.shape)
print("Black-white image max value:", image_bw.max())

# Display the black-and-white image
plt.imshow(image_bw, cmap='gray')
plt.title("Black-white image")
plt.show()

# Flatten each row of the image
image_rows = image_bw.reshape(image_bw.shape[0], -1)
print("Image reshaped to rows shape:", image_rows.shape)

# Scale the data
scaler = StandardScaler()
image_rows_scaled = scaler.fit_transform(image_rows)
print("Scaled rows shape:", image_rows_scaled.shape)

# Apply PCA
pca = PCA()
pca.fit(image_rows_scaled)

# Cumulative variance
cumulative_variance = np.cumsum(pca.explained_variance_ratio_) * 100  # percent conversion
print("Cumulative variance:")
print(cumulative_variance)

# Number of components for 95% covering of variance
num_components = np.argmax(cumulative_variance >= 95) + 1
print(f'Number of components to cover 95% of the variance: {num_components}')

# Show the cumulative variance plot
plt.figure(figsize=(8, 6))
plt.plot(cumulative_variance, marker='o')
plt.axhline(y=95, color='r', linestyle='--')  # Add a horizontal line for 95% variance
plt.axvline(x=num_components, color='k', linestyle='--')  # Add a vertical line for the number of components
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance by PCA Components')
plt.grid(True)
plt.show()
