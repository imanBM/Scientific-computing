import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Break-even model for a campus movie night event:
# Ticket price = KES 150 per student
# Fixed venue/equipment cost = KES 4,000 + nonlinear crowd-control cost
# Profit(n) = 150*n - (4000 + 2500 * exp(n / 100))
# We want Profit(n) = 0 (break-even ticket count)

def profit(n):
    return 150 * n - (4000 + 2500 * np.exp(n / 100.0))

# Method 1: Bisection method (bracketing between 30 and 100 tickets)
bisect_sol = root_scalar(
    profit,
    bracket=[30, 100],
    method="bisect",
    xtol=1e-10
)

# Method 2: Fixed-point iteration rewritten as n = g(n)
# Rearranging 150*n = 4000 + 2500*exp(n/100)  =>  n = (4000 + 2500*exp(n/100)) / 150
def g(n):
    return (4000 + 2500 * np.exp(n / 100.0)) / 150.0

n_curr = 40.0
history = [n_curr]
for _ in range(100):
    n_next = g(n_curr)
    history.append(n_next)
    if abs(n_next - n_curr) < 1e-10:
        break
    n_curr = n_next

print(f"Bisection break-even tickets: {bisect_sol.root:.4f} (~{np.ceil(bisect_sol.root):.0f} tickets)")
print(f"Fixed-point break-even tickets: {history[-1]:.4f}")
print("Fixed-point iterations needed:", len(history) - 1)

tickets = np.linspace(20, 110, 300)
plt.plot(tickets, profit(tickets), label="Net Profit (KES)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(bisect_sol.root, color="red", linestyle="--", label=f"Break-even ({bisect_sol.root:.1f} tickets)")
plt.xlabel("Number of Tickets Sold")
plt.ylabel("Net Profit / Loss (KES)")
plt.title("Campus Movie Night Break-Even Analysis")
plt.legend()
plt.grid(True)
plt.show()