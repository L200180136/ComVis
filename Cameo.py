import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened):      
    _,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 1.45)
    canny = cv2.Canny(blur, 50, 75)

    _,thresh = cv2.threshold(canny,255,255,255)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    color = cv2.cvtColor(canny, cv2.COLOR_GRAY2RGB)
    con1 = cv2.drawContours(color, contours, 40, (200, 0, 0), 1)
    con2 = cv2.drawContours(color, contours, 30, (0, 200, 0), 1)
    con3 = cv2.drawContours(color, contours, 20, (0, 0, 200), 1)
    con = con1 + con2 + con3 
    
    cv2.imshow("frame",frame)
    cv2.imshow("draw Contours", con)

    key = cv2.waitKey (1)
    if key == 27: 
        break     

cap.release()
cv2.destroyAllWindows()
