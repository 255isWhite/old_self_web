from ctypes import resize
import cv2 as cv

img = cv.imread("spiderman.jpg",cv.IMREAD_COLOR)
resized = cv.resize(img, None, fx=0.3, fy=0.3, interpolation=cv.INTER_AREA)
cv.imshow("resized",resized)
cv.waitKey(0)