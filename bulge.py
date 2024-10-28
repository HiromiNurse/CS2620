from PIL import Image
import math


image_start = Image.open("stoat.jpg")
data_start = image_start.load()
width, height = image_start.size

image_out = Image.new("RGB", size=(width, height))
data_out = image_out.load()
new_width, new_height = image_out.size

min_dimension = min(new_width, new_height)

for y in range(image_out.height):
    for x in range(image_out.width):
        pixel = data_start[x, y]

        xc = x - image_out.width / 2
        yc = y - image_start.height / 2

        radius = math.sqrt(xc**2 + yc**2)
        theta = math.atan2(yc, xc)

        new_radius = (radius/min_dimension/2) ** 2

        new_x = math.cos(theta)*new_radius*min_dimension/2
        new_y = math.sin(theta)*new_radius*min_dimension/2

        new_x += image_out.width/2
        new_y += image_out.height/2

        if new_x < 0 or new_x >= image_out.width or new_y < 0 or new_y >= image_out.height:
            data_out[x, y] = data_start[math.floow(new_x), math.floor(new_y)]
        else:
            data_out[x, y] = data_start[math.floor(new_x), math.floor(new_y)]

image_out.save("out.png")