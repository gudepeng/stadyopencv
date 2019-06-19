import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)

# 图片翻转
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("first")

img1 = cv2.flip(img, 0)
plt.subplot(2, 2, 2)
plt.imshow(img1)
plt.title("x-flip")

img2 = cv2.flip(img, 1)
plt.subplot(2, 2, 3)
plt.imshow(img2)
plt.title("y-flip")

img3 = cv2.flip(img, -1)
plt.subplot(2, 2, 4)
plt.imshow(img3)
plt.title("xy-flip")

plt.show()

# 图片缩放1
img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
(h, w, c) = img.shape
dstHeight = int(h * 0.5)
dstWidth = int(w * 0.5)
dst = cv2.resize(img, (dstWidth, dstHeight))
cv2.imshow('img1', dst)
cv2.waitKey(0)

# 图片缩放2
img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstHeight = int(height / 2)
dstWidth = int(width / 2)
dstImage = np.zeros((dstHeight, dstWidth, 3), np.uint8)
for i in range(0, dstHeight):
    for j in range(0, dstWidth):
        iNew = int(i * (height * 1.0 / dstHeight))
        jNew = int(j * (width * 1.0 / dstWidth))
        dstImage[i, j] = img[iNew, jNew]
cv2.imshow('img2', dstImage)
cv2.waitKey(0)

# 图片缩放3
img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
(h, w, c) = img.shape
matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
dst = cv2.warpAffine(img, matScale, (int(w / 2), int(h / 2)))
cv2.imshow('dst', dst)
cv2.waitKey(0)

# 图片剪切
img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
print(img.shape)
dst = img[250:350, 10:350]
cv2.imshow('image', dst)
cv2.waitKey(0)

# 图像移位1
img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
(h, w, c) = img.shape
matShift = np.float32([[1, 0, 100], [0, 1, 200]])
dst = cv2.warpAffine(img, matShift, (h, w))
cv2.imshow('dst', dst)
cv2.waitKey(0)

# 图像移位2
img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
(h,w,c) = img.shape
dst = np.zeros(img.shape,np.uint8)
for i in range(0,h):
    for j in range(0,w-100):
        dst[i,j+100]=img[i,j]
cv2.imshow('image',dst)
cv2.waitKey(0)

# 仿射变换
img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
(h, w, c) = img.shape
matSrc = np.float32([[0, 0], [0, h - 1], [h - 1, 0]])
matDst = np.float32([[50, 50], [300, h - 200], [h - 300, 100]])
matAffine = cv2.getAffineTransform(matSrc, matDst)
dst = cv2.warpAffine(img, matAffine, (w, h))
cv2.imshow('dst', dst)
cv2.waitKey(0)
