# Task 4: Floating-Point Arithmetic and Numerical Errors

## B. Input Values and Mathematical Operations
* **Input values:** Hardcoded decimal numbers (`0.1`, `0.2`, `0.3`), `np.sqrt(2)` vs an approximation (`1.414`), and very small numbers (`1e-4`, `1e-8`, `1e-12`).
* **Math performed:** 
  * Adds `0.1 + 0.2` and compares it to `0.3` using exact equality (`==`) versus tolerance checking (`np.isclose()`).
  * Computes **absolute error** (`|true - approx|`) and **relative error** (`absolute error / |true|`).
  * Compares two algebraically identical formulas—`(sqrt(1+x) - 1) / x` (unstable) and `1 / (sqrt(1+x) + 1)` (stable)—as `x` gets extremely tiny[cite: 8].

## C. Parameter Change and Impact
* **Change:** Changed the approximated value of $\sqrt{2}$ from `1.414` to `1.41421` (more decimal places).
* **Result:** The absolute error drops from `0.00021356` down to `0.00000356`, and the relative error shrinks from `0.0151%` to `0.00025%`. Using more decimal places reduces round-off error significantly[cite: 7, 8].

## D. Meaning of Output in Words
The output proves that computers cannot store certain base-10 decimals (like `0.1` and `0.2`) with 100% accuracy in binary, which causes `0.1 + 0.2 == 0.3` to evaluate as `False`[cite: 7, 8]. It shows that using `np.isclose()` safely ignores tiny binary rounding noise, and demonstrates how rewriting a math formula prevents catastrophic precision loss when working with tiny numbers[cite: 8]. No graph is generated for this task.

## E. New Related Case: Student Budget & Split-Bill Rounding Errors
* **Scenario:** Checking a student's daily snack expenses against an exact budget limit, and calculating the rounding error when splitting a KES 1,000 utility bill among 3 roommates.
* **Assumptions:** 
  * Three items cost `10.10`, `20.20`, and `30.30` (exact sum is `60.60`).
  * A `1000 / 3` split (`333.3333...`) is rounded to `333.33` for practical mobile money payment.
* **Output & Interpretation:** Python evaluates `10.10 + 20.20 + 30.30` as `60.599999999999994`, causing a strict `==` budget check to fail (`False`), whereas `np.isclose()` accurately returns `True`. For the split bill, the absolute rounding error is `KES 0.003333` per person (`0.001%` relative error), which explains why a 1-cent discrepancy (`KES 999.99` total) occurs when everyone pays the rounded amount.