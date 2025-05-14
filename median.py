 import cv2
 import numpy as np
 i=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
 m=cv2.medianBlur(i,5)
 cv2.imshow("OI",i)
 cv2.imshow("M",m)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
