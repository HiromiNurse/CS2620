from imageFunctions import *
from hiding import *


def main_menu():
    # try:
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
        return
    image = Image.open(selected_image)

    options_list = ["Normal", "Greyscale corrected", "Greyscale", "Color Isolation Red",
                    "Color Isolation Green", "Color Isolation Blue", "Invert", "Blind Filter",
                    "X-axis Mirror (Left)", "X-axis Mirror (Right)", "Y-axis Mirror (Top)",
                    "Y-axis Mirror (Bottom)", "Flip X-axis", "Flip Y-axis", "Flip Diagonal",
                    "Rotate 90(Clockwise)", "Rotate 90(Counter-Clockwise)", "Diagonal Mirror (Top Right)",
                    "Diagonal Mirror (Bottom Left)", "Transform", "Scale", "Arbitrary Rotation",
                    "Arbitrary Rotation (Cutoff)", "Arbitrary Rotation (inscribed)", "Gaussian Blur (no pad)",
                    "Gaussian Blur (Padded)", "Kernel Assortment", "Rotation About", "Hide QR Code",
                    "Hide QR better", "Read QR Code", 
                    "Quit/q"]

    column_height = len(options_list) // 3
    extra_options = len(options_list) % 3
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

    change_type = input("Change: ").strip()
    print(f"Selected Change: {options_list[int(change_type)]}")
    match change_type:
        case '0':
            image.save("output_image.png")
        case '1':
            new_image = greyscale_Corrected(image)
        case '2':
            new_image = greyscale(image)
        case '3':
            new_image = colorIsolationRed(image)
        case '4':
            new_image = colorIsolationGreen(image)
        case '5':
            new_image = colorIsolationBlue(image)
        case '6':
            new_image = colorInvert(image)
        case '7':
            return  # holder
        case '8':
            new_image = xAxisMirrorL(image)
        case '9':
            new_image = xAxisMirrorR(image)
        case '10':
            new_image = yAxisMirrorT(image)
        case '11':
            new_image = yAxisMirrorB(image)
        case '12':
            new_image = xAxisFlip(image)
        case '13':
            new_image = yAxisFlip(image)
        case '14':
            new_image = flipDiagonal(image)
        case '15':
            new_image = rotateClockwise(image)
        case '16':
            new_image = rotateCClockwise(image)
        case '17':
            new_image = diagonalMirrorT(image)
        case '18':
            new_image = diagonalMirrorB(image)
        case '19':
            new_image = transform(image)
        case '20':
            new_image = scale(image)
        case '21':
            new_image = rotateBigger(image)
        case '22':
            new_image = rotateCutoff(image)
        case '23':
            new_image = rotateSmallest(image)
        case '24':
            new_image = blurFunctionNP(image)
        case '25':
            new_image = blurFunction(image)
        case '26':
            new_image = customKernel(image)
        case '27':
            new_image = rotationAbout(image)
        case '28':
            new_image = hideQR(image)
            new_image.save("encoded_image.png")
            return
        case '29':
            new_image = hide_Qr_Linear(image)
        case '30':
            new_image = decodeQR()

        case _:
            print("Not an option. Quitting...")
            return

    if change_type != '0':
        print("Saving...")
        new_image.save("output_image.png")

    # except ValueError:
    #     print("Invalid input. Try again.")
    #     main_menu()
    #     return


if __name__ == "__main__":
    main_menu()
