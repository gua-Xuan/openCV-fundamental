
import cv2 as cv

img = cv.imread('image_input/shape.jpg')
imgContour = img.copy()
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cannyImg = cv.Canny(img,150,200)
contours,hierarchy =  cv.findContours(cannyImg, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

for cnt in contours:
    cv.drawContours(imgContour, cnt, -1,(255, 0, 0), 3)
cv.imshow('img',img)
cv.imshow('cannyImg',cannyImg)
cv.imshow('imgContour',imgContour)
cv.waitKey(0)