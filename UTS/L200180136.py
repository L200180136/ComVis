import cv2 #1

cam = cv2.VideoCapture(0) #2

while (cam.isOpened): #3

    _,frame = cam.read() #4
    canny = cv2.Canny(frame, 50, 75) #5
    
    cv2.imshow("Frame", canny) #6

    key = cv2.waitKey(1) #7
    if key == 27: #8
        break #9

cam.release()  #10
cv2.destroyAllWindows() #11
