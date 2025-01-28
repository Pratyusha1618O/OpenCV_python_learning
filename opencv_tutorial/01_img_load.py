import cv2

img = cv2.imread('nobara2.jpg',1)
# img2 = cv2.imread('nobara2.jpg',0) #grayscale

print(img)
cv2.imshow('Nobara',img)
# cv2.waitKey(2000) #2000ms or 2sec
cv2.waitKey(0) #window will not disappear
cv2.destroyAllWindows()

cv2.imwrite('Nobara_copy.jpg', img) #Nobara_copy.jpg will be created

