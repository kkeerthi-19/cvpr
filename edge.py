import cv2
import numpy as np
img=cv2.imread('img.jpg',0)
sobel=cv2.sobel(img,cv2.cv_64F,1,0,ksize=3)
lap=cv2.laplacian(img, cv2.cv_64F)
pre=cv2.filter2D(img,-1,no.array([[1,0,-1],[1,0,-1],[1,0,-1]])
cv2.imshow('sobel',sobel)
cv2.imshow('laplace',lap)
cv2.imshow('prewittx', pre)
cv2.waiKey(0)
cv2.destroyAllWindows()
