import numpy as np
import cv2
from matplotlib import pyplot as plt



def reduceWithfastNlMeansDenoising():
    img = cv2.imread('C:\\LogFiles\\python\\data\\capture.jpg')
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    grayImage = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey', grayImage)

    plt.subplot(121), plt.imshow(img)
    plt.subplot(122), plt.imshow(dst)
    plt.show()
    cv2.imwrite('C:\\Users\\ashis\\Pictures\\Camera Roll\\Output\\greyImage.PNG',grayImage)
    cv2.imwrite('C:\\Users\\ashis\\Pictures\\Camera Roll\\Output\\colorImage.PNG',dst)

reduceWithfastNlMeansDenoising()

def reduceWithfastNlMeansDenoisingColored():
    img = cv2.imread('C:\\Users\\ashis\\Pictures\\Camera Roll\\RP_back.PNG')
    converted_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    plt.subplot(121), plt.imshow(img)
    plt.subplot(122), plt.imshow(dst)
    plt.show()


def reduceWithfastNlMeansDenoisingMulti():
    img = cv2.imread('C:\\Users\\ashis\\Pictures\\Camera Roll\\RP_back.PNG')
    dst = cv2.fastNlMeansDenoisingMulti(img, None, 10, 10, 7, 21)
    plt.subplot(121), plt.imshow(img)
    plt.subplot(122), plt.imshow(dst)
    plt.show()

def reduceWithfastNlMeansDenoisingColoredMulti():
    img = cv2.imread('C:\\Users\\ashis\\Pictures\\Camera Roll\\RP_back.PNG')
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    plt.subplot(121), plt.imshow(img)
    plt.subplot(122), plt.imshow(dst)
    plt.show()