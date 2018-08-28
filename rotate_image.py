import cv2
import numpy as np

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
(h,w) = img.shape[:2]

M = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)
t_img = cv2.warpAffine(img, M,(w,h))
cv2.imshow("Translated", t_img)

cv2.waitKey(5000)
cv2.destroyAllWindows()