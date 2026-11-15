# Task 6: Solution of Systems of Linear Equations

## B. Input Values and Mathematical Operations
* **Input values:** A `2x2` coefficient matrix `A` representing CPU and memory usage per server type (`[[4, 2], [8, 12]]`), and a target vector `b` representing total observed usage (`[20, 72]`)[cite: 9].
* **Math performed:** Solves the linear system $Ax = b$ using `np.linalg.solve(A, b)` to find the unknown server counts `x`[cite: 9, 10]. It then multiplies `A @ solution` to verify the answer and calculates the residual norm (`np.linalg.norm(b - A @ solution)`) to check for any leftover numerical error[cite: 10].

## C. Parameter Change and Impact
* **Change:** Changed the total observed usage vector `b` from `[20.0, 72.0]` to `[24.0, 80.0]`.
* **Result:** The solver updates the required number of active servers from `3` Type A and `4` Type B to `4` Type A and `4` Type B (`4(4) + 2(4) = 24` CPU units, and `8(4) + 12(4) = 80` GB memory). The residual norm remains `0.0`, confirming an exact match.

## D. Meaning of Output in Words
The output tells you the exact number of Type A (`3`) and Type B (`4`) servers currently running to hit the exact CPU and memory totals[cite: 9, 10]. The verification line confirms that plugging those numbers back into the system reproduces `[20, 72]`, and a residual norm of `0.0` proves the solution is 100% accurate with no rounding error[cite: 9, 10]. No graph is generated for this task.

## E. New Related Case: Campus Event Ticket Sales Breakdown
* **Scenario:** Determining how many Regular tickets and VIP tickets were sold for a campus fresher's night event when you only know the total headcount and the total money collected.
* **Assumptions:** 
  * Regular tickets cost `KES 200`, and VIP tickets cost `KES 500`.
  * A total of `150` tickets were sold, generating `KES 42,000` in total revenue.
* **Output & Interpretation:** Solving the system gives `110` Regular tickets and `40` VIP tickets (`110 + 40 = 150` tickets, and `110(200) + 40(500) = 22,000 + 20,000 = 42,000` KES). The residual norm is `0.0`, confirming the exact breakdown of ticket sales.