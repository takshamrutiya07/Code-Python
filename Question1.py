# Write a Python program to create a 6×6 NumPy matrix and extract all prime numbers, then calculate their sum.
def isPrime(n):
    if(n==0 or n==1):
        return -1
    for i in range(2,n):
        if(n%i == 0):
            return 0
    return n
import numpy as np
matrix = np.arange(36).reshape(6,6)
print(matrix)
sum = 0
for i in range(6):
    for j in range(6):
        if(isPrime(matrix[i][j])):
            # print(matrix[i][j])
            sum = sum+matrix[i][j]
print(f"Sum of Prime numbers of 6x6 matrix is:{sum}")


            
