import cv2

img = cv2.imread('images/test.jpg', cv2.IMREAD_UNCHANGED)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

img_copy = img.copy()
cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2, lineType=cv2.LINE_AA)
cv2.imshow('None approximation', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()