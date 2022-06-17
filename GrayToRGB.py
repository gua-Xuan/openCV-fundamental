#將灰階圖片轉為BGR

import cv2 as cv
import numpy as np

image = cv.imread("image_input/humanTest.jpg")#導入
print(image.shape)  #返回元組
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)#轉灰階
print(gray.shape)
cv.imwrite("image_output/__gray.png",gray)#導出

color_image = cv.applyColorMap(image, cv.COLORMAP_JET)
cv.namedWindow('gray_image',cv.WINDOW_NORMAL)
cv.namedWindow('color_image',cv.WINDOW_NORMAL)
cv.imshow("gray_image",gray)
cv.imshow("color_image",color_image)
cv.waitKey(0)
cv.destroyAllWindows()