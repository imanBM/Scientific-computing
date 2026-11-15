import numpy as np

# Buying three snacks/items costing KES 10.10, 20.20, and 30.30
spent = 10.10 + 20.20 + 30.30
budget_limit = 60.60

print("Calculated total spent:", spent)
print("Exact equality check (spent == budget_limit):", spent == budget_limit)
print("Tolerance check (np.isclose):", np.isclose(spent, budget_limit))

# Absolute and relative error when rounding a split bill
# Splitting a KES 1,000 hostel utility bill equally among 3 roommates
exact_share = 1000.0 / 3.0
rounded_share = 333.33  # What each roommate actually pays in cash/M-Pesa

abs_error = abs(exact_share - rounded_share)
rel_error = abs_error / abs(exact_share)

print(f"\nExact bill share: KES {exact_share:.6f}")
print(f"Absolute rounding error per person: KES {abs_error:.6f}")
print(f"Relative error: {rel_error:.6%}")