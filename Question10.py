# Write a Python program to generate and plot unit step, ramp, and exponential signals in the same graph using matplotlib with proper labeling and legends
import numpy as np
import matplotlib.pyplot as plt
n = np.arange(0, 10)
unit_step = np.where(n >= 0, 1, 0)        
ramp = n                                   
exponential = np.exp(0.4*n) 
plt.stem(n,unit_step,linefmt='b-',markerfmt='bo',basefmt=' ',label='Unit Step')
plt.stem(n, ramp,linefmt='g-',markerfmt='go',basefmt=' ',label='Ramp')
plt.stem(n, exponential,linefmt='r-',markerfmt='ro',basefmt=' ',label='Exponential')
plt.title('Unit Step, Ramp, and Exponential Signals')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
