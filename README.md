# Eigenvectors & Eigenvalues program

This repository contains solutions for lab tasks focusing on eigenvalues, eigenvectors, image compression using PCA, and cryptography using diagonalization.

## Part One: Eigenvalues and Eigenvectors Calculation

### Task Description
Write a function that takes a square matrix and returns its eigenvalues and eigenvectors using the NumPy library. Additionally, verify the equality A v = λ v for each eigenvalue and corresponding eigenvector.

### Recommended Libraries
- NumPy

### Useful Resources
- [Video on Eigenvalues and Eigenvectors](#)

## Part Two: Image Compression Using PCA

### Task Description
Implement a function to reduce image dimensionality using Principal Component Analysis (PCA).

### Recommended Libraries
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

### Useful Resources
- [Introduction to PCA](#)
- [Forum Discussion on PCA](#)

### What is PCA?
Principal Component Analysis (PCA) is a technique used in image processing to reduce its dimensionality. PCA identifies the principal components of an image by finding the eigenvectors of the covariance matrix of pixel values. These eigenvectors represent the most important features or patterns in the image.

By reducing the dimensionality of image data using PCA, it becomes easier to compress and store images, as well as perform operations such as image recognition and classification.

### Task Steps
1. **Display the Initial Color Image:**
   - Show the original color image and a vector containing its dimensions in pixels and the number of primary color channels used.

2. **Convert Image to Black and White:**
   - Transform the image to black and white, then display its size and the number of color channels (0.25 points).

3. **Apply PCA:**
   - Apply PCA to the black-and-white image matrix. Display the cumulative variance and determine the number of components needed to cover 95% of the variance. Use library functions (NumPy recommended) (0.75 points).
   - Display a plot of the process (0.5 points).

4. **Reconstruct Black and White Image:**
   - Reconstruct the black-and-white image using the limited number of components found in the previous step. Display the resulting image. For 95% coverage, a clearer image is expected, maintaining essential elements but possibly lacking fine details (1 point).

5. **Reconstruct Image with Different Number of Components:**
   - Reconstruct the image with various numbers of components and display the results. Try using more components and display the corresponding result. Check if a clearer image is obtained, and compare it with using fewer components (2 points).

## Part Three: Cryptography Using Diagonalization

### Task Description
Use diagonalization to decrypt codes. It is recommended to use the NumPy library.

### Recommended Libraries
- NumPy

### Useful Resources
- [Introduction to Linear Algebra in Cryptography](#)
- [Video on Cryptography](#)

### Task Steps
1. **Create Decryption Function:**
   - Create a function `decrypt_message(encrypted_vector, key_matrix)` that decrypts an encrypted vector using the key matrix and the inverse diagonalization operation.

2. **Verify Function with Example:**
   - Test the developed functions with an example using a randomly generated key matrix and a text message.

### Example Execution
- **Original Message:** Hello, World!
- **Encrypted Message:** [118703.+1.04957181e-11j 180926.+1.50897913e-11j 149312.+1.90968912e-11j 161873.+1.52982299e-11j 188078.+1.70487245e-12j 145036.+1.64536004e-11j 139370.+4.15241913e-11j 195037.+1.51003306e-11j 155629.+1.38144125e-11j 206859.+1.38439864e-11j 145588.+1.95891393e-11j 130163.+1.55598216e-11j 176423.+1.26512259e-11j]
- **Decrypted Message:** Hello, World!

## Usage Instructions
1. Clone the repository to your local machine.
2. Install the required libraries as specified.
3. Run the program according to the instructions provided in each part.

## Dependencies
- Python 3.x
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Contributors
- @iravelmakina
