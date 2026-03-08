import numpy as np
m=np.arange(0,15).reshape(3,5)#in this line we can't arrange all 15 elements in matrix.
#because 4*3=12 we can arrange only 12 elements in matrix.
#so that it will give ValueError.
#Ex:m=np.arange(0,15).reshape(3,4) Error:ValueError.
r=np.random.randint(3,3)
print(r)
print(m)