import cv2
import numpy as np
import matplotlib.pyplot as plt
def hist_match(source, reference):
 src_hist, bins = np.histogram(source.flatten(), 256, [0, 256])
 ref_hist, _ = np.histogram(reference.flatten(), 256, [0, 256])
 src_cdf = np.cumsum(src_hist) / src_hist.sum()
 ref_cdf = np.cumsum(ref_hist) / ref_hist.sum()
 mapping = np.interp(src_cdf, ref_cdf, np.arange(256))
 matched_image = np.interp(source.flatten(), np.arange(256),
mapping).reshape(source.shape)
 return np.uint8(matched_image)
source_image = cv2.imread("src.jpg")
reference_image = cv2.imread("ref.jpg")
#source_image_gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
#reference_image_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
result_image = hist_match(source_image, reference_image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Source Image (Grayscale)')
plt.imshow(source_image, cmap='gray')
plt.subplot(1, 3, 2)
plt.title('Reference Image (Grayscale)')
plt.imshow(reference_image, cmap='gray')
plt.subplot(1, 3, 3)
plt.title('Matched Image')
plt.imshow(result_image, cmap='gray')
plt.show()
