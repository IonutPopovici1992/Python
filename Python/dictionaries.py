student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# student['phone'] = '555-555'
# student['name'] = 'Jane'

student.update({'name': 'Jane', 'age': 26, 'phone': '555-555'})

print(student)
print(student['name'])
print(student['age'])
print(student['courses'])

print()

print(student.get('name'))
print(student.get('age'))
print(student.get('courses'))
print(student.get('phone', 'Not Found'))

print()

# del student['age']

# age = student.pop('age')

print(student)
# print(age)

print()

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

print()

for key, value in student.items():
    print(key, value)
