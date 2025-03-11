import cv2
import numpy as np
def add_title(image, title):
  canvas=cv2.copyMakeBorder(image, 50, 0, 0, 0, cv2.BORDER_CONSTANT, value=0)
  cv2.puttext(canvas, title, (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
  cv2.LINE_AA)
  return canvas
def main():
  image_path='img0.jpg'
  image=cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  if image is None:
  print("Error: Image not found!")
  return
  avg_filtered=cv2.blur(image,(5,5))
  gaussian_filtered=cv2.GaussianBlur(image, (5,5), 1)
  median_filtered=cv2.medianBlur(image, 5)
  original_with_title=add_title(image, "Original Img")
  avg_with_title=add_title(avg_filtered, "Averaging filt")
  gaussian_with_title=add_title(gaussian_filtered, "Gaussian")
  median_with_title=add_title(median_filtered, "Median")
  images=[original_with_title, avg_with_title, gaussian_with_title, median_with_title]
  max_height=max(img.shape[0] for img in images)
  resized_images=[cv2.resize(img, (int(img.shape[1]*max_height/img.shape[0]), max_height),
  interpolation=cv2.INTER_AREA)
  for img in images]
  combined=np.hstack(resized_images)
  cv2.imshow("Image smoothing: Linear and Nonlinear Filters", combined)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
if __name__=="__main__":
main()
