Program: 
import cv2 
import numpy as np 
img = np.array([ 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0] 
], dtype=np.uint8) 
 
# Structuring elements (Kernel for hit-or-miss transform) 
hit_kernel = np.array([ 
    [0, 1, 0], 
    [1, -1, 1], 
    [0, 1, 0] 
], dtype=np.int8) 
 
# Apply hit-or-miss transform 
result = cv2.morphologyEx(img, cv2.MORPH_HITMISS, hit_kernel) 
 
print("Original Image:\n", img) 
print("Hit-or-Miss Transform Result:\n", result) 
