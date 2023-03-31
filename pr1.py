import cv2
import numpy as np
import time

t0 = time.time()

cap = cv2.VideoCapture(0)  # 0 coresponds to the laptop webcam and 1 to the one from USB

# cap is an object and VideoCapture is a class
# the cap's method has two output: ret and frame

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
fps = cap.get(cv2.CAP_PROP_FPS)
print(width, height, fps) # frame per second
# quit()

while True:
	ret, frame = cap.read()
	if ret:
		t1 = time.time() - t0
		frame = cv2.flip(frame, 1) # move column by 180 deg
		t1_str = str(round(t1, 2))
		cv2.putText(frame, t1_str, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, \
		1, (0, 0, 255), 1)
		#cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA, True)

		#frame_little = frame[200: 300, 200:400]
		#frame = 255 - frame # change each pixel
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow("myWebcam", frame)
		q = cv2.waitKey(1)
		if q == ord("q"):
			break

cv2.destroyAllWindows() # this function allows users to destroy or close all windows at any time after exiting the script.
cap.release() # close cap


