import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Campus Smocha Stall Supply-Demand Cycle (Lotka-Volterra System)
# x = Smocha stock prepared (in dozens)
# y = Active student buyers visiting the stall (in tens)
#
# dx/dt = a*x - b*x*y   (vendor prep/restocking rate minus student buying rate)
# dy/dt = d*x*y - c*y   (new students attracted by fresh smocha minus students leaving when sold out)

a, b, c, d = 1.1, 0.4, 0.8, 0.2

def stall_dynamics(t, state):
    x, y = state
    dx_dt = a * x - b * x * y
    dy_dt = d * x * y - c * y
    return [dx_dt, dy_dt]

t_eval = np.linspace(0, 20, 400)
# Initial state: 5 dozen smochas ready, 20 students (2.0 tens) around
sol = solve_ivp(stall_dynamics, (0, 20), [5.0, 2.0], t_eval=t_eval)

smochas, buyers = sol.y

print(f"Peak smocha stock:  {np.max(smochas):.2f} dozen")
print(f"Lowest smocha stock:{np.min(smochas):.2f} dozen")
print(f"Peak student crowd: {np.max(buyers) * 10:.1f} students")

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].plot(sol.t, smochas, label="Smocha stock (dozens)")
axes[0].plot(sol.t, buyers, label="Student crowd (tens)")
axes[0].set_xlabel("Time (hours)")
axes[0].set_ylabel("Quantity")
axes[0].set_title("Smocha Supply & Crowd Cycles Over Time")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(smochas, buyers, color="purple")
axes[1].set_xlabel("Smocha Stock (dozens)")
axes[1].set_ylabel("Student Crowd (tens)")
axes[1].set_title("Phase Portrait (Closed Cycle)")
axes[1].grid(True)

plt.tight_layout()
plt.show()