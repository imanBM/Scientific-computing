import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Phone battery percentage checked every 2 hours from 8:00 AM to 8:00 PM (20:00)
hours = np.array([8, 10, 12, 14, 16, 18, 20], dtype=float)
battery_pct = np.array([100.0, 88.0, 74.0, 52.0, 41.0, 25.0, 12.0])

# Build linear and cubic spline interpolation functions
linear_interp = interp1d(hours, battery_pct, kind="linear")
cubic_interp = CubicSpline(hours, battery_pct)

# Estimate battery level every 15 minutes (0.25 hours)
quarter_hours = np.arange(8, 20 + 0.25, 0.25)
linear_est = linear_interp(quarter_hours)
cubic_est = cubic_interp(quarter_hours)

# Check estimated battery at 1:30 PM (13.5) during afternoon lectures
target_time = 13.5
print(f"Linear battery estimate at 1:30 PM: {float(linear_interp(target_time)):.2f}%")
print(f"Cubic battery estimate at 1:30 PM:  {float(cubic_interp(target_time)):.2f}%")

plt.scatter(hours, battery_pct, color="black", zorder=5, label="Actual battery checks")
plt.plot(quarter_hours, linear_est, linestyle="--", label="Linear interpolation")
plt.plot(quarter_hours, cubic_est, label="Cubic spline interpolation")
plt.xlabel("Hour of Day (24-hr)")
plt.ylabel("Battery Percentage (%)")
plt.title("Student Phone Battery Drain Interpolation")
plt.legend()
plt.grid(True)
plt.show()