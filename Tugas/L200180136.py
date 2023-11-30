import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while(cam.isOpened):      
    _,frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 1.45)
    canny = cv2.Canny(blur, 50, 75)

    _,thresh = cv2.threshold(canny,255,255,255)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    color = cv2.cvtColor(canny, cv2.COLOR_GRAY2RGB)
    cnt = contours[-4]
    con1 = cv2.drawContours(color, [cnt], 0, (215, 0, 0), 1)
    con2 = cv2.drawContours(color, contours, 2, (0, 215, 0), 1)
    con3 = cv2.drawContours(color, contours, 0, (0, 0, 215), 1)
    con = con1 + con2 + con3 
    
    cv2.imshow("Frame Utama",frame)
    cv2.imshow("Draw Constours", con)

    key = cv2.waitKey (1)
    if key == 27: 
        break     

cam.release()
cv2.destroyAllWindows()
