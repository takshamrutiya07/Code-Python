# Write a Python program to rotate a 3×3 matrix by 90 degrees clockwise.
import numpy as np
matrix=np.arange(1,10).reshape(3,3)
# matrix[0],matrix[0:,]=matrix[0:,],matrix[0]
print(matrix)
neww=matrix.copy()
l1=matrix[0]# 1st row
l2=matrix[1]# 2nd row  
l3=matrix[2]# 3rd row
neww[:,-1]=l1#assiging the 1st row value to last column of new matrix
neww[:,-2]=l2#assiging the 2nd row value to second column of new matrix
neww[:,-3]=l3#assiging the 3rd row value to first column of new matrix
print(neww)

