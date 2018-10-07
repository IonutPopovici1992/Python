def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 1))
print(raise_to_power(2, 2))
print(raise_to_power(2, 3))
print(raise_to_power(2, 4))
print(raise_to_power(2, 5))
