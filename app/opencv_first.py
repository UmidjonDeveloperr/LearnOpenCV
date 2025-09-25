import cv2
import numpy as np

img_grayscale = cv2.imread('images/test.jpg', 0)

cv2.imshow('grayscale image, original', img_grayscale)
cv2.waitKey(0)

down_width = 300
down_height = 200
down_points = (down_width, down_height)
down_sized_image = cv2.resize(img_grayscale, down_points, interpolation=cv2.INTER_LINEAR)
cv2.imshow('down sized image', down_sized_image)
cv2.waitKey(0)

scale_down = 0.7
scale_down_image = cv2.resize(img_grayscale, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
cv2.imshow('down scaled image', scale_down_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('../grayscale.jpg', img_grayscale)