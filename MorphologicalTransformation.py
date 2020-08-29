import cv2
import numpy as np

def Opening():
    originalImage = cv2.imread('C:\\Users\\ashis\\Pictures\\Camera Roll\\RP_back.PNG')
    img = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    #erosion = cv2.erode(originalImage, kernel, iterations=1)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('image', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #img = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

Opening()