# Task 7: Gaussian Elimination and LU Decomposition

## B. Input Values and Mathematical Operations
* **Input values:** A `3x3` coefficient matrix `A` (`[[4, -1, 0], [-1, 4, -1], [0, -1, 3]]`) and three different right-hand side measurement vectors `b` (`[15, 10, 10]`, `[16, 11, 9]`, and `[14, 12, 11]`).
* **Math performed:** Uses `scipy.linalg.lu_factor(A)` to break matrix `A` down into Lower (`L`) and Upper (`U`) triangular matrices once. Then it loops through each measurement vector `b` and uses `lu_solve()` (forward and backward substitution) to quickly find `x`, verifying accuracy with `np.linalg.solve()` and the residual norm[cite: 11, 12].

## C. Parameter Change and Impact
* **Change:** Added a fourth measurement vector `np.array([20.0, 15.0, 15.0])` to the `measurement_sets` list without changing matrix `A`.
* **Result:** The program solves the fourth system immediately (`[6.25, 5.0, 6.67]`) without re-running `lu_factor(A)`. This shows that once `A` is factored, adding new `b` vectors requires almost zero extra heavy computation.

## D. Meaning of Output in Words
The output prints the solved `x` values for each of the three measurement sets alongside a residual norm near `0`, proving the answers are exact. Comparing the first `lu_solve` output with `np.linalg.solve` shows identical numbers, proving that factoring a matrix once and reusing it gives the exact same answer much faster when solving repeated equations[cite: 11, 12]. No graph is generated for this task.

## E. New Related Case: Monthly Hostel Bill Splitting with Fixed Ratios
* **Scenario:** Calculating how much three roommates (Alex, Brian, and Chris) owe each month over three months (January–March) when their cost-sharing weights stay fixed, but the monthly utility bills fluctuate.
* **Assumptions:** 
  * The sharing weight matrix `A` stays constant every month.
  * Monthly bill totals `b` (in thousands of KES) change each month based on electricity and water usage.
* **Output & Interpretation:** Factoring `A` once and running `lu_solve` for each month yields exact individual contributions (e.g., in January, Alex pays `3.5k`, Brian pays `2.0k`, and Chris pays `2.5k`). All residual norms are near `0.0`, confirming the bills balance out completely every month.