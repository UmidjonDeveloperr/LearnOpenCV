import cv2

img = cv2.imread('images/test.jpg')
top_left_corner, bottom_right_corner = [], []

#USING MOUSE CALLBACK
# def drawrectangle(action, x, y, flags, *userdata):
#     global top_left_corner, bottom_right_corner
#
#     if action == cv2.EVENT_LBUTTONDOWN:
#         top_left_corner = [(x, y)]
#     elif action == cv2.EVENT_LBUTTONUP:
#         bottom_right_corner = [(x, y)]
#         cv2.rectangle(img, top_left_corner[0], bottom_right_corner[0], (0, 255, 0), 2)
#         cv2.imshow('Window', img)
#
# img_copy = img.copy()
# cv2.namedWindow('Window')
# cv2.setMouseCallback('Window', drawrectangle)
#
# k = 0
# while k != 113:
#     cv2.imshow('Window', img_copy)
#     k = cv2.waitKey(0)
#     if k == 99:
#         image = img.copy()
#         cv2.imshow('Window', image)
# cv2.destroyAllWindows()


#USING TRACKBAR
max_scale_up = 100
scale_factor = 1
window_name = "Resized image"
trackbar_value = "Scale"

cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

def scale(*args):
    scale_factor = 1 + args[0] / 100.0
    scaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(window_name, scaled_img)

cv2.createTrackbar(trackbar_value, window_name, max_scale_up, 100, scale)
cv2.imshow(window_name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()












