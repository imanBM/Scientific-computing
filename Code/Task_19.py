import numpy as np
from scipy.optimize import minimize

# Student side hustle optimization:
# x = batches of printed study guides produced per week
# y = custom phone cases designed per week
#
# Profit function has diminishing returns due to marketing/effort:
# Profit(x, y) = 450*x - 15*x^2 + 600*y - 20*y^2
# Since scipy.optimize.minimize finds a MINIMUM, we minimize -Profit(x, y)

def negative_profit(vars):
    x, y = vars
    profit = (450 * x - 15 * x**2) + (600 * y - 20 * y**2)
    return -profit

# Constraints:
# 1. Material budget: KES 300 per guide batch + KES 500 per phone case <= KES 6,000
# 2. Time limit: 1.0 hr per guide batch + 1.5 hrs per phone case <= 15 hours
constraints = [
    {"type": "ineq", "fun": lambda v: 6000.0 - (300.0 * v[0] + 500.0 * v[1])},
    {"type": "ineq", "fun": lambda v: 15.0 - (1.0 * v[0] + 1.5 * v[1])}
]

# Quantities cannot be negative
bounds = [(0, None), (0, None)]

# Solve unconstrained first (unlimited money & time)
unconstrained = minimize(negative_profit, x0=[1.0, 1.0])

# Solve constrained (with real budget & time limits)
constrained = minimize(
    negative_profit,
    x0=[2.0, 2.0],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

print("--- Unconstrained Optimum (Unlimited Time & Capital) ---")
print(f"Optimal batches [guides, cases]: {np.round(unconstrained.x, 2)}")
print(f"Max possible weekly profit:      KES {-unconstrained.fun:.2f}")

print("\n--- Constrained Optimum (KES 6,000 Budget & 15 Hrs/Week) ---")
print(f"Optimal batches [guides, cases]: {np.round(constrained.x, 2)}")
print(f"Max realistic weekly profit:     KES {-constrained.fun:.2f}")