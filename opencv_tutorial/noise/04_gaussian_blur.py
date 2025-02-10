import cv2 
img = cv2.imread("noisy.jpg") 
gaussian_blur = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow('Original Image', img) 

cv2.imshow('Blur Image', gaussian_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()