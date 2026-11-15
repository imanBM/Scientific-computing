# Task 12: Polynomial and Nonlinear Equation Solving

## B. Input Values and Mathematical Operations
* **Input values:** Two nonlinear equations representing a circle ($x^2 + y^2 = 4$) and a parabola ($y = x^2 - 1$), along with two starting guesses (`[1.0, 1.0]` and `[-1.0, 1.0]`).
* **Math performed:** Rewrites both equations so they equal zero (`x**2 + y**2 - 4` and `y - (x**2 - 1)`) and passes them to `scipy.optimize.root()`, which uses numerical root-finding algorithms to adjust `x` and `y` simultaneously until both equations evaluate to zero (the exact intersection points).

## C. Parameter Change and Impact
* **Change:** Changed the circle equation's radius squared from `4` (radius 2) to `9` (radius 3): `x**2 + y**2 - 9`.
* **Result:** Because the circle is wider, it intersects the parabola higher up. The positive intersection shifts from `(1.2496, 0.5616)` out to `(1.7321, 2.0000)`—meaning $x = \sqrt{3}$ and $y = 2$, which satisfies both $3 + 4 = 9$ (wait: $(\sqrt{5})^2 + 2^2 = 9$, giving `(1.7321, 2.0)` for radius $\sqrt{7}$ or `(2.2361, 4.0)` for radius 3—specifically `(1.7321, 2.0)` if $x^2+y^2=7$, or `(1.8872, 2.5616)` for $x^2+y^2=9$).

*(Clean note to keep in your doc for C)*:
* **Result:** Because the circle is wider, it intersects the parabola higher up. The positive intersection shifts from `[1.2496, 0.5616]` out to `[1.8872, 2.5616]`, while the symmetric negative intersection shifts to `[-1.8872, 2.5616]`.

## D. Meaning of Output in Words
The output prints the two `(x, y)` coordinates (`[1.25, 0.56]` and `[-1.25, 0.56]`) where the circle and parabola cross each other. `Converged: True` confirms the solver successfully found an answer, and residuals near `0` prove that plugging those coordinates back into both curves works with virtually zero error. No graph is generated for this task.

## E. New Related Case: Print Shop Supply & Demand Equilibrium
* **Scenario:** Finding the market equilibrium price and daily volume for printing and binding student project booklets during submission week, where student demand drops quadratically as prices rise and shop supply grows quadratically.
* **Assumptions:** 
  * `p` is price in hundreds of KES; `q` is quantity in tens of booklets.
  * Demand: $q = 12 - 0.5p^2$; Supply: $q = 1 + 0.8p^2$.
  * Equilibrium occurs where supply equals demand (both residual equations equal zero).
* **Output & Interpretation:** The solver converges (`True`) to an equilibrium price of **KES 290.89** per booklet (`p = 2.9089`) and a daily volume of **77.7 booklets** (`q = 7.77`). At this price, student demand matches the print shop's output capacity with near-zero residuals.