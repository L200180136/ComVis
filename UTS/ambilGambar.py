import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow('Camera')
success, frame = cam.read()
cv2.imshow('Camera',frame)

while (True):
    key = cv2.waitKey(1)
    if key == 32:
        cv2.imwrite('L200180136.jpg', frame)
    elif key == 27:
        cv2.destroyWindow('Camera')
        cam.release() 




