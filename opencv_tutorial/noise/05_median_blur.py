import cv2 
img = cv2.imread("noisy.jpg") 
median_blur = cv2.medianBlur(img, 5)

cv2.imshow('Original Image', img) 
cv2.imshow('Blur Image', median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()