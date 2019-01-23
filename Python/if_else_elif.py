## Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# ----------

language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match!')

# ----------
# and
# or
# not

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome!')

# ----------
a = [1, 2, 3]
# b = [1, 2, 3]
b = a

print(a == b)
print(a is b)
print(id(a))
print(id(b))

# ----------
## False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = 1

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
