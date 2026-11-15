# Task 3: Mathematical Functions and Vectorization

## B. Input Values and Mathematical Operations
* **Input values:** A generated NumPy array of 1,000,000 random network latency readings ranging between `5 ms` and `250 ms`[cite: 6].
* **Math performed:** The code divides every reading by `1000.0` to convert milliseconds to seconds, and then squares each value (`seconds ** 2`)[cite: 6]. It runs this math twice—once using a standard Python `for` loop and once using NumPy vectorization—and uses `timeit` to measure how fast each method finishes[cite: 6].

## C. Parameter Change and Impact
* **Change:** Changed the array size from `1_000_000` elements to `5_000_000` elements.
* **Result:** Both methods take roughly 5 times longer to finish because there is 5 times more data to process. However, the Python loop slows down significantly in real-world seconds (taking over a full second), while the vectorized NumPy code still finishes in a fraction of a second, proving that vectorization scales much better with large datasets.

## D. Meaning of Output in Words
The output prints the first five squared latency numbers to verify that the math works, followed by the exact time in seconds it took the loop and the vectorized function to finish[cite: 6]. The final line shows the "speed-up" multiplier (e.g., `50x` or `100x`), proving that doing math on an entire NumPy array at once is drastically faster than looping through items one by one[cite: 6]. No graph is generated for this task.

## E. New Related Case: Bulk Mobile Money Fee Calculation
* **Scenario:** Calculating transaction fees for 1,000,000 simulated mobile money transfers (between KES 100 and KES 5,000) to see how much faster vectorized processing is for a payment system.
* **Assumptions:** 
  * 1,000,000 random transfer amounts generated using NumPy.
  * Every transfer is charged a flat 1.5% fee plus a KES 5.00 tax (`(transfers * 0.015) + 5.0`).
* **Output & Interpretation:** The script prints the first five calculated fees in KES, then compares the execution times. The vectorized NumPy approach calculates all one million fees in milliseconds, achieving a massive speed-up over the traditional `for` loop.