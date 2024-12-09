from image_functions import *
import subprocess
from ascii_video_color import *


options_list = ["Quit", "Change Image", "Save Image", "Corrected Greyscale",
                "Greyscale", "Isolate Red", "Isolate Green", "Isolate Blue", "Invert Colors"
                "Mirror Left on Right", "Mirror Right on Left", "Mirror Top on Bottom",
                "Mirror Bottom on Top", "Mirror Top Left to Bottom Right",
                "Mirror Bottom Right to Top Left", "Flip About X-axis", "Flip About Y-axis",
                "Flip About Diagonal", "Rotate 90 Clockwise", "Rotate 90 CounterClockwise",
                "Rotate and Expand", "Rotate Maintain Size", "Rotate About Center",
                "Rotate About Point", "Translate", "Transform", "Scale", "Blur", "Blur No Padding",
                "Custom Kernel", "Qr Code Simplifier", "Qr Code Reader", "Qr Code Enocoder",
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
    image = WorkingImage
    option = print_menu()
    while option != 0:
        match option:
            case 0:
                quit()
            case 1:
                image.change_image()
            case 2:
                save_name = input("Name of the same image (no extension): ")
                image.save(name=save_name)
            case 3:
                image.corrected_greyscale()
            case 4:
                image.greyscale()
            case 5:
                image.isolateRed()
            case 5:
                image.isolateGreen()
            case 6:
                image.isolateBlue()
            case 7:
                image.invertColors()
            case 8:
                image.leftToRightMirror()
            case 9:
                image.rightToLeftMirror()
            case 10:
                image.topToBottomMirror()
            case 11:
                image.bottomToTopMirror()
            case 12:
                image.bottomToTopDiagonalMirror()
            case 13:
                image.topToBottomDiagonalMirror()
            case 14:
                image.flipXAxis()
            case 15:
                image.flipYAxis()
            case 16:
                image.flipDiagonal()
            case 17:
                image.rotate90Clockwise()
            case 18:
                image.rotate90CounterClockiwse()
            case 19:
                image.rotateAndEnlarge()
            case 20:
                image.rotateAndCrop()
            case 21:
                image.rotateAboutCenter()
            case 22:
                image.rotateAboutPoint()
            case 23:
                image.arbitraryTranslation()
            case 24:
                image.arbitraryTransformation()
            case 25:
                image.scale()
            case 26:
                image.blur()
            case 27:
                image.blurNoPadding()
            case 28:
                image.customKernelApplicator()
            case 29:
                image.qr_code_simplifier()
            case 30:
                image.qrCodeReader()
            case 31:
                image.qrCodeEncoder()
            case 32:
                image.stringEncoder()
            case 33:
                image.readString()
            case 34:
                initialize1()
            case _:
                print("Not an option.")
        go_forth = input("Continue? (y/n): ")
        if go_forth.lower() != "n":
            option = print_menu()
        else:
            quit()
