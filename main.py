import cv2
from tensorflow import keras
import numpy as np

model = keras.models.load_model('/home/xdevelynnx/Desktop/HGR_CNN.h5')
vid = cv2.VideoCapture(0)
dim = (30, 30)
frame_count = 0

while(True):
	ret, frame = vid.read()
	cv2.imshow('frame', frame)
	frame_count += 1

	if frame_count % 5 == 0:	
		resized = frame
		resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
		resized = cv2.resize(resized, dim, interpolation=0)
		resized= resized.reshape(-1,30,30,1)
		prediction_c = model.predict_classes(resized)
		#0= backward - 1 = forward - 2 = left - 3 = right - 4 = stop 
		if prediction_c == 0:
			print("backward")
		elif prediction_c ==1:
			print("forward")
		elif prediction_c == 2:
			print("left")
		elif prediction_c == 3:
			print("right")
		else :
			print("stop")

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
vid.release()
cv2.destroyAllWindows()
