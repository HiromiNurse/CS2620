from PIL import Image
from math import radians, cos, sin
from gaussian_Blur import *
from os import listdir
import math


class WorkingImage:
    def __init__(self, name="image.jpg"):
        self.image = Image.open(name)
        self.width = self.image.width
        self.height = self.image.height


    def corrected_greyscale(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]
                greyscale_value = int((r * .21) + (g * .71) + (b * .08)) // 3
                data[x, y] = (greyscale_value, greyscale_value, greyscale_value)


    def greyscale(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]
                greyscale_value = int(r + g + b) // 3
                data[x, y] = (greyscale_value, greyscale_value, greyscale_value)


    def isolateRed(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]

                greyscale_value = int(r + g + b) // 3

                if r> 65 and (r- g) > 15 and (r- b) > 25 and r> greyscale_value:
                    data[x, y] = (r, g, b)
                else:
                    data[x, y] = (greyscale_value, greyscale_value, greyscale_value)


    def isolateGreen(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]

                greyscale_value = int(r + g + b) // 3

                if g > 45 and (g - r) > 15 and (g - b) > 15 and g > greyscale_value:
                    data[x, y] = (r, g, b)
                else:
                    data[x, y] = (greyscale_value, greyscale_value, greyscale_value)


    def isolateBlue(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]

                greyscale_value = int(r + g + b) // 3

                if b > 65 and (b - g) > 15 and (b - r) > 25 and b > greyscale_value:
                    data[x, y] = (r, g, b)
                else:
                    data[x, y] = (greyscale_value, greyscale_value, greyscale_value)


    def leftToRightMirror(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]
                data[self.width - x - 1, y] = (r, g, b)

    def rightToLeftMirror(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]
                if x >= (self.width // 2):
                    data[self.width - 1 - x, y] = (r, g, b)

    def topToBottomMirro(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]
                data[x, self.height - 1 - y] = (r, g, b)

    def bottomToTopMirror(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]
                if y >= (self.height // 2):
                    data[x, self.height - 1 - y] = (r, g, b)


    def bottomToTopDiagonalMirror(self):
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                if x >= self.width // 2 and y >= self.height // 2:
                    data[x, y] = data[self.width - x - 1, self.height - 1 - y]

    def topToBottomDiagonalMirror(self):
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                if x <= self.width // 2 and y <= self.height // 2:
                    data[x, y] = data[self.width - x - 1, self.height - 1 - y]

    def flipXAxis(self):
        data = self.image.load()
        new_image = Image.new("RGB", size=(self.width, self.height))
        new_data = new_image.load()
        for y in range(self.height):
            for x in range(self.width):
                new_data[x, y] = data[self.width - x - 1, y]
        self.image = new_image


    def flipYAxis(self):
        data = self.image.load()
        new_image = Image.new("RGB", size=(self.width, self.height))
        new_data = new_image.load()
        for y in range(self.height):
            for x in range(self.width):
                new_data[x, y] = data[x, self.height - y - 1]

    def flipDiagonal(self):
        self.flipXAxis
        self.flipYAxis


    def invertColors(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = data[x, y]
                data[x, y] = (255 - r, 255 - g, 255 - b)

    def rotate90Clockwise(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        new_image = Image.new("RGB", size=(self.height, self.width))
        new_data = new_image.load()
        for y in range(self.height):
            for x in range(self.width):
                new_data[x, y] = data[x, self.height - y - 1]
        self.image = new_image

    def rotate90CounterClockiwse(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()
        new_image = Image.new("RGB", size=(self.height, self.width))
        new_data = new_image.load()
        for y in range(self.height):
            for x in range(self.width):
                new_data[x, y] = data[self.width - 1 - x, y]
        self.image = new_image

    def rotateAndEnlarge(self):
        self.image = self.image.convert("RGBA")
        data = self.image.load()

        angle = int(input()) # Change Later to accomodate gui
        radian_angle = radians(angle)

        cosine = cos(-radian_angle)
        sine = sin(-radian_angle)

        new_width = int(abs(self.width * -cosine) + abs(self.height * -sine))
        new_height = int(abs(self.height * -cosine) + abs(self.width * -sine))

        new_image = Image.new("RGBA", size=(new_width, new_height))
        new_data = new_image.load()

        x_center, y_center = self.width // 2, self.height // 2
        new_x_center, new_y_center = new_width // 2, new_height // 2

        for y in range(self.height):
            for x in range(self.width):
                x_old = int((x - new_x_center) * cosine - (y - new_y_center) * sine + x_center)
                y_old = int((x - new_x_center) * sine - (y - new_y_center) * cosine + y_center)

                if 0 <= x_old < self.width and 0 <= y_old < self.height:
                    new_data[x, y] = data[x_old, y_old]

        self.image = new_image

    def rotateAndCrop(self):
        self.image = self.image.convert("RGBA")
        aspect_ratio = self.width / self.height

        angle = int(input()) # Change Later to accomodate gui
        radian_angle = radians(angle)

        self.image = self.image.rotate(angle, expand=False)
        # Fix / make own code
        # new_width, new_height = rotated_image.size
        #
        # cos_angle = abs(cos(angle_radians))
        # sin_angle = abs(sin(angle_radians))
        #
        # new_w = width * cos_angle + height * sin_angle
        # new_h = height * cos_angle + width * sin_angle
        #
        # crop_w = int(min(new_w, new_h * aspect_ratio))
        # crop_h = int(min(new_h, new_w / aspect_ratio))
        #
        # left = (new_width - crop_w) // 2
        # right = left + crop_w
        # top = (new_height - crop_h) // 2
        # bottom = top + crop_h
        #
        # final_product = rotated_image.crop((left, top, right, bottom))

    def rotateAboutCenter(self):
        self.image = self.image.convert("RGBA")
        data = self.image.load()

        angle = int(input())  # Change Later to accomodate gui
        radian_angle = radians(angle)

        cosine = cos(-radian_angle)
        sine = sin(-radian_angle)

        new_image = Image.new("RGBA", size=(self.width, self.height))
        new_data = new_image.load()

        x_center, y_center = self.width // 2, self.height // 2

        for y in range(self.height):
            for x in range(self.width):
                x_old = int((x - x_center) * cosine - (y - y_center) * sine + x_center)
                y_old = int((x - x_center) * sine - (y - y_center) * cosine + y_center)

                if 0 <= x_old < self.width and 0 <= y_old < self.height:
                    new_data[x, y] = data[x_old, y_old]


    def rotateAboutPoint(self):
        self.image = self.image.convert("RGBA")
        data = self.image.load()

        x_origin = int(input("X coord to rotate about: "))
        y_origin = int(input("Y coord to rotate about: "))

        self.image = self.image.convert("RGBA")

        angle = int(input())  # Change Later to accomodate gui
        radian_angle = radians(angle)

        cosine = cos(-radian_angle)
        sine = sin(-radian_angle)

        new_width = int(abs(self.width * -cosine) + abs(self.height * -sine))
        new_height = int(abs(self.height * -cosine) + abs(self.width * -sine))

        new_image = Image.new("RBGA", size = (new_width, new_height))
        new_data = new_image.load()

        x_center, y_center = self.width // 2 + x_origin, self.height // 2 + y_origin
        new_x_center, new_y_center = new_width // 2, new_height // 2

        for y in range(self.height):
            for x in range(self.width):
                x_old = int((x - new_x_center) * cosine - (y - new_y_center) * sine + x_center)
                y_old = int((x - new_x_center) * sine + (y - new_y_center) * cosine + y_center)

                if 0 <= x_old < self.width and 0 <= y_old < self.height:
                    new_data[x, y] = data[x_old, y_old]

    def arbitraryTranslation(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()

        dx = int(input("Change in x: ")) # Change for GUI input
        dy = int(input("Change in y: ")) # Change for GUI input

        new_image = Image.new("RGB", size=(self.width+dx, self.height+dy))
        new_data = new_image.load()

        for y in range(new_image.height):
            for x in range(new_image.width):
                new_x = x - dx
                new_y = y - dy

                if 0 >= new_x < new_image.width and 0 >= new_y < new_image.height:
                    new_data[x, y] = data[new_x, new_y]
                else:
                    new_data[x, y] = (0, 0, 0)
        self.image = new_image


    def arbitraryTransformation(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()

        # In GUI, add in matrix form
        a = int(input("x scale: "))  # x scale
        b = int(input("x rotation: "))  # x rotation
        cin = str(input("x translation: "))  # x translation
        d = int(input("y rotation: "))  # y rotation
        e = int(input("y scale: "))  # y scale
        fin = str(input("y translation: "))  # y translation
        # Refactor later to use in GUI

        if cin.strip().lower() == "width":
            c = int(self.image.width - 1)
        elif cin.strip().lower() == "height":
            c = int(self.image.height - 1)
        if fin.strip().lower() == "height":
            f = int(self.image.height - 1)
        elif fin.strip().lower() == "width":
            f = int(self.image.width - 1)

        new_image = Image.new("RGB", size=(self.width, self.height))
        new_data = new_image.load()

        for y in range(self.height):
            for x in range(self.width):
                new_x = x * a + y * b + c
                new_y = x * d + y * e + f

                # Make sure the pulling works as intended and is not backward
                new_data[x, y] = data[new_x, new_y]


    def scale(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()

        # Make GUI compatable
        scale_factor = int(input("Scale Factor: "))

        new_image = Image.new("RGB", size=(int(self.width * scale_factor), int(self.height * scale_factor)))
        new_data = new_image.load()

        for y in range(self.height):
            for x in range(self.width):
                new_x = int(x / scale_factor)
                new_y = int(y / scale_factor)

                new_data[x, y] = data[new_x, new_y]

    def blur(self):
        blur_factor = float(input("Blur amount: "))
        kernel_size = int(input("Kernel size: "))
        kernel = gaussian_kernel(kernel_size, blur_factor)

        new_image_array = applyKernel(self.image, kernel)

        self.image = Image.fromarray(new_image_array)

    def blurNoPadding(self):
        blur_factor = float(input("Blur amount: "))
        kernel_size = int(input("Kernel size: "))
        kernel = gaussian_kernel(kernel_size, blur_factor)

        new_image_array = applyKernelNoPadding(self.image, kernel)

        self.image = Image.fromarray(new_image_array)

    def customKernelApplicator(self):
        # Transfer this function here with gui support
        kernel = kernelShenanigan()

        new_image_array = applyKernel(self.image, kernel)

        self.image = Image.fromarray(new_image_array)

    def qr_code_simplifier(self):
        # Change to GUI dropdown maybe?
        qr_code_list = [f for f in listdir() if "qr" in f]
        qr_code_number = 0

        for qr in qr_code_list:
            print(f"{qr_code_number}: {qr}")
            qr_code_number += 1
        qr_input = int(input("Selected QR Code: "))
        qr_code = Image.open(qr_code_list[qr_input])

        print("Select Qr code version (1 - 40): "
              "\nVersion 1: 21x21"
              "\nVersion2: 25x25"
              "\nVersionN: (4 x N) + 17")
        new_size = (int(input("Enter QR code version (version = [X - 23] / 4) (1-40): ")) * 4) + 21

        qr_code.convert("L")
        qr_code.thumbnail((new_size, new_size))

        qr_data = qr_code.load()

        for y in range(new_size):
            for x in range(new_size):
                if qr_data[x, y] < 128:
                    qr_data[x, y] = 0
                else:
                    qr_data[x, y] = 255

    def qrCodeReader(self):
        self.image = self.image.convert("RGBA")
        data = self.image.load()

        qr_bits = # Make it so it reads the first 16 bits to get the qr code size
        qr_size = math.sqrt(qr_bits) + 16

        qr_code = Image.new("RGB", size=(qr_size, qr_size))
        qr_data = qr_code.load()

        for y in range(self.image.height):
            for x in range(self.image.width):
                r, g, b = data[x, y]
                if (g & 1) == 1:
                    qr_data[x, y] = (0, 0, 0)
                else:
                    qr_data[x, y] = (255, 255, 255)
        qr_code.save("qr_code.png")
        qr_code.show()

    def qrCodeEncoder(self):
        self.image = self.image.convert("RGB")
        data = self.image.load()

        # Make GUI friendly
        # Make menu to select qrcode?
        qr_code_list = [f for f in listdir() if "qr" in f]
        qr_code_number = 0

        for qr in qr_code_list:
            print(f"{qr_code_number}: {qr}")
            qr_code_number += 1
        qr_input = int(input("Selected QR Code: "))
        qr_code = Image.open(qr_code_list[qr_input])
        qr_data = qr_code.load()

        if qr_code.size > self.image.size:
            # Make GUI friendly
            print("QR code to large.")
        else:
            qr_bits = (qr_code.width - 4) * (qr_code.height - 4)
            cooldown = (qr_bits + 16) // (self.width * self.height)

            qr_bin = bin(qr_bits)[2:]
            qrx_pos = 0
            qry_pos = 0
            for i in qr_bin:
                if qrx_pos < self.width:
                    r, g, b = data[qrx_pos, qry_pos]
                else:
                    qry_pos += 1
                    qrx_pos = qrx_pos - self.width
                    r, g, b = data[qrx_pos, qry_pos]

                r &= 254
                g &= 254
                b &= 254
                r |= int(i)
                g |= int(i)
                b |= int(i)
                data[qrx_pos, qry_pos] = (r, g, b)

                qrx_pos += cooldown

            x_pos = 0
            y_pos = 0
            current_count = 0
            size_corrector = (qry_pos * self.width) + qrx_pos
            passes = 0 # Fix so it always writes 16 bits
            encoded_bits = 0

            for y in range(self.height):
                for x in range(self.width):
                    if passes > size_corrector:
                        if encoded_bits >= qr_bits:
                            if current_count == cooldown:
                                current_count = 0
                                r, g, b = data[x, y]
                                r &= 254
                                g &= 254
                                b &= 254
                                if qr_data[x_pos, y_pos] < 128:
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
                                if x_pos < self.width:
                                    x_pos += 1
                                else:
                                    y_pos += 1
                                    x_pos = 0
                            else:
                                current_count += 1
                    else:
                        passes += 1

    def stringEncoder(self):
        # Encode a string in the least siginificant bit of an image
        pass

    def colorReducer(self):
        data = self.image.load()

    def deconvoluter(self):
        data = self.image.load()

    def seamCarvedResize(self):
        data = self.image.load()
