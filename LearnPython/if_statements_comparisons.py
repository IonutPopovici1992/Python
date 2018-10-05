def max_number(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3


print(max_number(1, 2, 3))
print(max_number(10, 20, 30))
print(max_number(100, 200, 300))
