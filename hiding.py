from PIL import Image


def hideQR(image):
    qrImage = image.open("qr-code.png")
    qrData = qrImage.load()
    data = image.load(image)

    width, height = qrImage.size
    for y in range(image.height):
        for x in range(image.width):
            r,g,b = data[x,y]
            r &= 254
            if 0 <=x<height and 0<=y<height:
                qr, qg, qb = qrData[x,y]
                if qr<100 and qg<100 and qb<100:
                    # add 0 to the end of the binary number r
                    continue
                else:
                    # add 1 to the end of the binary number r
                    continue
            data[x,y] = (r, g, b)
    return image

