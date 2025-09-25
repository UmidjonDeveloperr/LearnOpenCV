import cv2

vid_capture = cv2.VideoCapture('videos/test_video.mp4')

if (vid_capture.isOpened() == False):
    print("Error opening the video file")
else:
    fps = vid_capture.get(5)
    print('Frames per second : ', fps, 'FPS')

    frame_count = vid_capture.get(7)
    print('Frame count : ', frame_count)

frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
fps = vid_capture.get(5)
output = cv2.VideoWriter('videos/output_video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, frame_size)

while (vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(20)
        output.write(frame)

        if key == ord('q'):
            break
    else:
        break
vid_capture.release()
output.release()
cv2.destroyAllWindows()