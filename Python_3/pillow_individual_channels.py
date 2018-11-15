from PIL import Image

image = Image.open("images/Finland_Lapland_winter.jpg")
print(image.mode)

r, g, b = image.split()

r.show()
g.show()
b.show()
