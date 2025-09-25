import cv2

src = cv2.imread('images/thresh_pic.jpg', cv2.IMREAD_GRAYSCALE)

#BINARY THRESHOLDING
thresh = 0
maxValue = 255
th, dist = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
cv2.imshow('Binary thresholded image', dist)
cv2.waitKey()
cv2.destroyAllWindows()

#INVERSE BINARY THRESHOLDING
thresh = 0
maxValue = 255
th, dist = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY_INV)
cv2.imshow('Inversed Binary thresholded image', dist)
cv2.waitKey()
cv2.destroyAllWindows()

#Truncate Thresholding
thresh = 100
maxValue = 255   #-----------------------> this will be ignored
th, dist = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TRUNC)
cv2.imshow('Truncate thresholded image', dist)
cv2.waitKey()
cv2.destroyAllWindows()

#Threshold to Zero
thresh = 200
maxValue = 255   #-----------------------> this will be ignored
th, dist = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO)
cv2.imshow('Threshold to Zero image', dist)
cv2.waitKey()
cv2.destroyAllWindows()

#Inverted Threshold to Zero
thresh = 100
maxValue = 255   #-----------------------> this will be ignored
th, dist = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TRUNC)
cv2.imshow('Inverted Threshold to Zero image', dist)
cv2.waitKey()
cv2.destroyAllWindows()