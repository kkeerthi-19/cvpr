import cv2
import numpy as np

image = cv2.imread('img0.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

low_threshold = 100
high_threshold = 200
edges = cv2.Canny(blurred_image, low_threshold, high_threshold)

cv2.imshow('Original Image', image)
cv2.imshow('Edge Detected Image', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
