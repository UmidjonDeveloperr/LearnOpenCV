import cv2
import numpy as np

img = cv2.imread('images/shapes_2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
img_copy = img.copy()
cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2, lineType=cv2.LINE_AA)

for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    vertices = len(approx)

    if vertices == 4:
        shape = 'RECTANGLE'
    elif vertices == 3:
        shape = 'TRIANGLE'
    elif vertices == 5:
        shape = 'PENTAGON'
    elif vertices == 6:
        shape = 'HEXAGON'
    elif vertices == 8:
        shape = 'OCTAGON'
    else:
        shape = 'CIRCLE'

    x, y, w, h = cv2.boundingRect(approx)
    text_x = x
    text_y = y + h + 25

    cv2.drawContours(img_copy, contour, -1, (0, 255, 0), 2, lineType=cv2.LINE_AA)
    cv2.putText(img_copy, shape, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow('Detected shapes', img_copy)
cv2.imwrite('images/shapes_2_detected.jpg', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()