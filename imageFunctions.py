from PIL import Image


def greyscale_Corrected(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscalec_value = int((red * .21) + (green * .71) + (blue * .08)) // 3
            data[x, y] = (greyscalec_value, greyscalec_value, greyscalec_value)
        return image


def greyscale(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscale_value = (red + green + blue) // 3
            data[x, y] = (greyscale_value, greyscale_value, greyscale_value)
    return image


def colorIsolationRed(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscale_value = (red + green + blue) // 3
            if red > 65 and (red - green) > 15 and (red - blue) > 25 and red > greyscale_value:
                data[x, y] = (red, green, blue)
            else:
                data[x, y] = (greyscale_value, greyscale_value, greyscale_value)
    return image


def colorIsolationGreen(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscale_value = (red + green + blue) // 3
            if green > 45 and (green - red) > 15 and (green - blue) > 15 and green > greyscale_value:
                data[x, y] = (red, green, blue)
            else:
                data[x, y] = (greyscale_value, greyscale_value, greyscale_value)
    return image


def colorIsolationBlue(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscale_value = (red + green + blue) // 3
            if blue > 65 and (blue - green) > 15 and (blue - red) > 25 and blue > greyscale_value:
                data[x, y] = (red, green, blue)
            else:
                data[x, y] = (greyscale_value, greyscale_value, greyscale_value)
    return image


def xAxisMirrorL(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            data[image.width - x - 1, y] = (red, green, blue)
    return image


def xAxisMirrorR(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if x >= (image.width // 2):
                data[image.width - 1 - x, y] = (red, green, blue)
    return image


def yAxisMirrorT(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            data[x, image.height - 1 - y] = (red, green, blue)
    return image


def yAxisMirrorB(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if y >= (image.height // 2):
                data[x, image.height - 1 - y] = (red, green, blue)
    return image


def diagonalMirrorT(image):  # fix
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            data[x, y] = data[x, y]
    return image


def diagonalMirrorB(image):  # fix
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            data[image.image.width - x - 1, y] = data[y, x]


def colorInvert(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            data[x, y] = (255 - red, 255 - green, 255 - blue)
    return image


def xAxisFlip(image):
    data = image.load()
    for y in range(image.height):
        x_pixels = []
        for x in range(image.width):
            pixel = data[x, y]
            x_pixels.append(pixel)
        for x in range(image.width):
            data[x, y] = x_pixels[image.width - x - 1]
    return image


def yAxisFlip(image):
    data = image.load()
    for x in range(image.width):
        y_pixels = []
        for y in range(image.height):
            pixel = data[x, y]
            y_pixels.append(pixel)
        for y in range(image.height):
            data[x, y] = y_pixels[image.height - y - 1]
    return image


def flipDiagonal(image):
    image = yAxisFlip(image)
    image = xAxisFlip(image)
    return image


def rotateClockwise(image):
    data = image.load()
    rotated_image = Image.new(mode="RGB", size=(image.height, image.width))
    rotated_image_data = rotated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            rotated_image_data[rotated_image.width - 1 - y, x] = pixel
    return rotated_image


def rotateCClockwise(image):
    data = image.load()
    rotated_image = Image.new(mode="RGB", size=(image.height, image.width))
    rotated_image_data = rotated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            rotated_image_data[y, image.width - 1 - x] = pixel
    return rotated_image

# Rotates the image and adds background in the new whitespace
# Fix later 
def rotateBigger(image):
    data = image.load()
    degrees = int(input("Rotation in degrees: "))


# Rotates and only keeps the original size of the image
def rotateCutoff(image):
    data = image.load()

# Rotates and takes the smallest window fitting all of image
def rotateSmallest(image):
    data = image.load()

def translation(image):
    data = image.load()
    dx = int(input("Change in x: "))
    dy = int(input("Change in y: "))
    translated_image = Image.new("RGB", size=((image.width+dx), (image.height+dy)))
    new_data = translated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            new_data[x+dx, y+dy] = pixel
    return translated_image

def scale(image):
    data = image.load()
    scaleSize = int(input("Scale Amount: "))
    new_image = Image.new("RGB", size=(int(image.width*scaleSize), int(image.height*scaleSize)))
    new_data = new_image.load()
    for y in range(new_image.height):
        for x in range(new_image.width):
            current_x = x
            current_y = y

            pixel = data[int(current_x / scaleSize), int(current_y / scaleSize)]

            new_data[x, y] = pixel
    return new_image

def transform(image):
    data = image.load()
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    e = int(input("e: "))
    f = int(input("f: "))
    translated_image = Image.new("RGB", size=((image.width), (image.height)))
    new_data = translated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]

            new_x = x * a + y * b + c
            new_y = x * d + y * e + f

            new_data[new_x, new_y] = pixel

    return translated_image
