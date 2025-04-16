import numpy as np
import cv2
import matplotlib.pyplot as plt

def marr_hildreth_edge_detection(image, sigma=1.0):
    gaussian = cv2.GaussianBlur(image, (5, 5), sigma)
    laplacian = cv2.Laplacian(gaussian, cv2.CV_64F)
    edges = ((laplacian < 0) & (cv2.dilate(laplacian, None) > 0)).astype(np.uint8) * 255
    return edges

image = cv2.imread('ika.jpg')
edges = marr_hildreth_edge_detection(image, sigma=1.5)

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Marr-Hildreth Edges")
plt.imshow(edges, cmap='gray')
plt.show()
