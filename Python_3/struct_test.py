from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 9, 4.73)
print(packed_data)

print()

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

print()

# To get bytes data back to normal
original_data = unpack('iif', packed_data)
print(original_data)
