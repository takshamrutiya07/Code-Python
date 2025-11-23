# import sympy as sp
# n, z, w = sp.symbols('n z w', real=True)
# x_n = sp.cos(w*n)
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# sp.pprint(sp.simplify(X_z), use_unicode=True)


# import numpy as np
# x = [1, 2, 3, 4]
# h = [1, 0, -1]
# N = max(len(x), len(h))
# x_padded = np.pad(x, (0, N - len(x)), mode='constant')
# h_padded = np.pad(h, (0, N - len(h)), mode='constant')
# X_fft = np.fft.fft(x_padded)
# H_fft = np.fft.fft(h_padded)
# circular_conv = np.fft.ifft(X_fft * H_fft)
# circular_conv = np.real(circular_conv)
# print("Circular Convolution: ", circular_conv)


import numpy as np
import matplotlib.pyplot as plt
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 4, 5, 6])
# cross_corr = np.correlate(x, y, mode='full')
# plt.stem(cross_corr)
# plt.title('Cross-Correlation')
# plt.show()

# x = np.array([1, 2, 3, 4, 5])
# auto_corr = np.correlate(x, x, mode='full')
# plt.stem(auto_corr)
# plt.title('Autocorrelation')
# plt.show()

# import numpy as np
# import soundfile as sf
# from scipy import signal
# import matplotlib.pyplot as plt
# y, fs = sf.read("audio.wav")
# h, _ = sf.read("impulse.wav")
# y = y.flatten()
# h = h.flatten()

# linear_conv = signal.convolve(y, h, mode='full')
# N = len(y)
# circular_conv = np.fft.ifft(np.fft.fft(y, N) * np.fft.fft(h, N)).real

# plt.figure(figsize=(10,6))
# plt.subplot(2,1,1)
# plt.title("Linear Convolution")
# plt.plot(linear_conv)

# plt.subplot(2,1,2)
# plt.title("Circular Convolution")
# plt.plot(circular_conv)

# plt.tight_layout()
# plt.show()

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
def load_audio(path):
    audio, fs = sf.read(path)
    return audio.flatten(), fs
clean, fs = load_audio("clean_audio.wav")
noisy, _ = load_audio("noisy_audio.wav")
periodic, _ = load_audio("periodic_audio.wav")
auto_clean = np.correlate(clean, clean, mode='full')
auto_noisy = np.correlate(noisy, noisy, mode='full')
auto_periodic = np.correlate(periodic, periodic, mode='full')
cross_clean_noisy = np.correlate(clean, noisy, mode='full')
cross_clean_periodic = np.correlate(clean, periodic, mode='full')

plt.figure(figsize=(12, 10))
plt.subplot(3, 2, 1)
plt.title("Autocorrelation (Clean)")
plt.stem(auto_clean)
plt.subplot(3, 2, 2)
plt.title("Autocorrelation (Noisy)")
plt.stem(auto_noisy)
plt.subplot(3, 2, 3)
plt.title("Autocorrelation (Periodic)")
plt.stem(auto_periodic)
plt.subplot(3, 2, 4)
plt.title("Cross-Correlation: Clean vs Noisy")
plt.stem(cross_clean_noisy)
plt.subplot(3, 2, 5)
plt.title("Cross-Correlation: Clean vs Periodic")
plt.stem(cross_clean_periodic)
plt.tight_layout()
plt.show()

