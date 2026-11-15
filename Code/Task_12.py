import numpy as np
from scipy.optimize import root

# Campus print shop equilibrium during final-year project submission week:
# p = price per bound booklet (in hundreds of KES, e.g., 2.0 = KES 200)
# q = daily quantity of booklets (in tens, e.g., 5.0 = 50 booklets)
#
# Nonlinear Demand curve: q = 12 - 0.5 * p^2  =>  q + 0.5 * p^2 - 12 = 0
# Nonlinear Supply curve: q = 1 + 0.8 * p^2   =>  q - 0.8 * p^2 - 1 = 0

def market_equations(z):
    p, q = z
    return [
        q + 0.5 * (p**2) - 12.0,
        q - 0.8 * (p**2) - 1.0
    ]

# Solve from a positive initial guess [price, quantity]
solution = root(market_equations, [2.0, 5.0])
p_eq, q_eq = solution.x

print("Solver converged:", solution.success)
print(f"Equilibrium price per booklet: KES {p_eq * 100:.2f}")
print(f"Equilibrium daily booklets:    {q_eq * 10:.1f} booklets")
print("Residuals (should be ~0):     ", np.round(market_equations(solution.x), 10))