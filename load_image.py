import cv2

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
print(img.shape)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()