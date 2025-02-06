import numpy as np 
import pandas as pd 

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)

# Print the array, its size and its shape (what's the difference between size and shape?)
print("Array:", arr)
print("Shape:", arr.shape)  # Expect (5,)
print("Size:", arr.size)    # Number of elements 

# Create a 2D array
my_2d_list = [[1, 2, 3],
              [4, 5, 6]]
arr_2d = np.array(my_2d_list)

# Print the array and its shape
print("2D Array:\n", arr_2d)
print()
print("Shape:", arr_2d.shape)

# Create and print an array of zeros and an array of ones
zeros_arr = np.zeros((3, 4))
ones_arr = np.ones((2, 2))

print("Zeros:\n", zeros_arr)
print()
print("Ones:\n", ones_arr)

# Print the element at the second row, and third column of arr_2d
print("Element at second row, third column:", arr_2d[1, 2])
print()

# Print a slice of arr
print("Elements from index 1 to 3:", arr[1:4])

# Define arrays a and b
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Compute and print the sum of a, mean of b, and argmax of b
print("Sum of a:", a.sum()) # np.sum(a)
print("Mean of b:", b.mean())
print("Index of max element in b:", np.argmax(b))
print()

# Compute and print the square root of all the elements in a
arr_sqrt = np.sqrt(a)
print("Square roots of a:", arr_sqrt)

# Compute and print the dot product of a and b
dot_prod = np.dot(a, b)
print("Dot product of a and b:", dot_prod)
print()

# Normalize the vector b (what does linalg stand for?)
b_norm_val = np.linalg.norm(b)
b_normalized = b / b_norm_val
print("Normalized b with L2 norm:", b_normalized) 

# Use a seed to print the same randomly generated numbers multiple times
np.random.seed(42)
random_arr = np.random.rand(5)
print("Random array of 5 elements:", random_arr)

# Demonstrate speed of NumPy vs. Python lists
import time

# Create large Python list vs. NumPy array
size = 1000000
py_list = list(range(size))
np_arr = np.arange(size)

# Timing Python list multiplication
start_time = time.time()
py_result = [x * 2 for x in py_list]
py_time = time.time() - start_time

# Timing NumPy array multiplication
start_time = time.time()
np_result = np_arr * 2
np_time = time.time() - start_time

print(f"Python list time: {py_time:.6f} seconds")
print(f"NumPy array time: {np_time:.6f} seconds")
print()
print("NumPy is ~", round(py_time / np_time, 1), "times faster for this operation!")