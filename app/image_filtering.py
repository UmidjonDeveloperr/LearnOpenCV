import cv2
import numpy as np

image = cv2.imread('images/test.jpg')

kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)

cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()

# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()

#APPLY BUILT-IN FUNCTION
img2 = cv2.blur(image, (5, 5))
cv2.imshow('Blurred using built in function', img2)
cv2.waitKey()
cv2.destroyAllWindows()

#APPLY GaussianBlur
img3 = cv2.GaussianBlur(image, (5, 5), sigmaX=0, sigmaY=0)
cv2.imshow('Gaussian Blur', img3)
cv2.waitKey()
cv2.destroyAllWindows()

#APPLY MEDIAN-BLUR
img4 = cv2.medianBlur(image, 5)
cv2.imshow('Median Blur', img4)
cv2.waitKey()
cv2.destroyAllWindows()

#SHARPENING THE IMAGE
kernel3 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharp_img = cv2.filter2D(image, -1, kernel3)
cv2.imshow('Sharpened image', sharp_img)
cv2.waitKey()
cv2.destroyAllWindows()

#BLATERAL FILTERING IMAGE
bl_img = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral filter', bl_img)
cv2.waitKey()
cv2.destroyAllWindows()