#Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
import numpy as np

# Create an array of 10 zeros
zeros = np.zeros(10, dtype=int)
print("Array of 10 zeros:", zeros)

# Create an array of 10 ones
ones = np.ones(10, dtype=int)
print("Array of 10 ones:", ones)

# Create an array of 10 fives
fives = np.full(10, 5, dtype=int)
print("Array of 10 fives:", fives)
