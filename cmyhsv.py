import cv2
import numpy as np
image = cv2.imread("img0.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
gray_rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray_image)
cv2.imshow("HSV", hsv_image)
cv2.imshow("Gray to RGB", gray_rgb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
