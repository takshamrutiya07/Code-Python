# Write a Python program to generate and plot unit impulse, cosine, and sine signals for . Mark the amplitude clearly on the plot.
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)
impulse = np.where(n == 0, 1, 0)
cosine = np.cos(0.2 * np.pi * n)
sine = np.sin(0.2 * np.pi * n)

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(n, impulse)
plt.title('Unit Impulse Signal δ[n]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.stem(n, cosine)
plt.title('Cosine Signal cos(0.2πn)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.stem(n, sine)
plt.title('Sine Signal sin(0.2πn)')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
