from PIL import Image
from PIL import ImageFilter

image = Image.open("images/Finland_Lapland_winter.jpg")

blur = image.filter(ImageFilter.BLUR)
detail = image.filter(ImageFilter.DETAIL)
edges = image.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()
