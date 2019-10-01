# Map, Filter, and Reduce Functions
# Filter

# Method 3: Use 'filter' function

# Example: Find all data above the average.

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
average = statistics.mean(data)
print(average)

print()

print(filter(lambda x: x > average, data))
print(list(filter(lambda x: x > average, data)))

print()

print(filter(lambda x: x < average, data))
print(list(filter(lambda x: x < average, data)))
