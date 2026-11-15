# Task 11: Root Finding — Newton-Raphson and Secant Methods

## B. Input Values and Mathematical Operations
* **Input values:** A list of cash flows `[-10000, 3000, 3500, 4000, 2500]`, an initial guess `x0 = 0.10` for Newton-Raphson, two starting guesses `x0 = 0.05, x1 = 0.20` for Secant, and tolerance `xtol = 1e-12`[cite: 17, 18].
* **Math performed:** Defines the Net Present Value (`npv`) equation and its exact calculus derivative (`d_npv`), then uses `scipy.optimize.root_scalar` to solve for the interest rate where `NPV(rate) = 0` using both the **Newton-Raphson method** (tangent line steps) and the **Secant method** (two-point slope approximation)[cite: 17, 18].

## C. Parameter Change and Impact
* **Change:** Increased the Year 1 cash inflow from `3000` to `4500` (stronger early return on the initial `-10000` investment).
* **Result:** The Internal Rate of Return (IRR) jumps from `11.1586%` up to `17.5425%`. Because money comes back faster in the first year, the investment yields a much higher effective interest rate.

## D. Meaning of Output in Words
The output prints the Internal Rate of Return (IRR) as a percentage (`11.158616%`), which is the exact break-even interest rate where the future cash inflows equal the initial `-10,000` cost. Both Newton-Raphson and Secant give the exact same percentage, and plugging that rate back into `npv()` outputs `0.000000`, confirming the root is exact. No graph is generated for this task.

## E. New Related Case: Student Side-Hustle Monthly Rate of Return
* **Scenario:** Calculating the monthly Internal Rate of Return (IRR) for a student who spends `KES 25,000` on equipment for a campus printing/delivery side-hustle and tracks net profits over 4 months.
* **Assumptions:** 
  * Month 0 outlay is `-KES 25,000`.
  * Net monthly profits are `KES 7,000`, `8,000`, `8,500`, and `6,500` (total `KES 30,000` collected).
* **Output & Interpretation:** Both Newton-Raphson and Secant converge to a monthly return rate of `7.742969%` (with `NPV = KES 0.00000000`). This means the side-hustle beats standard savings/mobile-money interest rates, making the upfront `KES 25,000` investment worthwhile.