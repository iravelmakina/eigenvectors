# Eigenvectors & Eigenvalues Program

This repository contains a set of tools and demonstrations related to eigenvalues, eigenvectors, PCA-based image compression, and cryptographic operations using matrix diagonalization.

---

## Part One: Eigenvalues and Eigenvectors Calculation

### Description
A Python module that computes the eigenvalues and eigenvectors of a square matrix using NumPy. It also verifies the equality \( A \cdot v = \lambda \cdot v \) for each eigenpair.

### Libraries Used
- NumPy

---

## Part Two: Image Compression Using PCA

### Description
A Jupyter Notebook demonstrating image compression through Principal Component Analysis (PCA). The process involves converting a color image to grayscale, applying PCA, and reconstructing the image using a reduced number of principal components.

### What is PCA?
Principal Component Analysis is a technique used to reduce the dimensionality of data while retaining the most important features. In image processing, PCA finds the eigenvectors of the covariance matrix of pixel values to extract dominant patterns, enabling efficient compression and reconstruction.

### Steps Covered
1. Display the original image and its dimensions.
2. Convert the image to grayscale and analyze its shape.
3. Apply PCA to extract the most significant components.
4. Visualize explained variance and determine component count for optimal compression.
5. Reconstruct the image using various numbers of principal components and visualize the results.

### Libraries Used
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Part Three: Cryptography Using Diagonalization

### Description
This module demonstrates encryption and decryption of messages using matrix diagonalization. A key matrix is used to encrypt a text message, and its inverse is used to decrypt it.

### Features
- Encrypt a message by diagonalizing the key matrix and applying it to a message vector.
- Decrypt the encrypted message using inverse diagonalization.
- Display the original, encrypted, and decrypted messages for verification.

### Libraries Used
- NumPy

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/iravelmakina/eigenvectors.git
   cd eigenvectors
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Navigate to `src/` to run Python modules or open `notebooks/part_two.ipynb` for the PCA visualization.

---

## Dependencies
- Python 3.x
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## License
This project is open-source under the **MIT License**.

## Contributors
- [@iravelmakina](https://github.com/iravelmakina)
