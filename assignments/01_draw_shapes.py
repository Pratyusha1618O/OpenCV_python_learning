import cv2
import numpy as np

## Creating image
l = int(input("Enter canvas height: "))
b = int(input("Enter canvas width: "))
h = int(input("Enter canvas height: "))
img = np.ones([l,b,h])
# [length, breadth, height]
print(img.shape)


# Draw line
print("Draw a staright line: ")
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

img = cv2.line(img, (x1,y1), (x2, y2), (255, 0, 0), 5)
#line(img, (start coordinate), (end coordinate), (color), thickness)


## Draw rectangle
# x1,y1 -------
# |           |
# |           |
# |           |
# ---------x2,y2
print("Draw Rectangle: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

img = cv2.rectangle(img, (a,b), (c,d), (100,200,0), 4)
#When we give thickness -1 , the rectangle will fill with the color


## Draw Circle
print("Draw Circle")
r = int(input("Enter radius: "))
print("center point:")
x = int(input("Enter x: "))
y = int(input("Enter y: "))

img = cv2.circle(img, (x,y), r, (100, 0, 255), 4)
# circle(img, (center), radius, (color), thickness)


## Text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (200, 400), font, 4, (0,255,255), 10, cv2.LINE_AA)

cv2.imshow("Plygons", img)

cv2.waitKey(0)
cv2.destroyAllWindows()