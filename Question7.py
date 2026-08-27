# Write a Python program to compute the sum of each row and each column of a NumPy matrix
import numpy as np
matrix=np.arange(1,11).reshape(5,2)
print(matrix)
row,colum=matrix.shape
print("sum of rows:")
for i in range(row):
    print(sum(matrix[i]))
    
print("sum of colums")
for j in range(colum):
    print(sum(matrix[:,j]))