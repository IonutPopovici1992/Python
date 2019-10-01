# Map, Filter, and Reduce Functions
# Map

import math


def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

print(50 * "-")

# Method 2: Use 'map' function

print(map(area, radii))
print(list(map(area, radii)))

print(50 * "-")

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26),
         ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)
print(list(map(c_to_f, temps)))
