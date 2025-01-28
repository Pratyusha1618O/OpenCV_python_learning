import cv2 
img = cv2.imread("krishna.jpg") 
blur_image = cv2.medianBlur(img,5)

cv2.imshow('Original Image', img) 
cv2.imshow('Blur Image', blur_image) 
cv2.waitKey(0) 