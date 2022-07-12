import cv2 as cv

img = cv.imread('gato.jpg')

cv.imshow("eh o gatos", img)

cv.waitKey(0)