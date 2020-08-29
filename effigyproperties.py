from PIL import Image


# from reduceNoise import reduceWithfastNlMeansDenoising


# Define a method for printing image attributes

def printImageAttributes(imageObject, imagePath):
    # Retrieve the attributes of the image

    fileFormat = imageObject.format  # Format of the image

    imageMode = imageObject.mode  # Mode of the image

    imageSize = imageObject.size  # Size of the image - tupe of (width, height)

    colorPalette = imageObject.palette  # Palette used in the image

    # Print the attributes of the image

    print("Attributes of image:%s" % imagePath)

    print("The file format of the image is:%s" % fileFormat)

    print("The mode of the image is:%s" % imageMode)

    print("The size of the image is:width %d pixels,height %d pixels" % imageSize)

    print("Color palette used in image:%s" % colorPalette)

    print("Keys from image.info dictionary:%s")

    for key, value in imageObject.info.items():
        print(key)
    if imageObject.info.get('dpi'):
        x_dpi, y_dpi = imageObject.info['dpi']
        if x_dpi != y_dpi:
            print('Inconsistent DPI image data')
        print("x_dpi: " + str(x_dpi))
        print("y_dpi: " + str(y_dpi))


# Create an image object and show the image

imagePath = "C:/LogFiles/DPO/Document/ID Docs/download.jpg"

imagePathTemp = "TempImage"

image = Image.open(imagePath)

image.show()

# Create an image object with color palette and show the image

imageWithColorPalette = image.convert("P", palette=Image.ADAPTIVE, colors=8)

imageWithColorPalette.show()

# Print the attributes of the images

printImageAttributes(image, imagePath)

print("==================")

printImageAttributes(imageWithColorPalette, imagePathTemp)

# reduceWithfastNlMeansDenoising()


from PIL import Image

im = Image.open("C:/LogFiles/DPO/Document/ID Docs/images (1).jpg")
im.save("C:/LogFiles/DPO/Document/ID Docs/images (1)-600.jpg", dpi=(600, 600))
