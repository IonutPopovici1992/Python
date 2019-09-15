# Python Classes and Objects


class User:
    pass


user1 = User()
# user1 is an "instance" of User
# user1 is an "object"

user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name)
print(user1.last_name)

print(80 * "-")

first_name = "Arthur"
last_name = "Clarke"

print(first_name, last_name)

print(80 * "-")

print(user1.first_name, user1.last_name)

print(80 * "-")

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

print(first_name, last_name)

print(10 * "*")

print(user1.first_name, user1.last_name)

print(10 * "*")

print(user2.first_name, user2.last_name)

print(80 * "-")

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"

print(user1.age)
# print(user2.age)
print(user2.favorite_book)
