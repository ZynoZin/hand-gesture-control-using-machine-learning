# Hand Gesture Control Using Machine Learning

## Introduction
This work represents our final project for our first year in ENSIAS, it's about controlling an Arduino Uno robot using the Deeo Learning algorithm: CNN. This project can be used for other similar cases.

## Robot building
Upload the ```runTheMotors.ino``` to your Arduino Uno, make sure it's always ON as well as the bluetooth connected to it.

## Classes
### void
there are no hands in the frame, in this case the robot shouldn't do any changes to his actual state.
### Forward
The robot moves forward :raised_hand:
### Backward
The robot moves backwards :fist:
### Right
The robot goes right :thumbsdown:
### Left
The robot goes left :thumbsup:
### Stop
the robot stops :ok_hand:

## Model Structure
```py
model = Sequential()
model.add(Conv2D(64, (3,3), strides=(1, 1), input_shape = (100, 100, 1), padding='same', activation = 'relu'))
model.add(MaxPool2D((8,8)))
model.add(Conv2D(128, (3,3), activation = 'relu'))
model.add(Flatten())
model.add(Dense(6, activation = 'softmax'))
```
# Execution
Make sure your robot has a bluetooth connection, connect to it using your laptop or any PC that has a webcam. Check which ports the robot is connected to and change it's value in ```main.py``` here:
```py
serialcomm = Serial('COM6', 9600)
```
In our case, it's COM6.
Once it's done, execute the ```main.py```
### Windows:
```powershell
python .\main.py
```
### Linux/Mac:
```bash
python3 main.py
```
