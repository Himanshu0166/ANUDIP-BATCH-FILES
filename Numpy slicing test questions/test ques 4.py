#Write a NumPy program to convert a list and tuple into arrays.
import numpy as np

# Given list and tuple
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

# Convert the list to a array
array_from_list = np.array(my_list)
print("List to Array:")
print(array_from_list)

# Convert the tuple to a array
array_from_tuple = np.array(my_tuple)
print("Tuple to Array:")
print(array_from_tuple)
