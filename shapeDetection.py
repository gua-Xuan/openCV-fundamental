#圖片集合(長方形,正方形,圓形,橢圓形)
import cv2 as cv

img = cv.imread('image_input/shapes.jpg')
img_contour = img.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_img = cv.Canny(img, 150, 200)
contours, hierarchy =  cv.findContours(canny_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
shape_type = {
    4: "rectangle",8:"ellipse",11:"ellipse",15:"circle",100:"unknown!"
}
for cnt in contours:
    # cv.drawContours(imgContour, cnt, -1,(255, 0, 0), 1) #形狀邊界提取
    area = cv.contourArea(cnt)
    print(area)
    if area > 1000: #雜訊過濾
        peri = cv.arcLength(cnt, True)
        vertices = cv.approxPolyDP(cnt, peri*0.01,True)
        corners = len(vertices)
        detection_result = shape_type.get(corners,100)
        x, y, w, h = cv.boundingRect(vertices)
        cv.rectangle(img_contour, (x,y), (x+w,y+h), (0,255,0),2)
        # cv.putText(img_contour, str(corners), (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),1) #確認頂點數量
        # cv.putText(img_contour, str(area), (x,y+50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255),1) #確認面積
        cv.putText(img_contour,detection_result,(x,y-5),cv.FONT_HERSHEY_PLAIN,1.2,(0,255,255),1)
        
# cv.imshow('img', img) #灰階圖
# cv.imshow('cannyImg', canny_img) #邊緣提取圖
cv.imshow('imgContour', img_contour)
cv.waitKey(0)