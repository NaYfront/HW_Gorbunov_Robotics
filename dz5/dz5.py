import cv2
import matplotlib.pyplot as plt

default_file = 'map1.pgm'
src = cv2.imread(cv2.samples.findFile(default_file), cv2.IMREAD_GRAYSCALE)
gray_image = cv2.Canny(src, 50, 200, None, 3)
cdst = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
plt.figure(figsize=(15,15))
plt.imshow(cdst)
plt.title("map")