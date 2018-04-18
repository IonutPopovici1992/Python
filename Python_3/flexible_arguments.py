def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(1)
add_numbers(1, 2)
add_numbers(1, 2, 3)
add_numbers(100, 200, 300)
add_numbers(250, 250, 250)
