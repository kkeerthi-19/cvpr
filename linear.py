import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
average = cv2.blur(img, (5, 5))                
gaussian = cv2.GaussianBlur(img, (5, 5), 0)    
median = cv2.medianBlur(img, 5)                

titles = ['Original', 'Averaging', 'Gaussian', 'Median']
images = [img, average, gaussian, median]

plt.figure(figsize=(12, 6))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
