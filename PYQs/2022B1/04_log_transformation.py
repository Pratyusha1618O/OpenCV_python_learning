import cv2
import numpy as np

img = cv2.imread("flower.jpg",0)

# apply log transformation: s = c*log(1+r)
c = 255 / np.log(1 + np.max(img))
log_transformed = c * np.log(1 + img.astype(np.float32))
log_transformed = np.uint8(log_transformed)

#subtract
sub = cv2.absdiff(img, log_transformed)

cv2.imshow("Original image", img)
cv2.imshow("Log transformed image", log_transformed)
cv2.imshow("Diff", sub)


cv2.waitKey(0)
cv2.destroyAllWindows()
