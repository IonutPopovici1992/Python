lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Tim"]

# extend()
friends.extend(lucky_numbers)
print(friends)

# append()
friends.append("Joel")
print(friends)

# insert()
friends.insert(1, "Kelly")
print(friends)

# remove()
friends.remove("Jim")
print(friends)

# clear()
friends.clear()
print(friends)

# pop()
friends.pop()
print(friends)

# index()
friends.index("Kevin")
print(friends)

# count()
friends.count("Jim")
print(friends)

# sort()
friends.sort()
print(friends)

# reverse()
friends.reverse()
print(friends)

# copy()
friends2 = friends.copy()
print(friends2)
