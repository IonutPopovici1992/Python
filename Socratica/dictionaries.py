### Dictionaries

# FriendFace post
# user_id = 209
# message = "D5 E5 C5 C4 G4"
# language = "English"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)

post = {
    "user_id": 209,
    "message": "D5 E5 C5 C4 G4",
    "language": "English",
    "datetime": "20230215T124231Z",
    "location": (44.590533, -104.715556)
}

print(type(post))

print()

post2 = dict(message="SS Cotopaxi", language="English")
print(post2)

print()

post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
print(post2)

print()

print(post['message'])
# print(post2['location'])

# if 'location' in post2:
#     print(post2['location'])
# else:
#     print("The post does not contain a location value.")

print()

try:
    print(post2['location'])
except KeyError:
    print("The post does not have a location.")

print()

print(dir(post2))

print()

print(help(post2.get()))

print()

location = post2.get('location', None)
print(location)

print()

print(post)

print()

for key in post.keys():
    value = post[key]
    print(key, "=", value)

print()

for key, value in post.items():
    print(key, "=", value)

print()

print(dir(post))
