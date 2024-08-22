import random
import time

def generate_array(n):
    return [random.random() for _ in range(n)]

def dot_product(array1, array2):
    return sum(a * b for a, b in zip(array1, array2))

n = 500000000  # Size of the arrays

# Measure time to generate arrays
start = time.time()
array1 = generate_array(n)
array2 = generate_array(n)
time_to_generate = time.time() - start

# Measure time to calculate dot product
start = time.time()
result = dot_product(array1, array2)
time_to_dot_product = time.time() - start

# Report results
print(f"Dot Product: {result}")
print(f"Time to generate arrays: {time_to_generate} seconds")
print(f"Time to calculate dot product: {time_to_dot_product} seconds")


#----------------------------------------------------------------------------------#




