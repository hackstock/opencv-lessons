import cv2

img = cv2.imread("demo.png", cv2.IMREAD_COLOR)
cv2.imshow("image", img)

key = cv2.waitKey(0) & 0xFF
if key == 27: # waits for esc key to be pressed
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite("demo.jpg", img)
    cv2.destroyAllWindows()