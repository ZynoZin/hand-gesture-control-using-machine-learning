import glob
import cv2
import os
import csv

# Writing data to csv file
array_of_train_data = []
array_of_test_data = []
name = ""
dim = (100, 100)
train_data = ["label"]
test_data = ["label"]
# for train data
for i in range(0, 10000):
    train_data.append("pixel_" + str(i))
array_of_train_data.append(train_data)

for file in glob.glob("train/*"):
    img = cv2.imread(file)
    filename, file_extension = os.path.splitext(file)
    resized = cv2.resize(img, dim, interpolation=0)
    resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    name = filename.split('-')[0]
    label_name = name[6:]
    if(label_name == "null"):
        label_name = "background"
    data_in_line = resized.flatten()
    train_data = [label_name]
    for i in range(0, len(data_in_line)):
        train_data.append(data_in_line[i])
    array_of_train_data.append(train_data)

csv_filename = "data_train.csv"
with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(array_of_train_data)
print("done")

# for test data
for i in range(0, 10000):
    test_data.append("pixel_" + str(i))
array_of_test_data.append(test_data)
for file in glob.glob("test/*"):
    img = cv2.imread(file)
    filename, file_extension = os.path.splitext(file)
    resized = cv2.resize(img, dim, interpolation=0)
    resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    name = filename.split('-')[0]
    label_name = name[5:]
    if(label_name == "null"):
        label_name = "background"
    data_in_line = resized.flatten()
    test_data = [label_name]
    for i in range(0, len(data_in_line)):
        test_data.append(data_in_line[i])
    array_of_test_data.append(test_data)

csv_filename = "data_test.csv"
with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(array_of_test_data)
print("done")
