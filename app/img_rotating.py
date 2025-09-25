import cv2
import numpy as np

img = cv2.imread('images/test.jpg')
cv2.imshow('original image', img)
cv2.waitKey(0)

height, width = img.shape[:2]
center = (width / 2, height / 2)

#IMAGE ROTATING
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow('rotated image', rotated_img)
cv2.waitKey(0)

#IMAGE TRANSLATION
tx = width / 4
ty = height / 4
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)
translated_img = cv2.warpAffine(src=img, M=translation_matrix, dsize=(width, height))
cv2.imshow('translated image', translated_img)
cv2.waitKey(0)