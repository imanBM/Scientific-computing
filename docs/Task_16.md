# Task 16: Numerical Integration

## B. Input Values and Mathematical Operations
* **Input values:** A continuous power consumption function `power(t) = 50 + 15 * sin(pi * t / 12) + 0.8 * t`, a time array `t` spanning `0` to `24` hours (`25` hourly samples), and evaluated power readings `P = power(t)`.
* **Math performed:** Computes total energy (the area under the power curve over 24 hours) using three numerical integration methods from `scipy.integrate`:
  * `trapezoid(P, t)`: Approximates the area using straight-line trapezoids between adjacent hourly readings.
  * `simpson(P, x=t)`: Approximates the area using smooth parabolic arcs across triplets of points.
  * `quad(power, 0, 24)`: Uses adaptive Gaussian quadrature directly on the math function to find the virtually exact integral.

## C. Parameter Change and Impact
* **Change:** Increased the number of sample points in `np.linspace(0, 24, 25)` from `25` points (1-hour intervals) to `241` points (6-minute intervals).
* **Result:** With 10 times more slices, the Trapezoidal rule's error shrinks by roughly a factor of `100` (from `~0.11` down to `~0.0011`), matching the exact `quad` value (`1430.40 Wh`) to 3 decimal places. Simpson's rule becomes accurate to over 8 decimal places.

## D. Meaning of Output in Words
The output prints the total energy consumed over 24 hours (`1430.40 Wh`) calculated by all three methods, followed by the exact error of the Trapezoidal and Simpson methods compared to `quad`. It demonstrates that Simpson's rule is much more accurate than the Trapezoidal rule when working with curved sensor data at the exact same sample rate. No graph is generated for this task.

## E. New Related Case: Total Data Bundle Consumed During an Evening Session
* **Scenario:** Calculating the total mobile data (in Megabytes) consumed during a 60-minute evening study and video-tutorial session when download speed (`MB/min`) fluctuates smoothly over time.
* **Assumptions:** 
  * Speed is logged every `5` minutes (`13` samples across `60` minutes).
  * Speed follows `12.0 + 6.0 * sin(pi * t / 30) + 0.05 * t` MB/min.
* **Output & Interpretation:** All three integration methods show the student used **810.00 MB** (`~0.79 GB`) of data during the hour. Because the sine wave completes two full symmetric cycles over 60 minutes, both Trapezoidal and Simpson's rules match the exact `quad` total (`810.0000 MB`) with zero integration error.