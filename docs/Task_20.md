import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo Simulation: Student Weekly Upkeep Budget (10,000 simulated weeks)
rng = np.random.default_rng(42)
num_simulations = 10_000
weekly_allowance = 3500.0  # KES 3,500 pocket money per week

# Simulate random weekly expenses across 10,000 weeks:
# 1. Meals/Cafeteria: Normal distribution (mean KES 1,600, std dev KES 250)
food_cost = rng.normal(loc=1600.0, scale=250.0, size=num_simulations)

# 2. Matatu/Transport: Uniform distribution between KES 400 and KES 900
transport_cost = rng.uniform(low=400.0, high=900.0, size=num_simulations)

# 3. Airtime, Bundles & Printing: Normal distribution (mean KES 600, std dev KES 150)
data_print_cost = rng.normal(loc=600.0, scale=150.0, size=num_simulations)

# 4. Unexpected emergency cost (30% chance of spending an extra KES 1,000)
unexpected_cost = rng.choice([0.0, 1000.0], size=num_simulations, p=[0.7, 0.3])

total_weekly_spend = food_cost + transport_cost + data_print_cost + unexpected_cost
remaining_cash = weekly_allowance - total_weekly_spend

avg_spend = np.mean(total_weekly_spend)
prob_broke = np.mean(total_weekly_spend > weekly_allowance) * 100
percentile_95 = np.percentile(total_weekly_spend, 95)

print(f"Weekly Allowance:           KES {weekly_allowance:.2f}")
print(f"Average Weekly Spend:       KES {avg_spend:.2f}")
print(f"95th Percentile Spend:      KES {percentile_95:.2f}")
print(f"Risk of going broke (>3500): {prob_broke:.2f}% of weeks")

plt.hist(total_weekly_spend, bins=40, color="skyblue", edgecolor="black", alpha=0.8)
plt.axvline(weekly_allowance, color="red", linestyle="--", linewidth=2, label=f"Allowance Limit (KES {weekly_allowance:.0f})")
plt.axvline(avg_spend, color="green", linestyle="-", linewidth=2, label=f"Average Spend (KES {avg_spend:.0f})")
plt.xlabel("Total Weekly Spending (KES)")
plt.ylabel("Number of Simulated Weeks")
plt.title("Monte Carlo Simulation: Student Weekly Spending (10,000 Runs)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()