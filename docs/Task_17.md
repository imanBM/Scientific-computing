# Task 17: Ordinary Differential Equations — First-Order Systems

## B. Input Values and Mathematical Operations
* **Input values:** Initial temperature `T0 = 90.0°C`, ambient room temperature `22.0°C`, cooling rate `k = 0.05`, time span `(0, 60)` minutes, and Euler step size `dt = 2.0` minutes.
* **Math performed:** Solves the first-order differential equation $dT/dt = -k(T - T_{ambient})$ using three approaches:
  * **Euler's Method:** Steps forward 2 minutes at a time using `T_next = T_curr + dt * rate`.
  * **`scipy.integrate.solve_ivp`:** Uses an adaptive Runge-Kutta (`RK45`) solver to compute high-precision temperature values.
  * **Analytical formula:** Computes the exact exponential curve $T(t) = T_{ambient} + (T_0 - T_{ambient})e^{-kt}$ to measure error.

## C. Parameter Change and Impact
* **Change:** Increased the Euler step size `dt` from `2.0` minutes to `5.0` minutes (taking bigger time jumps).
* **Result:** Euler's method becomes noticeably less accurate—it drops too fast at the beginning and underestimates the temperature by over `1.5°C` compared to the exact curve, because assuming the cooling rate stays constant for 5 full minutes introduces larger truncation error.

## D. Meaning of Output in Words and Graph Interpretation
* **Output:** The terminal prints the temperature at the end of the time window for Euler, `solve_ivp`, and the exact formula, showing that `solve_ivp` matches the exact math to several decimal places while Euler lags slightly behind.
* **Graph:** All three curves start hot and decay exponentially toward room temperature (`22°C`). The `solve_ivp` dots sit directly on top of the solid black exact line, whereas the red dashed Euler line dips slightly below it because Euler over-estimates how fast the liquid cools during each step.

## E. New Related Case: Hostel Tea Cooling Time
* **Scenario:** Tracking how quickly a freshly poured mug of hot tea (`92°C`) cools down in a `22°C` hostel room so a student knows how many minutes to wait before drinking it comfortably (`55°C`).
* **Assumptions:** 
  * Cooling constant `k = 0.08` per minute (typical ceramic mug indoors).
  * Room temperature stays steady at `22.0°C`.
* **Output & Interpretation:** After `10` minutes, `solve_ivp` shows the tea is at `53.45°C` (right around the `55°C` ideal drinking line on the graph, meaning ~9.5 minutes is the sweet spot). Euler's method estimates `52.38°C` at 10 minutes—slightly underestimating the temperature due to the 2-minute step size.