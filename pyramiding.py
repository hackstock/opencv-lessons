import cv2

original = cv2.imread("demo.png", cv2.IMREAD_COLOR)
cv2.imshow("Image", original)

smaller = cv2.pyrDown(original)
larger = cv2.pyrDown(original)

cv2.imshow("Original", original)
cv2.imshow("Smaller", smaller)
cv2.imshow("Larger", larger)

cv2.waitKey(0)
cv2.destroyAllWindows()