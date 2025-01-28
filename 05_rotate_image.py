import cv2
img = cv2.imread("nobara.jpg")
print(type(img)) 
# <class 'numpy.ndarray'>
print(img.shape[0:2])

height, width = img.shape[0:2]

rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height)) 

cv2.imshow('Rotated Image', rotatedImage) 
cv2.waitKey(0)

cv2.destroyAllWindows()