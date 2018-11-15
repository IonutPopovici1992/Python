from PIL import Image

image = Image.open("images/Finland_Lapland_winter.jpg")
square_image = image.resize((600, 600))
flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)
spin_image = image.transpose(Image.ROTATE_90)

image.show()
square_image.show()
flip_image.show()
spin_image.show()
