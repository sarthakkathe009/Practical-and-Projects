rate = 0.18
add_tax = lambda price: price * (1 + rate)
print(f"Price with tax (18%): {add_tax(100)}")  # Uses the first rate of 0.18

rate = 0.20
print(f"Price with tax (20%): {add_tax(100)}")  # Uses the second rate of 0.20

import time
# Measeure the execution time of a function
start_time = time.perf_counter()

total = 0
for i in range(1_000_000):
    total += i * i

end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time:.6f} seconds")