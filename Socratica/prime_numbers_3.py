# Python and Prime Numbers

# Prime Number: Only divisible by itself and 1
# (2, 3, 5, 7, 11, 13, 17, 19, ...)

# Composite Number: Can be factored into smaller integers
# (4 = 2 x 2, 6 = 2 x 3, 8 = 2 x 4, 9 = 3 x 3, ...)

# Unit: 1

# V3)


import math
import time


def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # 1 is not prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for divisor in range(3, 1 + max_divisor, 2):
        if n % divisor == 0:
            return False

    return True


# ===== Test Function =====
for number in range(1, 21):
    print(number, is_prime_v3(number))

print()
print(50 * "-")
print()

# ===== Time Function =====
t0 = time.time()
for n in range(1, 100000):
    is_prime_v3(n)
t1 = time.time()
print("Time required: ", t1 - t0)
