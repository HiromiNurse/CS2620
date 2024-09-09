from PIL import Image


def greyscale_Corrected(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscalec_value = int((red*.21)+(green*.71)+(blue*.08)) // 3
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
            greyscale_value = (red+green+blue) // 3
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
            greyscale_value = (red+green+blue) // 3
            if red > 65 and (red-green) > 15 and (red-blue) > 25 and red > greyscale_value:
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
            greyscale_value = (red+green+blue) // 3
            if green > 45 and (green-red) > 15 and (green-blue) > 15 and green > greyscale_value:
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
            greyscale_value = (red+green+blue) // 3
            if blue > 65 and (blue-green) > 15 and (blue-red) > 25 and blue > greyscale_value:
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
            data[image.width-x-1, y] = (red, green, blue)
    return image

def xAxisMirrorR(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if x >= (image.width//2):
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
            data[x, image.height-1 - y] = (red, green, blue)
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
                data[x, image.height-1-y] = (red, green, blue)
    return image

def diagonalMirrorT(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            data[x,y] = data[y,x]
    return image

def colorInvert(image):
    data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            data[x, y] = (255-red, 255-green, 255-blue)
    return image

def xAxisFlip(image):
    data = image.load()
    for y in range(image.height):
        x_pixels = []
        for x in range(image.width):
            pixel = data[x, y]
            x_pixels.append(pixel)
        for x in range(image.width):
            data[x, y] = x_pixels[image.width-x-1]  
    return image

def yAxisFlip(image):
    data = image.load()
    for x in range(image.width):
        y_pixels = []
        for y in range(image.height):
            pixel = data[x, y]
            y_pixels.append(pixel)
        for y in range(image.height):
            data[x, y] = y_pixels[image.height-y-1]
    return image

def flipDiagonal(image):
    data = image.load()

    return image

def rotateClockwise(image):
    data = image.load()
    rotated_image = Image.new(mode="RGB", size=(image.height, image.width))
    rotated_image_data = rotated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            rotated_image_data[rotated_image.width-1-y, x] = pixel
    return image

def rotateCClockwise(image):
    data = image.load()
    rotated_image = Image.new(mode="RGB", size=(image.height, image.width))
    rotated_image_data = rotated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            rotated_image_data[y, image.width - 1 - x] = pixel
    return image
