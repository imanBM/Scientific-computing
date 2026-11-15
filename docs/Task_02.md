# Task 2: NumPy Arrays and Numerical Computation

## B. Input Values and Mathematical Operations
* **Input values:** A NumPy array holding 24 hourly temperature readings in Celsius.
* **Math performed:** The code calculates the average (`np.mean`), lowest (`np.min`), and highest (`np.max`) temperatures. It also multiplies every number in the array by `1.8` and adds `32` all at once (vectorization) to convert the values to Fahrenheit without needing a `for` loop.

## C. Parameter Change and Impact
* **Change:** Changed the conversion formula from `1.8 * temperatures_c + 32` to `temperatures_c + 273.15`.
* **Result:** Instead of converting Celsius to Fahrenheit (giving numbers around 60–80), the code converts the temperatures to Kelvin (giving numbers around 290–302). The average, min, and max values in Celsius stay the same.

## D. Meaning of Output in Words
The output gives a quick summary of the coldest, hottest, and average temperatures recorded over 24 hours. It also prints the first six converted temperatures so you can confirm the unit conversion worked across the array. There is no graph in this task.

## E. New Related Case: Weekly Mobile Data Usage
* **Scenario:** Tracking daily phone data usage in Megabytes (MB) over one week to see which days use the most bundles and converting the totals to Gigabytes (GB).
* **Assumptions:** 
  * 7 daily readings recorded in MB.
  * 1 GB equals 1024 MB (`daily_mb / 1024.0`).
* **Output & Interpretation:** The script shows an average usage of `1191.57 MB` per day, a low of `640.00 MB`, and a peak of `2100.00 MB` (likely from downloading a large file or streaming). The converted array shows each day's usage in GB (e.g., `0.83 GB`, `1.17 GB`, up to `2.05 GB`).