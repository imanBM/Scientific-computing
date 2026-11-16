# Task 15: Numerical Differentiation

## B. Input Values and Mathematical Operations
* **Input values:** A uniform time array `t` from `0` to `10` seconds (11 points) and a position array `s` representing distance traveled in meters (`[0.0, 1.2, 4.9, ..., 100.2]`).
* **Math performed:** Uses `np.gradient(s, t)` to compute the first numerical derivative (velocity `v = ds/dt`) via central differences for interior points and one-sided differences at the boundaries. It then applies `np.gradient(v, t)` a second time to get the second derivative (acceleration `a = dv/dt`), and plots all three curves vertically.

## C. Parameter Change and Impact
* **Change:** Increased the number of time samples from `11` points (`1.0 s` step size) to `101` points (`0.1 s` step size) over the same 10-second window.
* **Result:** Because the step size $h$ between readings is 10 times smaller, the truncation error shrinks drastically. The calculated velocity and acceleration curves become much smoother and sit much closer to the true calculus derivatives.

## D. Meaning of Output in Words and Graph Interpretation
* **Output:** The terminal prints arrays for time, distance, speed, and acceleration, turning raw position logs into rate-of-change numbers without needing an algebraic formula.
* **Graph:** The top plot shows total distance rising in a curve. The middle plot shows velocity rising steadily in a near-straight line (meaning speed increases over time), and the bottom plot shows acceleration staying roughly flat around `2 m/s²` (with slight wobble due to measurement noise).

## E. New Related Case: File Download Speed and Bandwidth Fluctuation
* **Scenario:** Measuring instantaneous download speed (`MB/s`) and bandwidth acceleration/drop-off (`MB/s²`) over 10 seconds while downloading a file on campus Wi-Fi, given only cumulative megabytes downloaded per second.
* **Assumptions:** 
  * Cumulative data downloaded is recorded every `1.0` second (`dt = 1.0`).
  * Network congestion causes download speed to dip around seconds `4–6` before recovering.
* **Output & Interpretation:** `np.gradient()` reveals that download speed peaks at `8.50 MB/s` near the end (`t = 10s`), while dipping to `4.15 MB/s` around `t = 5–6s`. The third subplot highlights negative acceleration (`-1.40 MB/s²` at `t = 4s`) right when network congestion hits, followed by positive acceleration as bandwidth frees up.