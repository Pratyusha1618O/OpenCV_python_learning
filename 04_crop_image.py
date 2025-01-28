import cv2 
img = cv2.imread("nobara.jpg") 
height, width = img.shape[0:2] 

startRow = int(height*.15) 
startCol = int(width*.15) 
endRow = int(height*.85) 
endCol = int(width*.85)

croppedImage = img[startRow:endRow, startCol:endCol]

cv2.imshow('Original Image', img) 
cv2.imshow('Cropped Image', croppedImage) 
cv2.waitKey(0)

cv2.destroyAllWindows()