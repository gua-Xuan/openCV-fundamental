#cv2.Canny練習  
import cv2 as cv
from cv2 import WINDOW_NORMAL

img = cv.imread('image_input/shape.jpg')
imgCanny = cv.Canny(img,250,300)
cv.putText(imgCanny,"TEXT ADD",(0,20),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
cv.namedWindow("img_edge",cv.WINDOW_NORMAL)
cv.imshow("img_edge",imgCanny) #圖片邊緣提取
cv.waitKey(1000)