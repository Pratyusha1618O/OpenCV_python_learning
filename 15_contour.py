import cv2 
img = cv2.imread('krishna.jpg') 
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval, thresh = cv2.threshold(gray_img, 127, 255, 0)

img_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

cv2.drawContours(img, img_contours, -1, (0, 255, 0))

cv2.imshow('Image Contours', img) 
cv2.waitKey(0)

