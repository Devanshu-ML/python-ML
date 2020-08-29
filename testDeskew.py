import numpy as np
from skimage import io
from skimage.transform import rotate
from skimage.color import rgb2gray
from deskew import determine_skew

image = io.imread('C:/LogFiles/pdf2image/testing/unnamed.png')
grayscale = rgb2gray(image)
angle = determine_skew(grayscale)
while not angle == 0.0:
    print(angle)
    rotated = rotate(image, angle, resize=True) * 255
    io.imsave("C:/LogFiles/pdf2image/testing/deskewExampleOut.png", rotated.astype(np.uint8))
    print('saved')
    image = io.imread('C:/LogFiles/pdf2image/testing/deskewExampleOut.png')
    grayscale = rgb2gray(image)
    angle = determine_skew(grayscale)
    print(angle)
