import cv2
import numpy as np

img = cv2.imread("berlin.JPG", cv2.IMREAD_COLOR)
kernel_3x3 = np.ones((3,3), np.float32) / 9
kernel_7x7 = np.ones((7,7), np.float32) / 49

blurred_3 = cv2.filter2D(img, -1, kernel_3x3)
blurred_7 = cv2.filter2D(img, -1, kernel_7x7)

cv2.imshow("Original", img)
cv2.imshow("Slightly Blurred", blurred_3)
cv2.imshow("Highly Blurred", blurred_7)
cv2.waitKey(0)
cv2.destroyAllWindows()