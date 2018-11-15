from PIL import Image

image = Image.open("images/Finland_Lapland_winter.jpg")
flag = Image.open("images/Finland_flag.gif")

area = (784, 490, 960, 600)
image.paste(flag, area)

image.show()
