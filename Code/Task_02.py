import numpy as np

# Daily mobile data usage in MB over 7 days
daily_mb = np.array([
    850.0, 1200.5, 640.0, 2100.0, 
    950.5, 1500.0, 1100.0
])

avg_usage = np.mean(daily_mb)
min_usage = np.min(daily_mb)
max_usage = np.max(daily_mb)

# Vectorized conversion from Megabytes (MB) to Gigabytes (GB)
daily_gb = daily_mb / 1024.0

print(f"Average daily usage: {avg_usage:.2f} MB")
print(f"Lowest usage day: {min_usage:.2f} MB")
print(f"Highest usage day: {max_usage:.2f} MB")
print("Daily usage in GB:", np.round(daily_gb, 2))