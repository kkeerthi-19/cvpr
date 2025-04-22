import cv2 
import numpy as np 
 
image = cv2.imread('image2.jpg') 
kernel = np.ones((3, 3), np.uint8) 
dilated = cv2.dilate(image, kernel, iterations=1) 
eroded = cv2.erode(image, kernel, iterations=1) 
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel) 
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) 
 
cv2.imshow('Original Image', cv2.resize(image, (500, 350))) 
cv2.imshow('Dilated Image', cv2.resize(dilated, (500, 350))) 
cv2.imshow('Eroded Image', cv2.resize(eroded, (500, 350))) 
cv2.imshow('Opened Image', cv2.resize(opened, (500, 350))) 
cv2.imshow('Closed Image', cv2.resize(closed, (500, 350))) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
