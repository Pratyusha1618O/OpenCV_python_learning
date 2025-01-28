import numpy as np
import cv2

# img = cv2.imread('whiteBoard.jpg',1)

## Creating image using numpy...................
img = np.zeros([600, 800, 3], np.uint8) 
# zeros([height, width, 3], datatype)

img = cv2.line(img, (0,0), (255, 255), (255,0,0), 5)
#line(img, (start coordinate), (end coordinate), (color), thickness)
img = cv2.arrowedLine(img, (0,255), (255, 255), (255,0,144), 5) #0,255 gives straight line


## Rectangle ##
# x1,y1 -------
# |           |
# |           |
# |           |
# ---------x2,y2

img = cv2.rectangle(img, (384,0), (510, 128), (0,0,255), 5)
img = cv2.rectangle(img, (384,0), (510, 128), (0,0,255), -1) 
#When we give thickness -1 , the rectangle will fill with the color

## CIrcle ##
img = cv2.circle(img, (255,255), 100, (122,0,144), 5)
# circle(img, (center), radius, (color), thickness)

## Text ##

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (200,400), font, 4, (0,255,255), 10, cv2.LINE_AA)
# putText(img, text, Point, fontFace, fontScale, color, thickness,lineType)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()