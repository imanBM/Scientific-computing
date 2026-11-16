import numpy as np
import matplotlib.pyplot as plt

# Time in seconds (0 to 10s, every 1 second)
t = np.linspace(0, 10, 11)

# Cumulative data downloaded in Megabytes (MB) on campus Wi-Fi
# Starts fast, slows down slightly mid-way as more students connect, then picks up
downloaded_mb = np.array([0.0, 4.2, 9.8, 16.5, 22.0, 26.5, 30.2, 34.8, 41.0, 48.5, 57.0])

# First derivative: Instantaneous download speed (MB/s) using central differences
speed_mbs = np.gradient(downloaded_mb, t)

# Second derivative: Download speed change / acceleration (MB/s^2)
accel_mbs2 = np.gradient(speed_mbs, t)

print("Time (s):              ", t)
print("Downloaded (MB):       ", downloaded_mb)
print("Download Speed (MB/s): ", np.round(speed_mbs, 2))
print("Speed Change (MB/s^2): ", np.round(accel_mbs2, 2))

fig, axes = plt.subplots(3, 1, figsize=(7, 8), sharex=True)

axes[0].plot(t, downloaded_mb, marker="o")
axes[0].set_ylabel("Total Downloaded (MB)")
axes[0].set_title("File Download Progress, Speed, and Acceleration")
axes[0].grid(True)

axes[1].plot(t, speed_mbs, marker="s", color="orange")
axes[1].set_ylabel("Speed (MB/s)")
axes[1].grid(True)

axes[2].plot(t, accel_mbs2, marker="^", color="green")
axes[2].set_ylabel("Acceleration (MB/s²)")
axes[2].set_xlabel("Time (seconds)")
axes[2].grid(True)

plt.tight_layout()
plt.show()