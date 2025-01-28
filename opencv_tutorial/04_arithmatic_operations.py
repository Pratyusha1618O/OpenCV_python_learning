import cv2

img = cv2.imread('flower.jpg')

print(img.shape) # (row, col, channel) // (675, 1200, 3)
print(img.size) # total no of pixel //2430000
print(img.dtype) # datatype # uint8
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

