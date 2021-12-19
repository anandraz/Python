"""
This is open cv cam programming
"""
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame1 = cap.read()
    #ret, frame2 = cap.read()

    #diff = cv2.absdiff(frame1, frame2)

    if cv2.waitKey(10) == ord('q'):
        break

    #cv2.imshow('frame', diff) 
    
    #gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", frame1)
cap.release()
cv2.destroyAllWindows()