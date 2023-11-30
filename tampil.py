import cv2
import numpy as np

img = cv2.imread('example.png')
cv2.imshow('example.png',img)
cv2.waitKey()
cv2.destroyAllWindows()
