import dxcam
from PIL import Image
from os import system, get_terminal_size


def resize(image, new_width = 100):
    width, lines = get_terminal_size()
    new_width = width
    old_width, old_height = image.size
    new_height = new_width * old_height // old_width
    return image.resize((new_width, new_height))


def get_ascii(image):
    ascii_str = ""
    pixels = image.getdata()
    # for y in range(image.height):
    #     output_frame + "\n"
    #     for x in range(image.width):
    #         output_frame +
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel[1] // 25]
    return ascii_str


ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
screen_number = int(input("Which monitor will be the input?(0-3): "))
camera = dxcam.create(device_idx=0, output_idx=screen_number)
camera.start()
while True:
    frame = camera.get_latest_frame()
    image = Image.fromarray(frame)
    image = resize(image)
    image.convert("L")
    ascii_str = get_ascii(image)
    ascii_str_len = len(ascii_str)
    width = image.width
    ascii_img = ""
    for i in range(0, ascii_str_len, width):
        ascii_img += ascii_str[i: i+width] + "\n"
    system('cls')
    print(ascii_img)


camera.stop()

