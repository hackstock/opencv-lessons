import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    (h,w,c) = frame.shape
    black = (0,0,0)
    cv2.line(frame, (0,0),(w,h), black,2)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blue_frame = frame.copy()
    blue_frame[:,:,1] = 0
    blue_frame[:,:,2] = 0
    cv2.imshow("video", blue_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()