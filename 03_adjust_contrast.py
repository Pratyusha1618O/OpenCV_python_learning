import cv2 
import numpy as np 

img = cv2.imread("rgb.png")

contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0) 
cv2.imshow('Original Image', img) 
cv2.imshow('Contrast Image', contrast_img) 
cv2.waitKey(0)

cv2.destroyAllWindows()

# In the above code, the brightness is set to 0 as we 
# only want to apply contrast.