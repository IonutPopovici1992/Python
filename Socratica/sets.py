### Sets

example = set()
print(dir(example))

print()

print(help(example.add))

print()

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)

example.add(42)

print(example)

print()

print(len(example))

print()

print(help(example.remove))

print()

example.remove(42)
print(len(example))

print()

# example.remove(50)

print(help(example.discard))

example.discard(50)

print()
print(80*"-")
print()

example2 = set([28, True, 2.71828, "Helium"])
print(len(example2))
example2.clear()
print(len(example2))

print()
print(80*"-")
print()

# Integers 1 - 10

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7, 11])
composites = set([4, 6, 8, 9, 10])

odds.union(evens)
print(odds.union(evens))
evens.union(odds)
print(evens.union(odds))
print(odds)
print(evens)
print(odds.intersection(primes))
print(primes.intersection(evens))
print(evens.intersection(odds))
print(primes.union(composites))

print()
print(80*"-")
print()

print(2 in primes)
print(6 in odds)
print(9 not in evens)

print(dir(primes))
