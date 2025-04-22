 import numpy as np, cv2, matplotlib.pyplot as plt
 from sklearn.decomposition import PCA
 img = cv2.imread('img.jpg', 0)
 rec = PCA(10).fit_transform(img)
 img_rec = PCA(10).fit(img).inverse_transform(rec)
 img_rec = np.uint8(np.clip(img_rec, 0, 255))
 plt.imshow(np.hstack([img, img_rec]), cmap='gray')
 plt.title("Original | PCA Reconstructed")
 plt.axis('off')
 plt.show()
