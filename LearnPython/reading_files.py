employees_file = open("employees.txt", "r")

print(employees_file.readable())
print(employees_file.read())
# print(employees_file.readline())
# print(employees_file.readlines())

employees_file.close()
