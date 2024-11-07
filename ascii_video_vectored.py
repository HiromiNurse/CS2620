# import dxcam
from PIL import Image, ImageFilter
from os import system, get_terminal_size
from imageFunctions import greyscale


def resize(image):
    width, height = get_terminal_size()
    return image.resize((width, height-5), resample=1)


def brighten_color(r, g, b, factor=1.5):
    r = min(int(r * factor), 255)
    g = min(int(g * factor), 255)
    b = min(int(b * factor), 255)
    return r, g, b


def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def get_ascii(image, brightness_factor=1.0):
    ascii_str = []
    pixels = image.getdata()

    for pixel in pixels:
        r, g, b = pixel
        r, g, b = brighten_color(r, g, b, brightness_factor)
        ascii_char = ASCII_CHARS[(len(ASCII_CHARS)-1) - (sum(pixel) // 3 * (len(ASCII_CHARS) - 1) // 255)]
        color_code = rgb_to_ansi(r, g, b)
        ascii_str.append(f"{color_code}{ascii_char}\033[0m")
    return ascii_str


def get_ascii_single(pixel, brightness_factor = 1.0):
    # r, g, b = pixel
    # r, g, b = brighten_color(r, g, b, brightness_factor)
    ascii_char = ASCII_CHARS[(len(ASCII_CHARS)-1) 
                                  - ((sum(pixel) // 3) * (len(ASCII_CHARS) - 1) 
                                     // 255)]
    # color_code = rgb_to_ansi(r, g, b)
    # return (f"{color_code}{ascii_char}\033[0m)")
    return ascii_char


ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ASCII_CHARS_blob = "$@B8&WM#*oakbdpqZO0QUXcunxr1?+~,\"`'."

def convert_video():
    screen_number = int(input("Which monitor will be the input? (0-3): "))
    # camera = dxcam.create(device_idx=0, output_idx=screen_number)
    # camera.start()

    while True:
        # frame = camera.get_latest_frame()
        # image = Image.fromarray(frame)
        image = resize(image)

        ascii_str = get_ascii(image, brightness_factor=1.5)
        width = image.width
        ascii_img = ""


        for i in range(0, len(ascii_str), width):
            ascii_img += ''.join(ascii_str[i: i + width]) + "\n"

        system('cls')
        print(ascii_img)


def convert_picture():
    # image_name = input("Image name: ")
    image_name = "skibidi.jpg"
    image = Image.open(image_name)
    image = greyscale(image)

    edge_image = image.filter(ImageFilter.FIND_EDGES)
    
    image_data = image.load()
    edge_data = edge_image.load()

    width, height = image.size

    image_ascii = []

    for y in range(height):
        for x in range(width):
            # if edge_data[x, y][0] < 100:
            image_ascii.append(get_ascii_single(image_data[x, y]))
            # else:
            #     if y > 0:
            #         if edge_data[x, y-1][0] > 100:
            #             image_ascii.append("|")
            #         elif edge_data[x-1, y-1][0] > 100:
            #             image_ascii.append("V")
            #         elif x < width-1:
            #             if edge_data[x+1, y-1][0] > 100:
            #                 image_ascii.append("/")
            #             else:
            #                 image_ascii.append("|")
            #         elif edge_data[x-1, y][0] > 100:
            #             image_ascii.append("-")
            #         else:
            #             ascii = get_ascii_single(image_data[x, y])
            #             image_ascii.append(ascii)

    ascii_image = ''

    with open("text_out.txt", "w") as file:
        for i in range(0, len(image_ascii), width):
            ascii_image += ''.join(image_ascii[i: i+width]) + "\n"
        file.write(ascii_image)


if __name__ == "__main__":
    # choice = input("1 or 2: ")
    # if choice == '1':
    #     convert_video()
    # elif choice == '2':
    #     convert_picture()
    # else:
    #     print("Nope")
    convert_picture()