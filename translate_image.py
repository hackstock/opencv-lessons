import cv2
import numpy as np

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
(h,w) = img.shape[:2]

T = np.float32([[1,0, 50],[0,1,50]])
t_img = cv2.warpAffine(img, T,(w,h))
cv2.imshow("Translated", t_img)

cv2.waitKey(5000)
cv2.destroyAllWindows()