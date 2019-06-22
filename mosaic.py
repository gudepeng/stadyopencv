import cv2

img = cv2.imread("./img/opencv.jpg", cv2.IMREAD_COLOR)
(h, w, c) = img.shape

for m in range(250, 350):
    for n in range(10, 350):
        if m % 5 == 0 and n % 5 == 0:
            for i in range(0, 5):
                for j in range(0, 5):
                    (b, g, r) = img[m, n]
                    img[i + m, j + n] = (b, g, r)
cv2.imshow('dst', img)
cv2.waitKey(0)
