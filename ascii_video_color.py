import dxcam
from PIL import Image
from os import system, get_terminal_size
from time import sleep

'''
Add Vectoring? Make it so edges are detected and accounted for
'''

def resize(image, new_width=100):
    width, height = get_terminal_size()
    # new_width = width
    # old_width, old_height = image.size
    # new_height = new_width * old_height // old_width
    # return image.resize((new_width, new_height))
    return image.resize((width, height-5), resample=0)


def brighten_color(r, g, b, factor=1.5):
    r = min(int(r * factor), 255)
    g = min(int(g * factor), 255)
    b = min(int(b * factor), 255)
    return r, g, b


def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def get_ascii(image, brightness_factor=1.5):
    ascii_str = []
    pixels = image.getdata()

    for pixel in pixels:
        r, g, b = pixel
        r, g, b = brighten_color(r, g, b, brightness_factor)
        ascii_char = ASCII_CHARS[(len(ASCII_CHARS)-1) - (sum(pixel) // 3 * (len(ASCII_CHARS) - 1) // 255)]
        color_code = rgb_to_ansi(r, g, b)
        ascii_str.append(f"{color_code}{ascii_char}\033[0m")
    return ascii_str


# add gradient correction for ascii
# basically adds directionality
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
screen_number = int(input("Which monitor will be the input? (0-3): "))
camera = dxcam.create(device_idx=0, output_idx=screen_number)
camera.start()

def videoing():
    while True:
        frame = camera.get_latest_frame()
        image = Image.fromarray(frame)
        image = resize(image)

        ascii_str = get_ascii(image, brightness_factor=1.5)
        width = image.width
        ascii_img = ""

        for i in range(0, len(ascii_str), width):
            ascii_img += ''.join(ascii_str[i: i + width]) + "\n"

        system('cls')
        print(ascii_img)
        sleep(.01666)
