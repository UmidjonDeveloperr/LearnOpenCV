import cv2
import numpy as np

img = cv2.imread('images/blob_image.jpg', cv2.IMREAD_GRAYSCALE)

params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 10
params.maxThreshold = 200

params.filterByArea = True
params.minArea = 1500

params.filterByCircularity = True
params.minCircularity = 0.1

params.filterByConvexity = True
params.minConvexity = 0.87

params.filterByInertia = True
params.minInertiaRatio = 0.01

ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(img)
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Img With Keypoints', img_with_keypoints)
cv2.waitKey()
cv2.destroyAllWindows()