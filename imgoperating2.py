import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("first")

(B, G, R) = cv2.split(img)

plt.subplot(2, 2, 2)
plt.imshow(B)
plt.title("b")

plt.subplot(2, 2, 3)
plt.imshow(G)
plt.title("g")

plt.subplot(2, 2, 4)
plt.imshow(img[:, :, 2])
plt.title("r")
plt.show()

newimg = cv2.merge([B, G, R])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

(h, w, c) = img.shape
print(h, w, c)
zero = np.zeros(img.shape, dtype=np.uint8)

cv2.mixChannels([img], [zero], [0, 0, 1, 1, 2, 2])

cv2.imshow("newimg",zero)
cv2.waitKey(0)
cv2.destroyAllWindows()
