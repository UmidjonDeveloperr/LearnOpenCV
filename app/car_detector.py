import cv2
import numpy as np

cap = cv2.VideoCapture('videos/cars_video.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width,frame_height)
fps = cap.get(5)

frameId = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

frames = []
for fid in frameId:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(np.uint8)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
gray_median_frame = cv2.cvtColor(median_frame, cv2.COLOR_BGR2GRAY)

output_video = cv2.VideoWriter('videos/detected_cars_video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, frame_size)

ret = True
while ret:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dframe = cv2.absdiff(frame_gray, gray_median_frame)
    th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(image=dframe, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    frame_copy = frame.copy()

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        if w > 30 and h > 30:
            cv2.rectangle(frame_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('selected cars', frame_copy)
    key = cv2.waitKey(20)
    output_video.write(frame_copy)

    if key == 'q':
        break

cap.release()
output_video.release()
cv2.destroyAllWindows()




