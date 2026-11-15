import numpy as np

# Rows = Days (Mon, Tue, Wed), Columns = Food items (Chapati, Beans, Tea)
weekly_meals = np.array([
    [2, 1, 1],  # Monday: 2 chapatis, 1 beans, 1 tea
    [3, 1, 0],  # Tuesday: 3 chapatis, 1 beans, 0 tea
    [1, 1, 2]   # Wednesday: 1 chapati, 1 beans, 2 teas
])

# Prices in KES at two different spots: [Restaurant (Outside Campus), Cafeteria (On Campus)]
# Rows = Food items (Chapati, Beans, Tea), Columns = Spots
prices = np.array([
    [20.0, 15.0],  # Chapati price
    [40.0, 30.0],  # Beans price
    [15.0, 10.0]   # Tea price
])

# Matrix multiplication to get total daily cost at each spot
daily_costs = weekly_meals @ prices

print("Daily meal quantities (Mon-Wed):\n", weekly_meals)
print("\nTotal daily cost [Restaurant, Cafeteria] in KES:\n", daily_costs)
print("\n3-Day Total [Restaurant, Cafeteria]:", np.sum(daily_costs, axis=0))