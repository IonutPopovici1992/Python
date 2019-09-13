path = "D:/GitHub/Python/Socratica/google_stock_data.csv"

file = open(path)

for line in file:
    print(line)

print(80 * "-")

lines = [line for line in open(path)]

print(lines[0])

print(80 * "-")

print(lines[1])

print(80 * "-")

print(lines[0].strip())

print(80 * "-")

print(lines[0].strip().split(','))

print(80 * "-")

dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1])
