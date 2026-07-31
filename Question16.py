
# Write a Python program using NumPy to perform time-shifting and time-scaling operations on a discrete-time signal, then plot original and transformed signals.
import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)
x = np.sin(0.4 * np.pi * n)
shifted = np.sin(0.4 * np.pi * (n - 2))
scaled = np.sin(0.4 * np.pi * (0.5 * n))

plt.figure(figsize=(9, 5))
plt.stem(n, x, label='Original')
plt.stem(n, shifted, linefmt='r-', markerfmt='ro', basefmt='r-', label='Shifted (n-2)')
plt.stem(n, scaled, linefmt='g-', markerfmt='go', basefmt='g-', label='Scaled (0.5n)')

plt.legend()
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Time Shifting and Scaling')
plt.grid(True)
plt.show()
