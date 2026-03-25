# Write a Python program to perform matrix multiplication manually (without using NumPy dot).
import numpy as np
mat1=np.arange(1,10).reshape(3,3)
mat2=np.arange(1,13).reshape(3,4)
row1,colum1=mat1.shape
row2,colum2=mat2.shape
ans=np.zeros((row1,colum2),int)
if(colum1!=row2):
    print("Not valid matrix for multiplication!")
else:   
    for i in range(row1):
        for j in range(colum2):
            for k in range(row2):
                ans[i][j] += mat1[i][k] * mat2[k][j]
    print(ans)

   