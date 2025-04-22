 import cv2
 import numpy as np
 from skimage import exposure
 import matplotlib.pyplot as plt
 source = cv2.imread('img.jpg', 0)
 reference = cv2.imread('img4.jpg', 0)
 matched = exposure.match_histograms(source, reference)
 plt.figure(figsize=(12, 4))
 for i, img in enumerate([source, reference, matched], 1):
 plt.subplot(1, 3, i)
 plt.hist(img.ravel(), bins=256, range=[0, 256], color='gray')
 plt.title(['Source', 'Reference', 'Matched'][i-1])
 plt.xlabel('Pixel Intensity')
 plt.ylabel('Frequency')
 plt.tight_layout()
 plt.show()
 cv2.imshow('Source', source)
 cv2.imshow('Reference', reference)
 cv2.imshow("Matched", matched.astype("uint8"))
 cv2.waitKey(0)
 cv2.destroyAllWindows()
