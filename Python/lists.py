### Lists


courses = ['Geography', 'History', 'Math', 'Physiscs']
courses_2 = ['Art', 'Biology']
numbers = [1, 5, 2, 4, 3]
print(courses)
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

## append()
# courses.append('Art')
# print(courses)

## insert()
# courses.insert(0, 'Art')
# print(courses)

## extend()
# courses.extend(courses_2)
# print(courses)

## sort()
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

## remove()
# numbers.remove(5)
# print(numbers)

## pop()
# numbers.pop()
# print(numbers)

print("-----")

for course in courses:
    print(course)

print("-----")

for index, course in enumerate(courses, start=1):
    print(index, course)

print("-----")

course_str = ' - '.join(courses)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)
