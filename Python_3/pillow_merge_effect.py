from PIL import Image

image = Image.open("images/Finland_Lapland_winter.jpg")
flag = Image.open("images/Finland_flag.gif")

r1, g1, b1 = image.split()
r2, g2, b2 = flag.split()

new_image = Image.merge("RGB", (r2, g1, b2))
new_image.show()
