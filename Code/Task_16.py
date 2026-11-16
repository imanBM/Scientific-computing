import numpy as np
from scipy.integrate import trapezoid, simpson, quad

# Student evening internet data rate in MB per minute over a 60-minute study & YouTube session
# Rate fluctuates as student switches between reading PDFs and watching tutorial videos
def data_rate(t):
    return 12.0 + 6.0 * np.sin(np.pi * t / 30.0) + 0.05 * t

# Sample every 5 minutes (13 points from t=0 to t=60 minutes)
t = np.linspace(0, 60, 13)
rates = data_rate(t)

# Method 1: Trapezoidal rule on discrete samples
trap_mb = trapezoid(rates, t)

# Method 2: Simpson's rule on discrete samples
simp_mb = simpson(rates, x=t)

# Method 3: Exact adaptive quadrature on the continuous function
quad_mb, error_est = quad(data_rate, 0, 60)

print(f"Total Data (Trapezoidal rule): {trap_mb:.4f} MB")
print(f"Total Data (Simpson's rule):   {simp_mb:.4f} MB")
print(f"Total Data (Exact quad):       {quad_mb:.4f} MB")
print(f"Trapezoidal error vs quad:     {abs(trap_mb - quad_mb):.6f} MB")
print(f"Simpson's error vs quad:       {abs(simp_mb - quad_mb):.6f} MB")