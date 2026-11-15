import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Fixed cost-sharing matrix among 3 roommates (Alex, Brian, Chris)
# Each row represents an expense rule (Rent split, Wi-Fi split, Power split)
A = np.array([
    [3.0, 1.0, 1.0],
    [1.0, 3.0, 1.0],
    [1.0, 1.0, 3.0]
])

# Monthly bill totals (in thousands of KES) for January, February, and March
monthly_bills = [
    np.array([15.0, 12.0, 13.0]),  # January
    np.array([16.0, 11.0, 13.0]),  # February
    np.array([14.0, 14.0, 12.0])   # March
]

# Factor matrix A only once using LU decomposition
lu, piv = lu_factor(A)

months = ["January", "February", "March"]
for month, b in zip(months, monthly_bills):
    shares = lu_solve((lu, piv), b)
    residual = b - A @ shares
    print(f"--- {month} ---")
    print("Individual shares (Alex, Brian, Chris) in '000 KES:", np.round(shares, 2))
    print("Residual norm:", np.linalg.norm(residual))