import cv2

cap = cv2.VideoCapture(0)

while 1:
    _,frame = cap.read()
    cv2.imshow("",frame)
    if cv2.waitKey(30) == ord("q"):
        cv2.destroyAllWindows()
        cap.release()
        break