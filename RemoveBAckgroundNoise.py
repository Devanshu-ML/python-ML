import cv2
import numpy as np

im = cv2.imread('C:\\Users\\ashis\\Pictures\\Camera Roll\\RP_back.PNG')

def size_threshold():
    image = np.zeros((400, 400, 3), dtype="uint8")
    raw = image.copy()
    image[np.where((image == [0, 0, 0]).all(axis=2))] = [255, 255, 255]
    cv2.imshow('Test', image)
    cv2.imshow('Test2', raw)
    if cv2.waitKey() == ord('q'):
        cv2.destroyAllWindows()

sized = size_threshold()
print(sized)
centered = y_centroid_threshold(sized, 40, 63)
cv2.imshow('ocr_out.png', centered)
cv2.waitKey(0)
cv2.destroyAllWindows()