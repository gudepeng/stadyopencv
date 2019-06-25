import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('./img/g.jpg', 0)
# kernel = np.ones((15, 15), np.uint8)
# erosion = cv2.erode(img, kernel)
# dilate = cv2.dilate(img, kernel)
#
# kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (15, 15))
# dilate1 = cv2.dilate(img, kernel1)
#
# plt.subplot(2, 2, 1)
# plt.imshow(img, "gray")
# plt.title("img")
#
# plt.subplot(2, 2, 2)
# plt.imshow(erosion, "gray")
# plt.title("erosion")
#
# plt.subplot(2, 2, 3)
# plt.imshow(dilate, "gray")
# plt.title("dilate")
#
# plt.subplot(2, 2, 4)
# plt.imshow(dilate1, "gray")
# plt.title("dilate1")
#
# plt.show()


# img = cv2.imread('./img/g1.jpg', 0)
# kernel = np.ones((5, 5), np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# cv2.imshow("opening", opening)
# cv2.waitKey(0)
#
# img = cv2.imread('./img/g2.jpg', 0)
# kernel = np.ones((5, 5), np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("opening", opening)
# cv2.waitKey(0)
#
img = cv2.imread('./img/g.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("gradient", gradient)
cv2.waitKey(0)

img = cv2.imread('./img/g.jpg', 0)
kernel = np.ones((10, 5), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("tophat", tophat)
cv2.waitKey(0)

img = cv2.imread('./img/g.jpg', 0)
kernel = np.ones((10, 5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("tophat", blackhat)
cv2.waitKey(0)
