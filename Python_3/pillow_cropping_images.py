from PIL import Image

image = Image.open("images/Finland_Lapland_winter.jpg")
# print(image.size)
# print(image.format)
area = (300, 100, 900, 550)
cropped_image = image.crop(area)

image.show()
cropped_image.show()
