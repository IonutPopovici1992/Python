### Lists

example = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)
print(primes)
print(primes[0])
print(primes[1])
print(primes[2])
print(primes[-1])
print(primes[-2])
print(primes[-3])
# print(primes[-9])

print()

# Slicing
print(primes)
print(primes[2:5])
print(primes[0:6])

print()

example2 = [128, True, "Alpha", 1.732, [64, False]]
print(example2)

print()

rolls = [4, 7, 2, 7, 12, 4, 7]
print(rolls)

print()

# Concatenation
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(numbers + letters)
print(letters + numbers)
print(numbers)
print(letters)
print(dir(numbers))
print(dir(letters))
