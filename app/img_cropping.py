import cv2

img = cv2.imread('images/test.jpg')
img_copy = img.copy()
img_height, img_width = img.shape[:2]

M = 76
N = 104
x1 = 0
y1 = 0

for y in range(0, img_height, M):
    for x in range(0, img_width, N):
        if img_height-y < M or img_width - x < N:
            break

        y1 = y + M
        x1 = x + N

        if x1 >= img_width and y1 >= img_height:
            x1 = img_width - 1
            y1 = img_height - 1
            tiles = img_copy[y:y + M, x:x + N]
            cv2.imwrite('cropped_images/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 1)
        elif y1 >= img_height:
            y1 = img_height - 1
            tiles = img_copy[y:y + M, x:x + N]
            cv2.imwrite('cropped_images/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 1)
        elif x1 >= img_width:
            x1 = img_width - 1
            tiles = img_copy[y:y + M, x:x + N]
            cv2.imwrite('cropped_images/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 1)
        else:
            tiles = img_copy[y:y + M, x:x + N]
            cv2.imwrite('cropped_images/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()









