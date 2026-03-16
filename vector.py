import numpy as np
b=np.arange(1,4)
c=np.arange(5,8)
d=np.arange(9,12)
a=np.array([b,c,d])
print(a)
l1= [a[1,0],a[1,1]]
l2=[a[2,0],a[2,1]]
print(np.array([l1,l2]))
f=np.ones([2,2],dtype=int)
f=2*f[0,]
print(f)