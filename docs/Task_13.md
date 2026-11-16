# Task 13: Interpolation

## B. Input Values and Mathematical Operations
* **Input values:** Two NumPy arrays containing 7 hourly timestamps (`[8, 9, 10, 11, 12, 13, 14]`) and their corresponding temperature readings (`[18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0]`), plus a target time of `10.5` (10:30 AM)[cite: 19, 20].
* **Math performed:** Builds two interpolation models using `scipy.interpolate`: `interp1d(..., kind="linear")` (connects adjacent points with straight lines) and `CubicSpline` (fits smooth cubic polynomials between points)[cite: 19]. It evaluates both functions at 10-minute intervals (`1/6` hour) and plots the curves alongside the raw points[cite: 20].

## C. Parameter Change and Impact
* **Change:** Changed `target_time` from `10.5` (10:30 AM) to `13.5` (1:30 PM), where the temperature peaks and starts dropping.
* **Result:** At `13.5`, linear interpolation gives `25.25°C` (strictly halfway between `25.5` and `25.0`), whereas the cubic spline predicts a slightly higher `25.41°C` because it curves smoothly over the afternoon peak instead of cutting a sharp corner.

## D. Meaning of Output in Words and Graph Interpretation
* **Output:** The terminal prints the estimated temperature at 10:30 AM using both methods (`23.25°C` linear vs. `23.31°C` cubic spline), showing how you can estimate missing readings between sensor logs[cite: 19, 20].
* **Graph:** The dots mark the actual hourly readings[cite: 20]. The linear curve connects dots with rigid straight segments (creating sharp corners at each hour), while the cubic spline draws a smooth, natural wave through every dot[cite: 19, 20].

## E. New Related Case: Student Phone Battery Drain Estimation
* **Scenario:** Estimating a student's phone battery percentage every 15 minutes throughout a 12-hour campus day (`8:00 AM` to `8:00 PM`) using only manual checks taken every two hours.
* **Assumptions:** 
  * Battery drops non-uniformly depending on usage (e.g., heavy data/hotspot use between `12:00 PM` and `2:00 PM`).
  * No charging occurs during the day.
* **Output & Interpretation:** At `1:30 PM` (`13.5`), linear interpolation estimates `57.50%` battery remaining, while the cubic spline estimates `57.16%`. The graph smoothly tracks the steep midday battery drop during lunch breaks and slower drain during evening classes.