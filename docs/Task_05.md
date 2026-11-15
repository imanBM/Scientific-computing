# Task 5: Matrix Algebra and Matrix Operations

## B. Input Values and Mathematical Operations
* **Input values:** A `4x2` matrix representing the `[x, y]` coordinates of a square's corners, a rotation angle (`45` degrees), and scaling factors (`2.0` on x, `1.5` on y).
* **Math performed:** Converts the angle to radians (`np.deg2rad`), builds a `2x2` rotation matrix using sine/cosine and a `2x2` scaling matrix, multiplies them together (`@` operator) into one combined transformation matrix, multiplies the square's coordinates by the transposed transformation matrix, and calculates the matrix determinant (`np.linalg.det()`).

## C. Parameter Change and Impact
* **Change:** Changed the rotation angle from `45` degrees to `90` degrees, and set scaling factors to `1.0` and `1.0` (no scaling).
* **Result:** The square stays its exact original size (determinant becomes `1.0` instead of `3.0`), and all corners rotate 90 degrees counter-clockwise around the origin `(0, 0)`—for example, `(1, 0)` moves directly to `(0, 1)`.

## D. Meaning of Output in Words
The output prints the original corner coordinates of the square, the combined transformation matrix, and the new coordinates after stretching and rotating the shape. The determinant (`3.0`) tells us how much the total area of the shape scaled up (the new area is 3 times larger than the original `1x1` square), and since it isn't zero, the transformation can be reversed. No graph is generated for this task.

## E. New Related Case: Comparing Student Meal Costs Across Two Eateries
* **Scenario:** Calculating a student's daily food expenses from Monday to Wednesday across two different places—an off-campus Restaurant versus the on-campus Cafeteria—using matrix multiplication.
* **Assumptions:** 
  * `weekly_meals` is a `3x3` matrix showing quantities of `[Chapati, Beans, Tea]` eaten each day.
  * `prices` is a `3x2` matrix listing the unit price in KES for each item at the Restaurant (Column 1) and the Cafeteria (Column 2).
* **Output & Interpretation:** Multiplying `weekly_meals @ prices` produces a `3x2` cost matrix showing exact daily spending at both places (e.g., Monday costs `KES 95` at the Restaurant vs. `KES 70` at the Cafeteria). Summing the columns shows a 3-day total of `KES 295` at the Restaurant compared to `KES 215` at the Cafeteria, clearly showing a `KES 80` savings by eating at the cafeteria.