from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
student3 = Student("Michael", "Art", 3.8, True)

print(student1.name)
print(student2.major)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll())
