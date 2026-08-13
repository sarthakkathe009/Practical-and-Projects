def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n == 0 or n == 1: # base case
        return 1
    else:
        return n * factorial(n - 1) # recursive call to factorial

for i in range(6):
    print(f"{i}! = {factorial(i)}")

def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 0: # base case
        return 0
    elif n == 1: # base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # recursive call to fibonacci
print(f"Fibonacci sequence: { [fibonacci(i) for i in range(10)] }")

def sum_of_digits(n):
    """Calculate the sum of digits of a number recursively."""
    if n == 0: # base case
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10) # recursive call to sum_of_digits

print(f"Sum of digits of 12345: {sum_of_digits(12345)}")