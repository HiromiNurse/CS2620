# from PIL import Image
# from os import listdir


# class balls:
#     def __init__(self):
#         self.image = Image.open("skibidi.jpg")
#         self.width = self.image.width
#         self.height = self.image.height

#     def balls2(self):
#         self.image = self.image.convert("RGB")
#         data = self.image.load()

#         # Make GUI friendly
#         # Make menu to select qrcode?
#         qr_code_list = [f for f in listdir() if "qr" in f]
#         qr_code_number = 0

#         for qr in qr_code_list:
#             print(f"{qr_code_number}: {qr}")
#             qr_code_number += 1
#         qr_input = int(input("Selected QR Code: "))
#         qr_code = Image.open(qr_code_list[qr_input])
#         qr_data = qr_code.load()

#         if qr_code.size > self.image.size:
#             # Make GUI friendly
#             print("QR code to large.")
#         else:
#             qr_bits = (qr_code.width - 4) * (qr_code.height - 4)
#             cooldown = (qr_bits + 16) // (self.width * self.height)

#             qr_bin = bin(qr_bits)[2:]
#             qrx_pos = 0
#             qry_pos = 0
#             for i in qr_bin:
#                 if qrx_pos < self.width:
#                     r, g, b = data[qrx_pos, qry_pos]
#                 else:
#                     qry_pos += 1
#                     qrx_pos = qrx_pos - self.width
#                     r, g, b = data[qrx_pos, qry_pos]

#                 r &= 254
#                 g &= 254
#                 b &= 254
#                 r |= int(i)
#                 g |= int(i)
#                 b |= int(i)
#                 data[qrx_pos, qry_pos] = (r, g, b)

#                 qrx_pos += cooldown

#             x_pos = 0
#             y_pos = 0
#             current_count = 0
#             size_corrector = (qry_pos * self.width) + qrx_pos
#             passes = 0
#             encoded_bits = 0

#             for y in range(self.height):
#                 for x in range(self.width):
#                     if passes > size_corrector:
#                         if encoded_bits >= qr_bits:
#                             if current_count == cooldown:
#                                 current_count = 0
#                                 r, g, b = data[x, y]
#                                 r &= 254
#                                 g &= 254
#                                 b &= 254
#                                 if qr_data[x_pos, y_pos] < 128:
#                                     # add 0 to the end of the binary numbers
#                                     r |= 0
#                                     g |= 0
#                                     b |= 0
#                                 else:
#                                     # add 1 to the end of the binary number r
#                                     r |= 1
#                                     g |= 1
#                                     b |= 1
#                                 data[x, y] = (r, g, b)
#                                 if x_pos < self.width:
#                                     x_pos += 1
#                                 else:
#                                     y_pos += 1
#                                     x_pos = 0
#                             else:
#                                 current_count += 1
#                     else:
#                         passes += 1



# tester = balls()
# tester.balls2()

# def BinaryToDecimal(binary): 
#     binary1 = binary 
#     decimal, i, n = 0, 0, 0
#     while(binary != 0): 
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i) 
#         binary = binary//10
#         i += 1
#     return (decimal) 

# text = "testing testing"
# print("Text:" + text)
# res = ''.join(format(ord(i), '08b') for i in text)
# print("Binary:" + str(res))
# str_data = ''
# for i in range(0, len(res), 8):
#     temp_data = int(res[i : i + 8])
#     decimal_data = BinaryToDecimal(temp_data)
#     str_data += chr(decimal_data)

# print("After:" + str_data)

# from image_functions import WorkingImage
from PIL import Image

from image_functions import WorkingImage

#
# image1 = WorkingImage("goblin.jpg")
# image1.stringEncoder()
# image1.save("STRIN!!NG!GN")#
#
# def color_distance(one, two):
#     r_diff = one[0] - two[0]
#     g_diff = one[1] - two[1]
#     b_diff = one[2] - two[2]
#
#     return abs(r_diff) + abs(g_diff) + abs(b_diff)
#
# def dithering():
#     image = Image.open("minion.jpg")
#     data = image.load()
#
#     error_matrix = []
#     for x in range(image.width+1):
#         row = []
#         for y in range(image.height+1):
#             row.append(0)
#         error_matrix.append(row)
#
#     for y in range(image.height):
#         for x in range(image.width):
#             pixel = data[x, y]
#             k = (pixel[0] + pixel[1] + pixel[2]) // 3
#
#             k += error_matrix[x][y]
#
#             out = 0
#             if k >= 128:
#                 out = 255
#
#             data[x, y] = (out, out, out)
#
#             error = k - out
#             # quarter_error = error / 4
#             error_matrix[x + 1][y] += error / 3
#             error_matrix[x - 1][y + 1] += error / 6
#             error_matrix[x][y + 1] += error / 3
#             error_matrix[x + 1][y + 1] += error / 6
#
#     image.save("GrayscaleMinion.png")
#
#
# def remap_dither(image, data, palette, filename):
#     palette_distances = []
#     for color1 in palette:
#         row = []
#         for color2 in palette:
#             distance = color_distance(color1, color2)
#             row.append(distance)
#         palette_distances.append(row)
#
#     error_matrix = []
#     for x in range(image.width+1):
#         row = []
#         for y in range(image.height+1):
#             row.append(0)
#         error_matrix.append(row)
#
#     for y in range(image.height):
#         for x in range(image.width):
#             pixel = data[x, y]
#             error = error_matrix[x][y]
#             pixel = (pixel[0] + error[0], pixel[1] + error[1], pixel[2] + error[2])
#             min_distance = 442
#             min_index = 0
#             for i, color in enumerate(palette):
#
#                 palette_distance = palette_distances[min_index][i]
#                 if palette_distance > min_distance * 2:
#                     continue
#
#                 distance = color_distance(color, pixel)
#                 if distance < min_distance:
#                     min_distance = distance
#                     min_index = i
#
#             data[x, y] = palette[min_index]
#
#             error = (pixel[0] - data[x, y][0], pixel[1] - data[x, y][1], pixel[2] - data[x, y][2])
#
#             error_matrix[x + 1][y] = (
#             error_matrix[x + 1][0] + error[0] * 0.25, error_matrix[x + 1][1] + error[1] * 0.25,
#             error_matrix[x + 1][1] + error[1] * 0.25)
#
#             error_matrix[x - 1][y+1] = (
#             error_matrix[x - 1][y+1][0] + error[0] * 0.25, error_matrix[x - 1][y+1][1] + error[1] * 0.25,
#             error_matrix[x - 1][y+1][1] + error[1] * 0.25)
#
#             error_matrix[x][y+1] = (
#             error_matrix[x][y+1][0] + error[0] * 0.25, error_matrix[x][y+1][1] + error[1] * 0.25,
#             error_matrix[x][y+1][1] + error[1] * 0.25)
#
#             error_matrix[x + 1][y + 1] = (
#             error_matrix[x + 1][y + 1][0] + error[0] * 0.25, error_matrix[x + 1][y + 1][1] + error[1] * 0.25,
#             error_matrix[x + 1][y + 1][1] + error[1] * 0.25)
#
#     image.save(filename)
#
# remap_dither(Image.open("minion.jpg"), Image.open("minion.jpg").load(), )
# #### BrOKY

# text = input('Hidden Text: ').strip()
# ascii_code = ''.join(format(ord(i), '08b') for i in text)
# print(ascii_code)

hidetest = WorkingImage("minion.jpg")
hidetest.stringEncoder()
hidetest.save("Encoded_minion")
hidetest.readString()

# number = 115200
# bin_num = bin(number)
# number1 = int(bin_num, 2)
# print(number, bin_num, number1, type(number))
