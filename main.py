
import cv2
from tensorflow import keras
import numpy as np
import imutils
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
    if(frame_count % 15 == 0):
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
            if prediction_c == 0:
                print("backward")
            elif prediction_c == 1:
                print("forward")
            elif prediction_c == 3:
                print("left")
            elif prediction_c == 2:
                print("right")
            elif prediction_c == 4:
                print("stop")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
