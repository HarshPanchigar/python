import numpy as np

matrix = np.array([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
])

arr = matrix.ravel()

print("Original Matrix:")
print(matrix)

print("\nOne-Dimensional Array:")
print(arr,"\n\n")

for i in matrix:
    print(i)