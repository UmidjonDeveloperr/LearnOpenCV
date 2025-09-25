import cv2
import numpy as np

cap = cv2.VideoCapture('videos/cars_video.mp4')

frameId = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

frames = []
for fid in frameId:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(np.uint8)

cv2.imshow('Median frame', median_frame)
cv2.waitKey()
cv2.destroyAllWindows()

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
gray_median_frame = cv2.cvtColor(median_frame, cv2.COLOR_BGR2GRAY)

ret = True
while ret:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dframe = cv2.absdiff(frame, gray_median_frame)
    th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow('frame', dframe)
    cv2.waitKey(20)

cap.release()
cv2.destroyAllWindows()