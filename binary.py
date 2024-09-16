from PIL import Image

image = Image.open("orionNebule.jpg")
data = image.load()
width, height = image.size
for y in range(height):
    for x in range(width):
        r, g, b = data[x,y]

        mask = 42

        r &= mask
        b &= mask
        g &= mask

        data[x,y] = (r,g,b)

image.save("binary-nebula.png")
