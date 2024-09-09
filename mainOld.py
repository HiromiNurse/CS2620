from PIL import Image
from os import listdir

def change_image(change_type, image, data):
    match change_type:
        case '0':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    data[x, y] = (red, green, blue)
            image.save("image_out.png")
        case '1':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    greyscalec_value = int((red*.21)+(green*.71)+(blue*.08)) // 3
                    data[x, y] = (greyscalec_value, greyscalec_value, greyscalec_value)
            image.save("image_out.png")
        case '2':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    greyscale_value = (red+green+blue) // 3
                    data[x, y] = (greyscale_value, greyscale_value, greyscale_value)
            image.save("image_out.png")
        case '3':
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
            image.save("image_out.png")
        case '4':
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
            image.save("image_out.png")
        case '5':
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
            image.save("image_out.png")
        case '6':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    data[x, y] = (255-red, 255-green, 255-blue)
            image.save("image_out.png")
        case '7':
            for y in range(image.height):
                for x in range(image.width):
                    data[x, y] = (5, 6, 7)
            image.save("image_out.png")
        case '8':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    data[image.width-x-1, y] = (red, green, blue)
            image.save("image_out.png")
        case '9':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    if x >= (image.width//2):
                        data[image.width - 1 - x, y] = (red, green, blue)
            image.save("image_out.png")
        case '10':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    data[x, image.height-1 - y] = (red, green, blue)
            image.save("image_out.png")
        case '11':
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    if y >= (image.height // 2):
                        data[x, image.height-1-y] = (red, green, blue)
            image.save("image_out.png")
        case '12':
            for y in range(image.height):
                x_pixels = []
                for x in range(image.width):
                    pixel = data[x, y]
                    x_pixels.append(pixel)
                for x in range(image.width):
                    data[x, y] = x_pixels[image.width-x-1]
            image.save("image_out.png")
        case '13':
            for x in range(image.width):
                y_pixels = []
                for y in range(image.height):
                    pixel = data[x, y]
                    y_pixels.append(pixel)
                for y in range(image.height):
                    data[x, y] = y_pixels[image.height-y-1]
            image.save("image_out.png")
        case '14':
            for y in range(image.height):
                x_pixels = []
                for x in range(image.width):
                    pixel = data[x, y]
                    x_pixels.append(pixel)
                for x in range(image.width):
                    data[x, y] = x_pixels[image.width-x-1]
            for x in range(image.width):
                y_pixels = []
                for y in range(image.height):
                    pixel = data[x, y]
                    y_pixels.append(pixel)
                for y in range(image.height):
                    data[x, y] = y_pixels[image.height-y-1]
            image.save("image_out.png")
        case '15':
            rotated_image = Image.new(mode="RGB", size=(image.height, image.width))
            rotated_image_data = rotated_image.load()
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    rotated_image_data[rotated_image.width-1-y, x] = pixel
            rotated_image.save("image_out.png")
        case '16':
            rotated_image = Image.new(mode="RGB", size=(image.height, image.width))
            rotated_image_data = rotated_image.load()
            for y in range(image.height):
                for x in range(image.width):
                    pixel = data[x, y]
                    rotated_image_data[y, image.width - 1 - x] = pixel
            rotated_image.save("image_out.png")
    quit()


def main_menu():
    print("What kind of change would you like to make?")
    image_list = [f for f in listdir() if ".jpg" in f]
    image_list.append("Quit")
    image_number = 0
    for image in image_list:
        print(f"{image_number}: {image}")
        image_number += 1

    selected_image_number = int(input("Input the number corresponding to the image name: "))
    selected_image = image_list[selected_image_number]
    if image_list[selected_image_number] == "Quit":
        quit()
    image = Image.open(selected_image)
    data = image.load()

    print(f"Selected Image: {selected_image}")
    print("What kind of change would you like to make?")

    options_list = ["Normal", "Greyscale corrected", "Greyscale", "Color Isolation Red",
                    "Color Isolation Green", "Color Isolation Blue", "Invert", "Blind Filter",
                    "X-axis Mirror (Left)", "X-axis Mirror (Right)", "Y-axis Mirror (Top)",
                    "Y-axis Mirror (Bottom)", "Flip X-axis", "Flip Y-axis", "Flip Diagonal",
                    "Rotate 90(Clockwise)", "Rotate 90(Counter-Clockwise)",
                    "Quit/q"]
    column_height = len(options_list)//3
    extra_options = len(options_list) % 3
    if extra_options == 0:
        for i in range(0, len(options_list) // 3):
            print(f"{i:3}: {options_list[i]:25}{(i+column_height):3}: {options_list[i+column_height]:25}"
                  f"{(i+(column_height*2)):3}: {options_list[i+(column_height*2)]:25}")
    elif extra_options == 1:
        for i in range(0, len(options_list) // 3):
            print(f"{i:3}: {options_list[i]:25}{(i+column_height+1):3}: {options_list[i+1+column_height]:25}"
                  f"{(i+(column_height*2)+1):3}: {options_list[i+(column_height*2)+1]:25}")
        print(f"{column_height:3}: {options_list[column_height]:25}")
    elif extra_options == 2:
        for i in range(0, len(options_list) // 3):
            print(f"{i:3}: {options_list[i]:25}{(i+column_height+1):3}: {options_list[i+1+column_height]:25}"
                  f"{(i+(column_height*2)+2):3}: {options_list[i+(column_height*2)+2]:25}")
        print(f"{column_height:3}: {options_list[column_height]:25}"
              f"{(column_height*2)+1:3}: {options_list[(column_height*2)+1]:25}")

    change_type = input("Change: ").strip()
    print(f"Selected Change: {options_list[int(change_type)]}")
    change_image(change_type, image, data)
