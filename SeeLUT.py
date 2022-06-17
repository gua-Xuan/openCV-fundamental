import cv2 as cv


cv2_luts = [lut for lut in dir(cv) if lut.startswith("COLORMAP_")]
print(f"opencv LUT colormap amount : {len(cv2_luts)} ")
print(f"opencv LUT colormap type: {cv2_luts}")
