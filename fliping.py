import cv2

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
flipped_h = cv2.flip(img,1)
flipped_v = cv2.flip(img,0)
flipped_b = cv2.flip(img,-1)

cv2.imshow("Original", img)
cv2.imshow("Flipped Horizontal", flipped_h)
cv2.imshow("Flipped Vertical", flipped_v)
cv2.imshow("Flipped Both", flipped_b)
cv2.waitKey(0)
cv2.destroyAllWindows()