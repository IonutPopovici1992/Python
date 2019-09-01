# Recursion, the Fibonacci Sequence and Memoization
# Fibonacci Sequence
# 1, 1, 2, 3, 5, 8, 13, 21
# Memoization Part 1

fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value


for n in range(1, 1001):
    print(n, ":", fibonacci(n))
