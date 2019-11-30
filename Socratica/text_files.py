# Text Files in Python

# print(help(open))

# f = open("text_files/guido_bio.txt")
# text = f.read()
# f.close()

# with open("text_files/guido_bio.txt") as fobj:
#     bio = fobj.read()
#
# print(bio)

# try:
#     with open("future_lottery_numbers.txt") as f:
#         text = f.read()
# except FileNotFoundError:
#     text = None
#
# print(text)

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

# with open("text_files/oceans.txt", "w") as f:
#     for ocean in oceans:
#         f.write(ocean)
#         f.write("\n")

# with open("text_files/oceans.txt", "w") as f:
#     for ocean in oceans:
#         print(ocean, file=f)

with open("text_files/oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)
