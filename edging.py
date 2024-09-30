from gaussian_Blur import applyKernel
from PIL import Image


def find_edge(image):
    data = image.load()

    # Greyscale the image for smoother edging
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            greyscale_value = (red + green + blue) // 3
            data[x, y] = (greyscale_value, greyscale_value, greyscale_value)

    # Run the laplacian kernel over the image
    goon = [[-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]]
    edged_image = applyKernel(image, goon)
    edged_image = Image.fromarray(edged_image)
    edged_image.save("Edged Image.png")
    
if __name__ == "__main__":
    find_edge(Image.open("image.jpg"))
