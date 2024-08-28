from PIL import Image


image = Image.new(mode="RGB", size=(255,255))
data = image.load()

for y in range(image.height):
    for x in range(image.width):
        data[x,y] = (x, y, 255 - (x+y))
#
# print(range(image.height))
# print(range(image.height, 0, -1))
image.save("ColorPallet.png")

y_rows = []
x_pixels = []

for y in range(9):
    y_rows.append([])
    for x in range(9):
        x_pixels.append([])

