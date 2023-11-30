import cv2
 
cam = cv2.VideoCapture(0)
fps = 30
size = (int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)),
 int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
 
videoWriter = cv2.VideoWriter(
 'L200180136.mp4', cv2.VideoWriter_fourcc('X','V','I','D'),
 fps, size)
 
success, frame = cam.read()

numFramesRemaining = 10 * fps - 1

while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cam.read()
    numFramesRemaining -= 1
