import numpy as np

# x = number of Regular student tickets sold (KES 200 each)
# y = number of VIP student tickets sold (KES 500 each)
#
# Equation 1 (Total tickets): 1x + 1y = 150
# Equation 2 (Total revenue): 200x + 500y = 42000

A = np.array([
    [1.0, 1.0],
    [200.0, 500.0]
])
b = np.array([150.0, 42000.0])

# Solve Ax = b
solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Regular tickets sold: {solution[0]:.0f}")
print(f"VIP tickets sold: {solution[1]:.0f}")
print("Verification (A @ solution):", A @ solution)
print("Residual norm:", np.linalg.norm(residual))