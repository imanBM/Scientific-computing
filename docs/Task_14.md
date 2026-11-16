# Task 14: Curve Fitting and Least-Squares Regression

## B. Input Values and Mathematical Operations
* **Input values:** Two NumPy arrays of 10 data points representing advertising spend (`[1, 2, ..., 10]`) and sales revenue (`[10.2, 13.1, ..., 26.1]`).
* **Math performed:** Uses `np.polyfit(spend, sales, deg=1)` (straight line) and `np.polyfit(spend, sales, deg=2)` (parabola) to find the best-fitting curves by minimizing the sum of squared vertical errors. It then wraps the coefficients with `np.poly1d()` to make predictions, computes the Root Mean Squared Error (`RMSE`) for both models, and plots the curves against the scatter points.

## C. Parameter Change and Impact
* **Change:** Changed the polynomial degree of the second model from `deg=2` (quadratic) to `deg=3` (cubic) using `np.polyfit(spend, sales, deg=3)`.
* **Result:** The RMSE drops slightly further because a cubic curve has more flexibility to bend toward individual noisy data points. However, fitting higher-degree polynomials risks **overfitting**—chasing random noise rather than the true underlying trend.

## D. Meaning of Output in Words and Graph Interpretation
* **Output:** The terminal prints the fitted equation coefficients and the RMSE for each model. A lower RMSE means the curve stays closer to the actual data points on average.
* **Graph:** The black dots show the raw observed data. The dashed linear line rises steadily at a constant slope, while the solid quadratic curve bends slightly to capture how growth slows down at higher spending levels.

## E. New Related Case: Revision Hours vs. CAT Exam Performance
* **Scenario:** Modeling the relationship between daily revision hours (`0.5` to `5.0` hours) and a student's CAT score (out of `30` marks) to predict scores and check for diminishing returns when studying excessively.
* **Assumptions:** 
  * 10 student data points collected across different study habits.
  * Fatigue sets in past 4 hours, causing score gains to level off rather than rise endlessly.
* **Output & Interpretation:** The quadratic fit achieves a much lower error (`RMSE = 0.236` marks) compared to the straight linear fit (`RMSE = 0.779` marks). Studying `3.2` hours predicts a score of `22.58 / 30`, and the curved graph clearly shows diminishing returns after `4.0` hours of revision.