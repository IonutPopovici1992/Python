number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
print(number_grid[1][1])
print(number_grid[2][2])

print()

for row in number_grid:
    print(row)

print()

for row in number_grid:
    for column in row:
        print(column)
