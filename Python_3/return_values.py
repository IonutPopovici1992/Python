def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

johnnys_limit = allowed_dating_age(25)
creepy_joe_limit = allowed_dating_age(50)

print("Johnny can date girls", johnnys_limit, "or older.")
print("Creepy Joe can date girls", creepy_joe_limit, "or older.")
