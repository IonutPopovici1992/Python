# René Descartes
# Cartesian Product
# If A and B are sets, then the Cartesian Product
# is the set of pairs (a, b)
# where 'a' is in A and 'b' is in B.
# A x B = {(a, b) | a E A, b E B}

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]

print(cartesian_product)
