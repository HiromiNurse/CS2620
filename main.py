from PIL import Image


image = Image.open("images.jpg")

data = image.load()


def change_image(change):
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x,y]

            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            match change:
                case 'invert':
                    data[x,y] = (255-red, 255-green, 255-blue)
                case 'greyscale corrected':
                    greyscalec_value = int((red*.21) + (green*.71) + (blue*.08)) // 3
                    
                    data[x,y] = (greyscalec_value, greyscalec_value, greyscalec_value)
                case 'greyscale':
                    greyscale_value = (red + green + blue) // 3
                    data[x,y] = (greyscale_value, greyscale_value, greyscale_value)
                case 'normal':
                    data[x,y] = (red, green,blue)            

print("What kind of change would you like to make?")
for change in ["Invert", "Greyscale corrected", "Greyscale", "Normal"]:
    print(change)
change_image(input().lower().strip())
image.save("aye-aye.png")
