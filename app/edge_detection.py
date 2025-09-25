import cv2

img = cv2.imread('images/tiger_image.jpg', cv2.IMREAD_GRAYSCALE)
img_blur = cv2.GaussianBlur(img, (5, 5), sigmaX=0, sigmaY=0)

#USING SOBEL
sobelx = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel XY', sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()

#USING CANNY
canny_edge = cv2.Canny(img_blur, 100, 200)
cv2.imshow('Canny Edge', canny_edge)
cv2.waitKey()
cv2.destroyAllWindows()
