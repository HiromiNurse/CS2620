from PIL import Image
from math import radians, cos, sin
from gaussian_Blur import *
from os import listdir


class working_image:
    def __init__(self, name="image.jpg"):
        self.image = Image.open(name)
        self.width = self.image.width
        self.height = self.image.height

    def corrected_greyscale(self):
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x,y]
                greyscale_value = int((r * .21) + (g * .71) + (b * .08)) // 3

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
    return_image = Image.new("RGB", size=(image.width, image.height))
    return_data = return_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscale_value = (red + green + blue) // 3
            return_data[x, y] = (greyscale_value, greyscale_value, greyscale_value)
    return return_image


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
    image = image.convert("RGBA")
    width, height = image.size
    angle = int(input("Rotation amount (in degrees):"))
    angle_radians = radians(angle)
    
    cosine = cos(-angle_radians)
    sine = sin(-angle_radians)

    new_width = int(abs(width * -cosine) + abs(height * -sine))
    new_height = int(abs(height * -cosine) + abs(width * -sine))

    rotated_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
    pixels_new = rotated_image.load()

    xCenter, yCenter = width // 2, height // 2
    xCenterNew, yCenterNew = new_width // 2, new_height // 2

    for y in range(new_height):
        for x in range(new_width):
            x_old = int((x - xCenterNew) * cos(-angle_radians) - (y - yCenterNew) * sin(-angle_radians) + xCenter)
            y_old = int((x - xCenterNew) * sin(-angle_radians) + (y - yCenterNew) * cos(-angle_radians) + yCenter)

            if 0 <= x_old < width and 0 <= y_old < height:
                pixels_new[x, y] = image.getpixel((x_old, y_old))

    return rotated_image


def how_did_this_happen(image):
    image = image.convert("RGBA")
    width, height = image.size
    angle = int(input("Rotation amount (in degrees):"))
    angle_radians = radians(angle)

    cosine = cos(-angle_radians)
    sine = sin(-angle_radians)

    new_width = int(abs(width * -cosine) + abs(height * -sine))
    new_height = int(abs(width * -cosine) + abs(height * -sine))

    rotated_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
    pixels_new = rotated_image.load()

    xCenter, yCenter = width // 2, height // 2
    xCenterNew, yCenterNew = new_width // 2, new_height // 2

    for y in range(new_height):
        for x in range(new_width):
            x_old = int((x - xCenterNew) * cosine - (y - yCenterNew) * sine + xCenter)
            y_old = int((x - xCenterNew) * sine - (y - yCenterNew) * cosine + xCenter)

            if 0 <= x_old < width and 0 <= y_old < height:
                pixels_new[x, y] = image.getpixel((x_old, y_old))

    return rotated_image


# Rotates and only keeps the original size of the image
def rotateCutoff(image):
    width, height = image.size
    angle = int(input("Rotation angle in degrees: "))
    angle_radians = radians(angle)

    rotated_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    pixels_new = rotated_image.load()

    cosine = cos(-angle_radians)
    sine = sin(-angle_radians)

    xCenter, yCenter = width // 2, height // 2
    for y in range(height):
        for x in range(width):
            x_old = int((x - xCenter) * cosine - (y - yCenter) * sine + xCenter)
            y_old = int((x - xCenter) * sine + (y - yCenter) * cosine + yCenter)

            if 0 <= x_old < width and 0 <= y_old < height:
                pixels_new[x, y] = image.getpixel((x_old, y_old))

    return rotated_image


# Rotates and takes the smallest window fitting all of image
def rotateSmallest(image):
    image.convert("RGBA")
    width, height = image.size
    aspect_ratio = width / height

    angle = int(input("Rotation angle in degrees: "))
    angle_radians = radians(angle)

    rotated_image = image.rotate(angle, expand=True, fillcolor = (0, 0, 0, 0))
    new_width, new_height = rotated_image.size

    cos_angle = abs(cos(angle_radians))
    sin_angle = abs(sin(angle_radians))

    new_w = width * cos_angle + height * sin_angle
    new_h = height * cos_angle + width * sin_angle

    crop_w = int(min(new_w, new_h * aspect_ratio))
    crop_h = int(min(new_h, new_w / aspect_ratio))

    left = (new_width - crop_w) // 2
    right = left + crop_w
    top = (new_height - crop_h) // 2
    bottom = top + crop_h

    final_product = rotated_image.crop((left, top, right, bottom))

    return final_product


