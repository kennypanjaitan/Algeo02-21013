import cv2
cam = cv2.VideoCapture()

while True:
    retV, frame = cam.read()
    cv2.imshow('Webcamku', frame)
    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
cam.release()
cv2.destroyAllWindows()