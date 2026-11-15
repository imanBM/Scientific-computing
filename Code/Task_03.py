import numpy as np
import timeit

# Simulate 1,000,000 M-Pesa transfers between KES 100 and KES 5,000
rng = np.random.default_rng(42)
transfers = rng.uniform(100, 5000, 1_000_000)

# Method 1: Standard Python loop (slow)
def loop_fees():
    fees = []
    for amount in transfers:
        # Assume a flat 1.5% transaction fee plus KES 5 tax
        fee = (amount * 0.015) + 5.0
        fees.append(fee)
    return fees

# Method 2: Vectorized NumPy operation (fast)
def vectorized_fees():
    return (transfers * 0.015) + 5.0

loop_time = timeit.timeit(loop_fees, number=1)
vector_time = timeit.timeit(vectorized_fees, number=3) / 3
result = vectorized_fees()

print("First five calculated fees (KES):", np.round(result[:5], 2))
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Speed-up: {loop_time / vector_time:.1f}x faster")