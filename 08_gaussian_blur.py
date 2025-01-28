import cv2 
img = cv2.imread("krishna.jpg") 
blur_image = cv2.GaussianBlur(img, (7,7), 0) 
cv2.imshow('Original Image', img) 
cv2.imshow('Blur Image', blur_image) 
cv2.waitKey(0)