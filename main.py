from image_functions import *
from ascii_video_color import *


options_list = ["Quit", "Change Image", "Save Image", "Corrected Greyscale",
                "Greyscale", "Isolate Red", "Isolate Green", "Isolate Blue", "Invert Colors",
                "Mirror Left on Right", "Mirror Right on Left", "Mirror Top on Bottom",
                "Mirror Bottom on Top", "Mirror Top Left to Bottom Right",
                "Mirror Bottom Right to Top Left", "Flip About X-axis", "Flip About Y-axis",
                "Flip About Diagonal", "Rotate 90 Clockwise", "Rotate 90 CounterClockwise",
                "Rotate and Expand", "", "Rotate About Center",
                "Rotate About Point", "Translate", "Transform", "Scale", "Blur", "Blur No Padding",
                "Custom Kernel", "Qr Code Simplifier", "Qr Code Reader", "Qr Code Encoder",
                "String Encoder", "String Decoder", "Ascii Video"]


def print_menu():
    column_height = len(options_list) // 3
    extra_options = len(options_list) % 3
    print("What kind of change would you like to make?")
    if extra_options == 0:
        for i in range(0, len(options_list) // 3):
            print(f"{i:3}: {options_list[i]:35}{(i + column_height):3}: {options_list[i + column_height]:35}"
                  f"{(i + (column_height * 2)):3}: {options_list[i + (column_height * 2)]:35}")
    elif extra_options == 1:
        for i in range(0, len(options_list) // 3):
            print(
                f"{i:3}: {options_list[i]:35}{(i + column_height + 1):3}: {options_list[i + 1 + column_height]:35}"
                f"{(i + (column_height * 2) + 1):3}: {options_list[i + (column_height * 2) + 1]:35}")
        print(f"{column_height:3}: {options_list[column_height]:35}")
    elif extra_options == 2:
        for i in range(0, len(options_list) // 3):
            print(
                f"{i:3}: {options_list[i]:35}{(i + column_height + 1):3}: {options_list[i + 1 + column_height]:35}"
                f"{(i + (column_height * 2) + 2):3}: {options_list[i + (column_height * 2) + 2]:35}")
        print(f"{column_height:3}: {options_list[column_height]:35}"
              f"{(column_height * 2) + 1:3}: {options_list[(column_height * 2) + 1]:35}")

    change_type = int(input("Change: ").strip())
    print(f"Selected Change: {options_list[change_type]}")
    return change_type

if __name__ == "__main__":
    image_list = [f for f in listdir() if ".jpg" in f]
    number = 1
    for image in image_list:
        print(f"{number}: {image}")
        number += 1
    image_name = input("Name of the image to open: ")
    image = WorkingImage(image_name)
    option = print_menu()
    while option != 0:
        match option:
            case 0:
                quit()
            case 1:
                image.change_image()
            case 2:
                save_name = input("Name of the saved image (no extension): ")
                image.save(name=save_name)
            case 3:
                image.corrected_greyscale()
            case 4:
                image.greyscale()
            case 5:
                image.isolateRed()
            case 6:
                image.isolateGreen()
            case 7:
                image.isolateBlue()
            case 8:
                image.invertColors()
            case 9:
                image.leftToRightMirror()
            case 10:
                image.rightToLeftMirror()
            case 11:
                image.topToBottomMirror()
            case 12:
                image.bottomToTopMirror()
            case 13:
                image.bottomToTopDiagonalMirror()
            case 14:
                image.topToBottomDiagonalMirror()
            case 15:
                image.flipXAxis()
            case 16:
                image.flipYAxis()
            case 17:
                image.flipDiagonal()
            case 18:
                image.rotate90Clockwise()
            case 19:
                image.rotate90CounterClockiwse()
            case 20:
                angle = int(input('Angle: '))
                image.rotateAndEnlarge(angle)
            case 21:
                angle = int(input('Angle: '))
                image.rotateAndCrop(angle)
            case 22:
                angle = int(input('Angle: '))
                image.rotateAboutCenter(angle)
            case 23:
                angle = int(input('Angle: '))
                x = int(input("x: "))
                y = int(input("y: "))
                image.rotateAboutPoint(angle, x, y)
            case 24:
                dx = int(input("Change in x: "))
                dy = int(input("Change in y: "))
                image.arbitraryTranslation(dx, dy)
            case 25:
                a = float(input("X Scale: "))
                b = int(input("X Rotation: "))
                c = (input("X Translation: "))
                d = float(input("Y Scale: "))
                e = int(input("Y Rotation: "))
                f = (input("Y Translation: "))
                image.arbitraryTransformation()
            case 26:
                scale_factor = float(input("Scale factor: "))
                image.scale(scale_factor)
            case 27:
                blur = float(input("Blur amount: "))
                kernel = int(input("Kernel size: "))
                image.blur(blur, kernel)
            case 28:
                blur = float(input("Blur amount: "))
                kernel = int(input("Kernel size: "))
                image.blurNoPadding(blur, kernel)
            case 29:
                image.customKernelApplicator()
            case 30:
                image.qr_code_simplifier()
            case 31:
                image.qrCodeReader()
            case 32:
                image.qrCodeEncoder()
            case 33:
                image.stringEncoder()
            case 34:
                image.readString()
            case 35:
                initialize1()
            case _:
                print("Not an option.")
        # go_forth = input("Continue? (y/n): ")
        # if go_forth.lower() != "n":
        option = print_menu()
        # else:
        #     quit()
