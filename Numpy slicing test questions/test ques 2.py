#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10
import numpy as np

# Create a 3x3 matrix with values ranging from 2 to 10
array = np.arange(2, 11)
matrix=array.reshape(3, 3)

print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix)

