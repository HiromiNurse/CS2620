from PIL import Image


def hideQR(image):
    qrImage = Image.open("qrcode.png")
    qrData = qrImage.load()
    data = image.load()

    width, height = qrImage.size
    if qrImage.size > image.size:
        print("QR code to large.")
        return

    for y in range(image.height):
        for x in range(image.width):
            r,g,b = data[x,y]
            r &= 247
            if 0 <=x<height and 0<=y<height:
                qr, qg, qb = qrData[x,y]
                if qr<100 and qg<100 and qb<100:
                    # add 0 to the end of the binary number r
                    r |= 0
                else:
                    # add 1 to the end of the binary number r
                    r |= 15
            data[x,y] = (r, g, b)
    return image


def decodeQR():
    image = Image.open("encoded_image.png")
    data = image.load()
    width, height = image.size

    qrCode = Image.new("RGB", (width, height))
    qrData = qrCode.load()

    for y in range(image.height):
        for x in range(image.width):
            r,g,b = data[x,y]
            if (r & 15) == 15:
                qrData[x,y] = (0, 0, 0)
            else:
                qrData[x,y] = (255, 255, 255)
    return qrCode

