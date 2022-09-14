import cv2 as cv

img = cv.imread("icon.jpg")
img_re = cv.resize(img,[180,180])
cv.imwrite("icon_re.png",img_re)