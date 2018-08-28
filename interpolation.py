import cv2
import numpy as np

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
s_img = cv2.resize(img, None, fx=0.75, fy=0.75, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Double", s_img)

cv2.waitKey(0)
cv2.destroyAllWindows()