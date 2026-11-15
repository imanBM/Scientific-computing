from scipy.optimize import root_scalar

# Student side-hustle investment:
# Initial cost: -KES 25,000 (Month 0)
# Monthly net profits over 4 months: KES 7,000, 8,000, 8,500, 6,500
cash_flows = [-25000, 7000, 8000, 8500, 6500]

# Net Present Value (NPV) function
def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

# Derivative of NPV with respect to rate (needed for Newton-Raphson)
def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)

# Method 1: Newton-Raphson (uses slope/derivative)
newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.05,
    method="newton",
    xtol=1e-12
)

# Method 2: Secant method (estimates slope using two guesses, no derivative needed)
secant = root_scalar(
    npv,
    x0=0.02,
    x1=0.15,
    method="secant",
    xtol=1e-12
)

print(f"Monthly IRR using Newton-Raphson: {newton.root:.6%}")
print(f"Monthly IRR using Secant method:  {secant.root:.6%}")
print(f"NPV at Newton solution:           KES {npv(newton.root):.8f}")