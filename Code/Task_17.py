import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Newton's Law of Cooling for a mug of hot tea in a hostel room:
# Room temperature = 22.0 C, Cooling constant k = 0.08 per minute, Initial tea temp = 92.0 C
room_temp = 22.0
k = 0.08
T0 = 92.0

def cooling_rate(t, T):
    return -k * (T - room_temp)

# Method 1: Manual Euler's Method (step size dt = 2.0 minutes over 40 minutes)
dt = 2.0
t_euler = np.arange(0, 40 + dt, dt)
T_euler = np.zeros_like(t_euler)
T_euler[0] = T0

for i in range(len(t_euler) - 1):
    T_euler[i + 1] = T_euler[i] + dt * cooling_rate(t_euler[i], T_euler[i])

# Method 2: SciPy Runge-Kutta solver (solve_ivp)
sol = solve_ivp(cooling_rate, (0, 40), [T0], t_eval=t_euler)

# Exact analytical solution for comparison
T_exact = room_temp + (T0 - room_temp) * np.exp(-k * t_euler)

print(f"Temp after 10 mins -> Euler: {T_euler[5]:.2f} C | solve_ivp: {sol.y[0][5]:.2f} C | Exact: {T_exact[5]:.2f} C")
print(f"Temp after 40 mins -> Euler: {T_euler[-1]:.2f} C | solve_ivp: {sol.y[0][-1]:.2f} C | Exact: {T_exact[-1]:.2f} C")

plt.plot(t_euler, T_exact, "k-", label="Exact solution")
plt.plot(t_euler, sol.y[0], "bo", label="solve_ivp (RK45)")
plt.plot(t_euler, T_euler, "r--", label="Euler method (dt=2 min)")
plt.axhline(55.0, color="green", linestyle=":", label="Ideal drinking temp (55°C)")
plt.xlabel("Time (minutes)")
plt.ylabel("Tea Temperature (°C)")
plt.title("Hostel Tea Cooling Curve (Euler vs. solve_ivp)")
plt.legend()
plt.grid(True)
plt.show()