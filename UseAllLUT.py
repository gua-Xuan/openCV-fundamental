import cv2 as cv
import numpy as np


cv2_luts = [lut for lut in dir(cv)  if lut.startswith("COLORMAP_")]
print(f"opencv LUT colormap amount : {len(cv2_luts)} ")
print(f"opencv LUT colormap type: {cv2_luts}")

print("cv.COLORMAP_COOL",type(eval("cv.COLORMAP_COOl")))
print(eval("cv.COLORMAP_COOL"), type(eval("cv.COLORMAP_COOL")))


image = cv.imread('./___.jpg')

all_luts_img = [(lut, cv.applyCplorMap(image,eval("cv"+lut))) for lut in cv2_luts ]

add_text_imgs = [cv.putText(lut_img[1],lut_img[0],(20,20), cv.FONT_HERSHEY_SIMPLEX,
 0.5, (0, 0, 255), 2 ) for lut_img in all_luts_img]

col1 = np.vstack(tuple(add_text_imgs[0:11]))#垂直方向連接元組或array
col2 = np.vstack(tuple(add_text_imgs[11:22]))#垂直方向連接元組或array
result = np.hstack((col1,col2))#水平方向連接
cv.imwrite("lut_result.jpg",result)
cv.imshow("result",result)
cv.waitKey(0)
