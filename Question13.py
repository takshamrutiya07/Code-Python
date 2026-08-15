# Write a Python program to compute Z-transform of a given sequence () using the sympy library and verify it by computing its inverse transform.
import sympy as sp
n, z = sp.symbols('n z')
x = [1, 2, 3]
ans=0
for i in range(len(x)):
    ans += x[i] * z**(-i)
print("Z-Transform of x[n]:", ans)

