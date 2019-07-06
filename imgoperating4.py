import numpy as np
import cv2

# 创建一张黑色的图像
img = np.zeros((500, 500, 3), np.uint8)
# 画线
img = cv2.line(img, (0, 0), (500, 500), (125, 125, 125), 2)
# 画矩形
img = cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 2)
# 画圆
img = cv2.circle(img, (250, 250), 50, (0, 0, 255), -1)
# 画椭圆
img = cv2.ellipse(img, (250, 250), (100, 50), 0, 0, 360, (0, 255, 255), -1)
# 画多边形
pts = np.array([[100, 100], [200, 300], [400, 500]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (255, 0, 255))
#画填充多边形
pts1 = np.array([[0, 00], [100, 200], [200, 200]], np.int32)
pts1= pts1.reshape((-1, 1, 2))
img = cv2.fillPoly(img, [np.array(pts1, np.int32)], (255, 255, 255))

# 画文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello OpenCV', (0, 250), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()