# Lambda Expressions & Anonymous Functions

# Anonymous Function = Lambda Expression

# Write a function to compute 3x + 1


def f1(x):
    return 3 * x + 1


print(f1(2))

print(50 * "-")

lambda x: 3 * x + 1

g = lambda x: 3 * x + 1
print(g(2))

print(50 * "-")

# Lambda Expression with multiple inputs
# Combine first name and last name into a single "Full Name"

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   leonhard", "EULER"))

print(50 * "-")

# A function with no name ...
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke",
                 "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

print(help(scifi_authors.sort))

print(50 * "-")

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

print(50 * "-")

# Quadratic Functions
# f(x) = a * x ** 2 + b * x + c

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a * x ** 2 + b * x + c

f2 = build_quadratic_function(2, 3, -5)
print(f2(0))
print(f2(1))
print(f2(2))
print(build_quadratic_function(3, 0, 1)(2))  # 3x^2 + 1 evaluated for x = 2
