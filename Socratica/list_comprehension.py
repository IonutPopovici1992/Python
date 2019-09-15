# List Comprehension
# List of squares

squares = []

for i in range(1, 101):
    squares.append(i ** 2)

print(squares)

print(80 * "-")

squares2 = [i ** 2 for i in range(1, 101)]
print(squares2)
