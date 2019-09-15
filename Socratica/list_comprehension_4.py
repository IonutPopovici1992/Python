# List Comprehension

movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946),
          ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954),
          ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 2001),
          ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001),
          ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

pre2k = [title for (title, year) in movies if year < 2000]

print(pre2k)

print(80 * "-")

# Scalar Multiplication

v = [2, -3, 1]
print(4 * v)

print()

print([2, 4, 6] + [1, 3])

print()

w = [4 * x for x in v]
print(w)
