### Lists
# Add data
# Remove data
# Change data

### Tuples
# Cannot be changed
# "Immutable"
# Made quickly

import timeit

list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)

print("List time: ", list_test)
print("Tuple time: ", tuple_test)

print()

empty_tuple = ()
test1 = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

print()

# Alternative Construction of Tuples
test4 = 1,
test5 = 1, 2
test6 = 1, 2, 3

print(test4)
print(test5)
print(test6)

print(type(test4))
print(type(test5))
print(type(test6))

print()

# Tuples with 1 Element
# Tuple Assignment

# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python?", knows_python)

print()

survey2 = (21, "Switzerland", False)

age, country, knows_python = survey2

print("Age = ", age)
print("Country = ", country)
print("Knows Python?", knows_python)

print()

# country = ("Australia")
# print(country)

country = ("Australia",)
print(country)
