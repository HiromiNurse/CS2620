from PIL import Image
import math
from imageFunctions import rotateBigger


def nn_interpolation(data, x, y):
    return (math.floor(x), math.floor(y))


def interpolate(start, end, percent):
    return (percent * (end - start) + start)


def interpolateRGB(start, end, percent):
    r_start, g_start, b_start = start[0], start[1], start[2]
    r_end, g_end, b_end = end[0], end[1], end[2]

    r = interpolate(r_start, r_end, percent)
    g = interpolate(g_start, g_end, percent)
    b = interpolate(b_start, b_end, percent)

    return (r, g, b)


def bilinear_interpolation(data, x, y):
    # Gather pixels (need 4 pixels)
    x_start = math.floor(x)
    x_end = x_start + 1
    x_percent = x - x_start

    y_start = math.floor(y)
    y_end = y_start + 1
    y_percent = y - y_end

    top_left = data[int(x_start), int(y_start)]
    top_right = data[int(x_end), int(y_start)]
    bottom_left = data[int(x_start), int(y_end)]
    bottom_right = data[int(x_end), int(y_end)]

    # Interpolate across the top two pixels
    top = interpolateRGB(top_left, top_right, x_percent)

    # Interpolate across the bottom two pixels
    bottom = interpolateRGB(bottom_left, bottom_right, x_percent)

    # Interpolate between the top and bottom pixels
    result = interpolateRGB(top, bottom, y_percent)

    # Return the result
    return (math.floor(result[0]), math.floor(result[1]), math.floor(result[2]))

image_start = Image.open("skib.jpg")
image_start = rotateBigger(image_start)
data_start = image_start.load()
width, height = image_start.size

image_out = Image.new("RGB", size=(width, height))
data_out = image_out.load()
new_width, new_height = image_out.size

min_dimension = min(new_width, new_height)

for y in range(new_height):
    for x in range(new_width):
        pixel = data_start[x, y]

        xc = x - new_width / 2
        yc = y - new_height / 2

        radius = math.sqrt(xc**2 + yc**2)
        theta = math.atan2(yc, xc)

        new_radius = (radius/(min_dimension/2)) ** 2
        if (radius > (min_dimension/2)):
            new_radius = radius/(min_dimension/2)

        new_x = math.cos(theta)*new_radius*min_dimension/2
        new_y = math.sin(theta)*new_radius*min_dimension/2

        new_x += new_width/2
        new_y += new_height/2

        if new_x < 0 or new_x >= new_width-1 or new_y < 0 or new_y >= new_height-1:
            # data_out[x, y] = data_start[math.floor(new_x), math.floor(new_y)]
            data_out[x, y] = (0, 0, 0)
        else:
            # data_out[x, y] = data_start[math.floor(new_x), math.floor(new_y)]
            data_out[x, y] = bilinear_interpolation(data_start, new_x, new_y)

image_out.save("out.png")
