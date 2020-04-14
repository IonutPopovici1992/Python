# Python and Prime Numbers

# Prime Number: Only divisible by itself and 1
# (2, 3, 5, 7, 11, 13, 17, 19, ...)

# Composite Number: Can be factored into smaller integers
# (4 = 2 x 2, 6 = 2 x 3, 8 = 2 x 4, 9 = 3 x 3, ...)

# Unit: 1

# V2) Test all divisors from 2 through sqrt(N)


import math
import time


def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # 1 is not prime

    for divisor in range(2, n):
        if n % divisor == 0:
            return False

    return True


def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # 1 is not prime

    max_divisor = math.floor(math.sqrt(n))
    for divisor in range(2, 1 + max_divisor):
        if n % divisor == 0:
            return False

    return True


# ===== Test Function =====
for number in range(1, 21):
    print(number, is_prime_v2(number))

print()
print(50 * "-")
print()

# ===== Time Function =====
t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("Time required: ", t1 - t0)
