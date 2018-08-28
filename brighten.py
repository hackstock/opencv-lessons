import cv2
import numpy as np

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
M = np.ones(img.shape, dtype="uint8") * 75

brighter = cv2.add(img, M)
cv2.imshow("brighter", brighter)

darker = cv2.subtract(img, M)
cv2.imshow("darker", darker)

cv2.waitKey(0)
cv2.destroyAllWindows()