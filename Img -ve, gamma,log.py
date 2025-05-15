import cv2
import numpy as np
img=cv2.imread('img.jpg',0)
neg=255-img
logt=np.unit8(45*np.log1p(img))
gamma=np.array((255*img/255)**2.2, dtype='uint8'))
cv2.imshow('img neg', neg)
cv2.imshow('gamma', gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()
