import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
f = cv2.imread('imgg.jpg')

# Convert the original image to grayscale
gray_image = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)

# Apply Marr-Hildreth edge detection using LoG filter
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
laplacian_abs = np.absolute(laplacian)
marr_hildreth_e = cv2.convertScaleAbs(laplacian_abs)

# Define the random constant c
c = 1

# Perform the element-wise addition for Marr-Hildreth
g_marr_hildreth = cv2.add(f, cv2.merge([marr_hildreth_e] * 3) * c)
g_marr_hildreth = np.clip(g_marr_hildreth, 0, 255).astype(np.uint8)

# Display the images
plt.figure(figsize=(8, 6))

# Display the original image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Display the generated Marr-Hildreth edge detection image
plt.subplot(2, 2, 2)
plt.imshow(marr_hildreth_e, cmap='gray')
plt.title('Generated Marr-Hildreth Edge Detection')
plt.axis('off')

# Display the generated output image for Marr-Hildreth
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(g_marr_hildreth, cv2.COLOR_BGR2RGB))
plt.title('Output Image (Marr-Hildreth)')
plt.axis('off')

# Adjust spacing between images
plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.tight_layout()
plt.show()