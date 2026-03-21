import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r'D:/Semester-3/Python Assignment/Lab11Image.png')
img1 = Image.open(r'D:/Semester-3/Python Assignment/Lab11Image.png')
img_arr = np.array(img)
img1_arr= np.array(img1)
a=img_arr+img1_arr
plt.imshow(a)
plt.show()
s=img_arr-img1_arr
print(s)
plt.imshow(s)
plt.show()

