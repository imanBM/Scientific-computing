# Task 10: Root Finding — Bisection and Fixed-Point Methods

## B. Input Values and Mathematical Operations
* **Input values:** A nonlinear heat-balance function `f(T) = T - 25 - 10 * exp(-T / 20)`, a search bracket `[20, 40]`, an initial fixed-point guess `T = 30.0`, and tolerance `xtol = 1e-10`[cite: 15, 16].
* **Math performed:** 
  * **Bisection:** Repeatedly cuts the `[20, 40]` interval in half, keeping whichever half has opposite signs at its endpoints until it narrows down on the root where `f(T) = 0`[cite: 15, 16].
  * **Fixed-Point Iteration:** Rewrites the equation as `T = 25 + 10 * exp(-T / 20)` and plugs the output back into the formula repeatedly until the change between guesses is smaller than `1e-10`[cite: 16].
  * Plots the function curve and marks the equilibrium root with a vertical dashed line[cite: 16].

## C. Parameter Change and Impact
* **Change:** Changed the stopping tolerance `xtol` from `1e-10` to `1e-2` in both the bisection solver and the fixed-point loop.
* **Result:** The fixed-point loop finishes in just `3` iterations instead of `11`, and bisection does far fewer interval splits. The equilibrium temperature displays as roughly `27.51°C` instead of `27.514415°C`—faster to compute, just slightly less precise.

## D. Meaning of Output in Words and Graph Interpretation
* **Output:** Both methods print the exact equilibrium temperature (`27.514415°C`) where heat gained equals heat lost, confirming that two completely different root-finding methods agree on the answer[cite: 15, 16].
* **Graph:** The solid blue line shows how the net heat balance changes with temperature. Where the blue curve crosses the horizontal `0` line (marked by the vertical dashed line) is the exact physical equilibrium point[cite: 16].

## E. New Related Case: Campus Movie Night Break-Even Point
* **Scenario:** Finding the minimum number of tickets a student club needs to sell for a campus movie night to break even (zero profit, zero loss) when ticket revenue is linear (`KES 150` per ticket) but venue/security costs grow exponentially with crowd size.
* **Assumptions:** 
  * Tickets sell at `KES 150` each.
  * Total cost is `4000 + 2500 * exp(n / 100)`.
  * Break-even occurs where `Profit(n) = 0` inside the bracket `[30, 100]`.
* **Output & Interpretation:** Both Bisection and Fixed-Point iteration converge to `55.66` tickets (meaning the club must sell at least **56 tickets** to avoid losing money). The graph clearly shows negative net profit (loss) below 56 tickets and positive profit above 56 tickets.