def rotationAbout(image):
    originx = int(input("X coord to rotate about: "))
    originy = int(input("Y coord to rotate about: "))
    image = image.convert("RGBA")
    width, height = image.size
    angle = int(input("Rotation amount (in degrees):"))
    angle_radians = radians(angle)
    
    cosine = cos(-angle_radians)
    sine = sin(-angle_radians)

    new_width = int(abs(width * -cosine) + abs(height * -sine))
    new_height = int(abs(height * -cosine) + abs(width * -sine))

    rotated_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
    pixels_new = rotated_image.load()

    xCenter, yCenter = width // 2 + originx, height // 2 + originy
    xCenterNew, yCenterNew = new_width // 2, new_height // 2

    for y in range(new_height):
        for x in range(new_width):
            x_old = int((x - xCenterNew) * cos(-angle_radians) - (y - yCenterNew) * sin(-angle_radians) + xCenter)
            y_old = int((x - xCenterNew) * sin(-angle_radians) + (y - yCenterNew) * cos(-angle_radians) + yCenter)

            if 0 <= x_old < width and 0 <= y_old < height:
                pixels_new[x, y] = image.getpixel((x_old, y_old))

    return rotated_image


def translation(image):
    data = image.load()
    dx = int(input("Change in x: "))
    dy = int(input("Change in y: "))
    translated_image = Image.new("RGB", size=((image.width + dx), (image.height + dy)))
    new_data = translated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            new_data[x + dx, y + dy] = pixel
    return translated_image


def scale(image):
    data = image.load()
    scaleSize = int(input("Scale Amount: "))
    new_image = Image.new("RGB", size=(int(image.width * scaleSize), int(image.height * scaleSize)))
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
    a = int(input("x scale: ")) # x scale
    b = int(input("x rotation: ")) # x rotation
    cin = str(input("x translation: ")) # x translation
    d = int(input("y rotation: ")) # y rotation
    e = int(input("y scale: ")) # y scale
    fin = str(input("y translation: ")) # y translation

    if cin.strip().lower() == "width":
        c = int(image.width - 1)
    elif cin.strip().lower() == "height":
        c = int(image.height - 1)
    if fin.strip().lower() == "height":
        f = int(image.height - 1)
    elif fin.strip().lower() == "width":
        f = int(image.width - 1)
    translated_image = Image.new("RGB", size=(image.width, image.height))
    new_data = translated_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]

            new_x = x * a + y * b + c
            new_y = x * d + y * e + f

            new_data[new_x, new_y] = pixel

    return translated_image


def blurFunction(image):
    fuzzyness = float(input("Blur amount: "))
    kernel_size = int(input("Kernel size: "))
    kernel = gaussian_kernel(kernel_size, fuzzyness)

    blurredImageArray = applyKernel(image, kernel)

    return Image.fromarray(blurredImageArray)


def blurFunctionNP(image):
    fuzzyness = float(input("Blur amount: "))
    kernel_size = int(input("Kernel size: "))
    kernel = gaussian_kernel(kernel_size, fuzzyness)

    blurredImageArray = applyKernelNoPadding(image, kernel)

    return Image.fromarray(blurredImageArray)

def customKernel(image):
    kernel = kernelShenanigan()

    kerneled_Image_Array = applyKernel(image, kernel)

    return Image.fromarray(kerneled_Image_Array)

