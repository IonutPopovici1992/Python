from PIL import Image

image = Image.open("images/Finland_Lapland_winter.jpg")
print(image.size)
print(image.format)

image.show()
