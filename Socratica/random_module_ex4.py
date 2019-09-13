# Normal Distribution (aka "Bell Curve")
# Mean
# Standard Deviation

import random

for i in range(20):
    print(random.normalvariate(0, 1))

print(80 * "-")

for i in range(20):
    print(random.normalvariate(0, 9))

print(80 * "-")

for i in range(20):
    print(random.normalvariate(5, 0.2))

print(80 * "-")

# Discrete Probability Distributions
# randint(min, max)
# "Random Integer"

for i in range(20):
    print(random.randint(1, 6))