"""
Function: Converts given qr code to a 1 pixel per bit version
"""
def qr_code_simplifier():
    qr_code_list = [f for f in listdir() if "qr" in f]
    qr_code_number = 0
    print("Which QR code needs to be simplified?")
    for qr in qr_code_list:
        print(f"{qr_code_number}: {qr}")
        qr_code_number += 1
    qr_input = int(input("Selected QR Code: "))
    image = Image.open(qr_code_list[qr_input])

    new_size = (int(input("Enter QR code version (version = [X - 23] / 4) (1-40): ")) * 4) + 21
    image = image.convert("L")
    image.thumbnail((new_size, new_size))
    data = image.load()

    for y in range(new_size):
        for x in range(new_size):
            if data[x, y] < 128:
                data[x, y] = 0
            else:
                data[x, y] = 255

    image.save("qrcode.png")

"""
Fucntion: Reads qr codes from image made with hide_qr_linear
"""
def qr_read():
    image = Image.open("encoded_image.png")
    data = image.load()
    width, height = image.size

    qrCode = Image.new("RGB", (width, height))
    qrData = qrCode.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = data[x, y]
            if (g & 1) == 1:
                qrData[x, y] = (0, 0, 0)
            else:
                qrData[x, y] = (255, 255, 255)
    return qrCode

"""
Function: Writes qr codes into an image in a line with an
arbitrary spacing by writing into the last bit of rgb channels
"""
def hide_Qr_Linear(image):
    qrImage = Image.open("qrcode.png")
    qrData = qrImage.load()
    data = image.load()

    width, height = qrImage.size
    if qrImage.size > image.size:
        print("QR code to large.")
        return

    x_pixel = 0
    y_pixel = 0
    cooldown = 5
    for y in range(image.height):
        for x in range(image.width):
            if cooldown == 0:
                cooldown = 5
                if x_pixel < width:
                    x_pixel += 1
                else:
                    y_pixel += 1
                    x_pixel = 0
            else:
                cooldown -= 1

            r, g, b = data[x, y]
            r &= 254
            g &= 254
            b &= 254
            if 0 <= x_pixel < width and 0 <= y_pixel < height:
                pixel_brightness = qrData[x_pixel, y_pixel]
                if pixel_brightness < 128:
                    # add 0 to the end of the binary numbers
                    r |= 0
                    g |= 0
                    b |= 0
                else:
                    # add 1 to the end of the binary number r
                    r |= 1
                    g |= 1
                    b |= 1
            data[x, y] = (r, g, b)
    return image

"""
Legacy versions of the qr code hider and reader
"""
# def hideQR(image):
#     qrImage = Image.open("qrcode.png")
#     qrData = qrImage.load()
#     data = image.load()

#     width, height = qrImage.size
#     if qrImage.size > image.size:
#         print("QR code to large.")
#         return

#     for y in range(image.height):
#         for x in range(image.width):
#             r, g, b = data[x, y]
#             r &= 254
#             g &= 254
#             b &= 254
#             if 0 <= x < height and 0 <= y < height:
#                 qr, qg, qb = qrData[x, y]
#                 if qg < 100 and qr < 100 and qb < 100:
#                     # add 0 to the end of the binary numbers
#                     r |= 0
#                     g |= 0
#                     b |= 0
#                 else:
#                     # add 1 to the end of the binary number r
#                     r |= 1
#                     g |= 1
#                     b |= 1
#             data[x, y] = (r, g, b)
#     return image


# def decodeQR():
#     image = Image.open("encoded_image.png")
#     data = image.load()
#     width, height = image.size

#     qrCode = Image.new("RGB", (width, height))
#     qrData = qrCode.load()

#     for y in range(image.height):
#         for x in range(image.width):
#             r, g, b = data[x, y]
#             if (g & 1) == 1:
#                 qrData[x, y] = (0, 0, 0)
#             else:
#                 qrData[x, y] = (255, 255, 255)
#     return qrCode


# Color Reduction. Reduce the number of colors on the image
# Instead fo (255, 0, 0) and (254, 0, 0) just use the first
def color_reduction(image):
    pass


# Richardson–Lucy deconvolution
def deconvolution(image):
    pass


# Seam carving algorithm
# Resizes cutting out un-important sections
def seam_carved_resize(image):
    pass