employees_file = open("employees.txt", "a")

print(employees_file.writable())
employees_file.write("\nToby - Human Resources")
employees_file.write("\nKelly - Customer Service")

employees_file.close()
