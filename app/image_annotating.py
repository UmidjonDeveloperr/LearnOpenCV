import cv2

img = cv2.imread('images/test.jpg')
cv2.imshow('original image', img)
cv2.waitKey(0)

# #DRAW LINE
img_copy = img.copy()
pointA = (400, 160)
pointB = (950, 160)
cv2.line(img_copy, pointA, pointB, color=(0, 0, 255), thickness=2)
cv2.imshow('lined image', img_copy)
cv2.waitKey(0)

# #DRAW A CIRCLE
circle_copy = img.copy()
circle_center = (int(img.shape[1]/2), int(img.shape[0]/2))
radius = 170
cv2.circle(circle_copy, circle_center, radius, (0, 0, 255), thickness=2)
cv2.imshow('circle image', circle_copy)
cv2.waitKey(0)

# #FILLING CIRCLE
filled_circle = img.copy()
circle_center = (int(img.shape[1]/2), int(img.shape[0]/2))
radius = 170
cv2.circle(filled_circle, circle_center, radius, (0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)
cv2.imshow('circle image', filled_circle)
cv2.waitKey(0)

# #DRAWING RECTANGLE
rectangle_copy = img.copy()
point_a = (400, 120)
point_b = (950, 460)
cv2.rectangle(rectangle_copy, point_a, point_b, (0, 0, 255), thickness=2)
cv2.imshow('rectangle image', rectangle_copy)
cv2.waitKey(0)

#DRAWING ELLIPSE
ellipse_copy = img.copy()
ellipse_center = (int(img.shape[1]/2), int(img.shape[0]/2))
axis1 = (400, 120)
axis2 = (300, 120)
cv2.ellipse(ellipse_copy, ellipse_center, axis1, 0, 180, 360, (0, 0, 255), thickness=2)
cv2.ellipse(ellipse_copy, ellipse_center, axis1, 0, 0, 180, (0, 255, 0), thickness=-2)
cv2.imshow('ellipse image', ellipse_copy)
cv2.waitKey(0)

#PUTTING TEXT
text_img = img.copy()
text = 'It is a happy tree'
org = (50, 350)
cv2.putText(text_img, text, org, cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
cv2.imshow('text image', text_img)
cv2.waitKey(0)