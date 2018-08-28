import cv2

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
print(img.shape)

blue = img.copy()
blue[:,:,1] = 0
blue[:,:,2] = 0

cv2.imshow("Blue", blue)

cv2.waitKey(0)
cv2.destroyAllWindows()