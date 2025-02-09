import cv2
import numpy as np

img = cv2.imread("pic.jpg", 0)

gamma = 1.5
gamma_corrected = np.uint8(255 * (img/255) ** gamma) ## power law transformation

diff = cv2.absdiff(img, gamma_corrected)

cv2.imshow("Original", img)
cv2.imshow("Gamma Corrected", gamma_corrected)
cv2.imshow("Difference", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()