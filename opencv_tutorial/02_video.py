import cv2

cap = cv2.VideoCapture(0) # 0 device index // default camera
print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = cap.read() # will return true if the frame is available

    # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.imshow('frame', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)# video in grayscale 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

