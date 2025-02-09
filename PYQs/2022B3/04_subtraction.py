import cv2
import numpy as np

img1 = cv2.imread("pic.jpg")
img2 = cv2.imread("sudoku.png")

if img1 is None or img2 is None:
    print("Image not found")
    exit()

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

sub = cv2.absdiff(img1, img2)

cv2.imshow("subtract 2", sub)
# cv2.imshow("Subtract same", sub_same)


cv2.waitKey(0)
cv2.destroyAllWindows()
