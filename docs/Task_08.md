# Task 8: Iterative Methods for Linear Systems

## B. Input Values and Mathematical Operations
* **Input values:** A `5x5` diagonally dominant matrix `A` representing connections between five interior grid points, boundary vector `b` (`[100, 0, 0, 0, 20]`), tolerance `tol=1e-8`, and `max_iter=500`.
* **Math performed:** Starts with an initial guess of all zeros and repeatedly updates the temperature estimates using two iterative algorithms: **Jacobi** (updates all values at once using the previous step's guesses) and **Gauss-Seidel** (immediately uses updated values as soon as they are calculated in the same step). It tracks the maximum change (`np.linalg.norm(..., ord=np.inf)`) per iteration until it drops below `1e-8`, then plots the error decay using `matplotlib`[cite: 12, 13, 14].

## C. Parameter Change and Impact
* **Change:** Changed the stopping tolerance `tol` from `1e-8` to `1e-2` (a much looser accuracy requirement).
* **Result:** Both methods stop running in roughly a third of the iterations because they don't have to keep refining tiny decimal places. However, the final temperatures are slightly less accurate (only accurate to about 2 decimal places instead of 8).

## D. Meaning of Output in Words and Graph Interpretation
* **Output:** The terminal prints the final estimated temperatures across the 5 points for Jacobi, Gauss-Seidel, and the exact solver (`[86.67, 73.33, 60.0, 46.67, 33.33]`), showing that guessing and refining eventually lands on the exact answer.
* **Graph:** The semi-log plot shows how fast the error drops over each iteration. The **Gauss-Seidel** line slopes downward much steeper and finishes in roughly half as many steps as the **Jacobi** line, proving that using newly updated numbers immediately makes it converge twice as fast.

## E. New Related Case: Hostel Corridor Wi-Fi Signal Distribution
* **Scenario:** Estimating the steady-state Wi-Fi signal strength (in dBm) across 5 adjacent hostel rooms along a straight corridor with a main router at one end (`-30 dBm`) and a repeater at the other (`-45 dBm`).
* **Assumptions:** 
  * Each room's average signal depends equally on its two neighboring rooms.
  * Tolerance is set to `1e-8` for smooth convergence.
* **Output & Interpretation:** Both iterative solvers converge to `[-32.5, -35.0, -37.5, -40.0, -42.5]` dBm across Rooms 1 to 5. Gauss-Seidel reaches the target tolerance in roughly half the iterations of Jacobi, and the results confirm that every room maintains a strong connection (better than `-45 dBm`).