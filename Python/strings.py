message = 'Hello, World!'

print(message)

# len()
print(len(message))

print(message[0])
print(message[5])

# slicing
print(message[0:5])
print(message[:5])
print(message[7:])

# lower()
print(message.lower())

# upper()
print(message.upper())

# count()
print(message.count('Hello'))
print(message.count('l'))

# find()
print(message.find('World'))

# replace()
message = message.replace('World', 'Python')
print(message)

print()

# format() or f''
greeting = 'Hello'
name = 'Michael'

message1 = greeting + ', ' + name + '. Welcome!'
print(message1)
message2 = '{}, {}. Welcome!'.format(greeting, name)
print(message2)
message3 = f'{greeting}, {name.upper()}. Welcome!'
print(message3)

print()

print(dir(name))

print()

print(help(str.lower))
