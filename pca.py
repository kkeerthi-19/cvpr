
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the image and convert to grayscale
image = cv2.imread("img0.jpg", cv2.IMREAD_GRAYSCALE)  # Replace with your image path

# Display original image size
print(f"Original Image Shape: {image.shape}")

# Normalize the image (optional, for better PCA performance)
image = image / 255.0

# Apply PCA for dimensionality reduction
pca = PCA(n_components=50)  # Adjust components (lower = more compression)
transformed = pca.fit_transform(image)  # Transform the image

# Reconstruct the image from the compressed version
reconstructed = pca.inverse_transform(transformed)

# Rescale image to 0-255 and convert to uint8
reconstructed = (reconstructed * 255).astype(np.uint8)

# Display original and PCA compressed images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(reconstructed, cmap='gray')
axes[1].set_title(f"PCA Compressed Image ({pca.n_components_} components)")
axes[1].axis("off")

plt.show()
