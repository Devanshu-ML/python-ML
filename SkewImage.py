# image processing resources
import imutils
from skimage.io import imread, imsave
from skimage.filters import gaussian, threshold_otsu
from skimage.feature import canny
from skimage.transform import probabilistic_hough_line, rotate

# testing
import numpy as np
import os


# deskewing function

def deskew(filename):
    image = imread(filename, as_gray=True)

    # threshold to get rid of extraneous noise
    thresh = threshold_otsu(image)
    normalize = image > thresh

    # gaussian blur
    blur = gaussian(normalize, 3)

    # canny edges in scikit-image
    edges = canny(blur)

    # hough lines
    hough_lines = probabilistic_hough_line(edges)

    # hough lines returns a list of points, in the form ((x1, y1), (x2, y2))
    # representing line segments. the first step is to calculate the slopes of
    # these lines from their paired point values
    slopes = [(y2 - y1) / (x2 - x1) if (x2 - x1) else 0 for (x1, y1), (x2, y2) in hough_lines]

    # it just so happens that this slope is also y where y = tan(theta), the angle
    # in a circle by which the line is offset
    rad_angles = [np.arctan(x) for x in slopes]

    # and we change to degrees for the rotation
    deg_angles = [np.degrees(x) for x in rad_angles]

    # which of these degree values is most common?
    histo = np.histogram(deg_angles, bins=180)

    # correcting for 'sideways' alignments
    rotation_number = histo[1][np.argmax(histo[0])]

    if rotation_number > 45:
        rotation_number = -(90 - rotation_number)
    elif rotation_number < -45:
        rotation_number = 90 - abs(rotation_number)

    return rotation_number


# testing on image library
_path = 'C:/LogFiles/pdf2image/testing/'
for dirpath, dirnames, filenames in os.walk(_path):
    for filename in filenames:
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
            rotation_angle = deskew(_path + filename)
            print('Rotation angle for ' + filename + ' is {0}'.format(rotation_angle) + '\n')
            #rotated = rotate(_path + filename, rotation_angle)
            rotated = imutils.rotate_bound(_path + filename, rotation_angle)
            imsave(_path + filename, rotated.astype(np.uint8))
