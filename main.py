import cv2
from tensorflow import keras
import numpy as np
import imutils
from serial import Serial
import time
serialcomm = Serial('COM6', 9600)
serialcomm.timeout = 1
model = keras.models.load_model('./HGR_CNN.h5')
camera = cv2.VideoCapture(0)
dim = (100, 100)
frame_count = 0
previous_prediction_c = 0
while(True):
    frame_count += 1
    _, img = camera.read()
    img = imutils.resize(img, width=1000)
    box = np.array([50, 50, 350, 350])
    (startX, startY, endX, endY) = box.astype("int")
    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 1)
    cv2.imshow('img', img)
    if(frame_count % 20 == 0):
        crop_img = img[50:350, 50:350]
        resized = crop_img
        resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(resized, dim, interpolation=0)
        resized = resized / 255.0
        resized = resized.reshape(-1, 100, 100, 1)
        prediction_c = model.predict_classes(resized)
        # 0= backward - 1 = forward - 2 = left - 3 = right - 4 = stop
        if(prediction_c != previous_prediction_c):
            previous_prediction_c = prediction_c
            i = f"{prediction_c[0]}"
            serialcomm.write(i.encode())
            time.sleep(0.5)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        i = '5'
        serialcomm.write(i.encode())
        time.sleep(1)
        break
camera.release()
serialcomm.close()
cv2.destroyAllWindows()
