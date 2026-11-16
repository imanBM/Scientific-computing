# Task 18: Systems of Differential Equations

## B. Input Values and Mathematical Operations
* **Input values:** Interaction parameters `a = 1.0`, `b = 0.1`, `c = 1.5`, `d = 0.075`, initial populations `[40.0, 9.0]` (40 prey, 9 predators), and a time window of `(0, 30)` with `400` evaluation points.
* **Math performed:** Uses `scipy.integrate.solve_ivp()` to simultaneously solve two coupled first-order differential equations (`dx/dt` for prey and `dy/dt` for predators), capturing how changes in one population directly drive changes in the other. It generates both a time-series plot and a phase-plane trajectory plot.

## C. Parameter Change and Impact
* **Change:** Increased the predator growth efficiency parameter `d` from `0.075` to `0.15` (predators multiply twice as fast per prey eaten).
* **Result:** Predator numbers spike much higher and faster, wiping out prey numbers down to near zero before crashing themselves. The oscillations become sharper with higher peaks and deeper troughs.

## D. Meaning of Output in Words and Graph Interpretation
* **Output:** The terminal reports the peak and minimum population sizes reached during the simulation, confirming that neither species dies out completely; instead, both rise and fall in repeating waves.
* **Graph:** The left plot shows two wavy lines chasing each other—whenever prey (`x`) peak, predators (`y`) boom shortly after, pushing prey down, which then causes predators to drop. The right plot (phase portrait) forms a closed loop, proving the system repeats the exact same cycle endlessly.

## E. New Related Case: Campus Smocha Stall Supply & Crowd Cycles
* **Scenario:** Modeling the back-and-forth cycle between smocha inventory at a busy campus gate stall (`x`, in dozens) and student customer crowds (`y`, in tens) over 20 operating hours.
* **Assumptions:** 
  * When plenty of fresh smochas are ready, word spreads and more students line up (`d * x * y`).
  * Once the vendor runs low on chapatis and smokies, students walk away (`-c * y`), giving the vendor time to prepare a fresh batch (`a * x`).
* **Output & Interpretation:** Smocha stock oscillates between a low of `1.39` dozen and a peak of `7.51` dozen, while the student crowd fluctuates between `9` and `54` students. The closed loop in the phase portrait shows a self-repeating rush-hour and restocking cycle.