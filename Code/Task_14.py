import numpy as np
import matplotlib.pyplot as plt

# Daily revision hours before a CAT vs. actual CAT score (out of 30)
study_hours = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
cat_scores = np.array([11.0, 13.5, 15.0, 17.5, 19.5, 22.0, 23.5, 25.0, 26.0, 26.5])

# Fit a degree-1 (linear) and degree-2 (quadratic) polynomial using least squares
linear_coeffs = np.polyfit(study_hours, cat_scores, deg=1)
quad_coeffs = np.polyfit(study_hours, cat_scores, deg=2)

linear_model = np.poly1d(linear_coeffs)
quad_model = np.poly1d(quad_coeffs)

# Calculate Root Mean Squared Error (RMSE) to see which curve fits better
rmse_linear = np.sqrt(np.mean((cat_scores - linear_model(study_hours))**2))
rmse_quad = np.sqrt(np.mean((cat_scores - quad_model(study_hours))**2))

print("Linear model coefficients (slope, intercept):", np.round(linear_coeffs, 3))
print("Quadratic model coefficients:", np.round(quad_coeffs, 3))
print(f"Linear RMSE:    {rmse_linear:.3f} marks")
print(f"Quadratic RMSE: {rmse_quad:.3f} marks")
print(f"Predicted score for 3.2 hours (Quadratic): {quad_model(3.2):.2f} / 30")

grid = np.linspace(0.5, 5.0, 200)
plt.scatter(study_hours, cat_scores, color="black", label="Actual CAT scores")
plt.plot(grid, linear_model(grid), linestyle="--", label=f"Linear fit (RMSE={rmse_linear:.2f})")
plt.plot(grid, quad_model(grid), label=f"Quadratic fit (RMSE={rmse_quad:.2f})")
plt.xlabel("Daily Revision Hours")
plt.ylabel("CAT Score (out of 30)")
plt.title("Revision Hours vs. CAT Score Regression")
plt.legend()
plt.grid(True)
plt.show()