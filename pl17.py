# # Example 1:
import sympy as sp
# n, z, a = sp.symbols('n z a')
# x_n = a**n
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# print("Z-transform of x[n] = a^n u[n]:")
# sp.pprint(X_z, use_unicode=True)

# # Example 2:
# n, z, a = sp.symbols('n z a')
# x_n = 2**n
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# print("Z-transform of x[n] = a^n u[n]:")
# sp.pprint(X_z, use_unicode=True)

# import sympy as sp
# n, z = sp.symbols('n z')
# u_n = 1
# U_z = sp.summation(u_n * z**(-n), (n, 0, sp.oo))
# print("Z-transform of the unit step signal u[n]:")
# sp.pprint(U_z, use_unicode=True)


# import sympy as sp
# n, z, alpha = sp.symbols('n z alpha')
# x_n = sp.exp(alpha * n)
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# print("Z-transform of x[n] = exp(alpha * n) u[n]:")
# sp.pprint(X_z, use_unicode=True)

# import sympy as sp
# n, z = sp.symbols('n z')
# x_n = [1, 2, 3]
# X_z = sum(x_n[i] * z**(-i) for i in range(len(x_n)))
# print("Z-transform of the finite sequence {1, 2, 3}:")
# sp.pprint(X_z, use_unicode=True)


# import sympy as sp
# n, z, omega = sp.symbols('n z omega')
# x_n = sp.sin(omega * n)
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# print("Z-transform of x[n] = sin(omega * n) u[n]:")
# sp.pprint(X_z, use_unicode=True)

# import sympy as sp
# n, z = sp.symbols('n z')
# x_n = 3**n
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

# print("Z-transform of x[n] = 3^n u[n]:")
# sp.pprint(sp.simplify(X_z), use_unicode=True)

import sympy as sp
n, z, w = sp.symbols('n z w', real=True)
x_n = sp.cos(w*n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

sp.pprint(sp.simplify(X_z), use_unicode=True)


