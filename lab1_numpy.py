import numpy as np
import time

def generate_array(n):
    return np.random.random(n)

n = 1000000  # Size of the arrays

# Measure time to generate arrays
start = time.time()
array1 = generate_array(n)
array2 = generate_array(n)
time_to_generate = time.time() - start

# Measure time to calculate dot product
start = time.time()
result = np.dot(array1, array2)
time_to_dot_product = time.time() - start

# Report results
print(f"Dot Product: {result}")
print(f"Time to generate arrays: {time_to_generate} seconds")
print(f"Time to calculate dot product: {time_to_dot_product} seconds")
