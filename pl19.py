# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import TransferFunction, lti, tf2zpk, bode   # FIXED import

# def analyze_z_transfer_function(num, den):
#     system = TransferFunction(num, den)

#     # FIX: TransferFunction does NOT have .zeros/.poles → use tf2zpk
#     zeros, poles, gain = tf2zpk(num, den)

#     print("Zeros:", zeros)
#     print("Poles:", poles)

#     # FIX: stability condition (your original kept)
#     stable = all(np.abs(pole) < 1 for pole in poles)
#     print("Stability:", "Stable" if stable else "Unstable")
#     causal = True
#     print("Causality:", "Causal" if causal else "Non-Causal")

#     time_invariant = True
#     print("Time Invariance:", "Time Invariant" if time_invariant else "Time Variant")
#     w, mag, phase = bode(system)

#     plt.figure(figsize=(12, 8))

#     plt.subplot(2, 1, 1)
#     plt.semilogx(w, mag)
#     plt.title('Bode Magnitude Plot')
#     plt.xlabel('Frequency [rad/s]')
#     plt.ylabel('Magnitude [dB]')
#     plt.grid()

#     plt.subplot(2, 1, 2)
#     plt.semilogx(w, phase)
#     plt.title('Bode Phase Plot')
#     plt.xlabel('Frequency [rad/s]')
#     plt.ylabel('Phase [degrees]')
#     plt.grid()
#     plt.tight_layout()
#     plt.show()
# num = [1, 0.5]
# den = [1, -1.5, 0.5]
# analyze_z_transfer_function(num, den)


# import sympy as sp
# n, z = sp.symbols('n z')
# X = sp.summation(z**(-n), (n, 0, sp.oo))

# print("Z-transform of u[n]:")
# print(X)
# print("\nSystem Stability:")
# print("Unstable")

import numpy as np
zeros = np.array([0.7, 0.9])
poles = np.array([0.6, 0.4])

print("Zeros:", zeros)
print("Poles:", poles)
stable = np.all(np.abs(poles) < 1)
print("\nStability:")
print("Stable" if stable else "Unstable")

