"""
Name:  Mayura Manawadu - 17/ENG/072
Detector with OpenCV dnn
"""

# Importing necessary libraries
import numpy as np
import cv2
import time

"""
Input video -> please rename the video file according to the input
"""

video = cv2.VideoCapture('videos/traffic-cars.mp4')

writer = None
h, w = None, None

"""
Loading YOLOV3 network - Here before training the traffic signs I used this model to check the speed of detections
Therefore I have used the COCO dataset's weights
"""

with open('yolo-coco-data/coco.names') as f:
    labels = [line.strip() for line in f]


"""
Loading coco weights to the YOLOv3 Objects Detector
"""

network = cv2.dnn.readNetFromDarknet('yolo-coco-data/yolov3.cfg',
                                     'yolo-coco-data/yolov3.weights')

all_layers = network.getLayerNames()

"""
# taking the output layers of the yolo network 82,94,106
"""


layers_names_output = \
    [all_layers[i[0] - 1] for i in network.getUnconnectedOutLayers()]

probability_minimum = 0.5

thresh = 0.3

colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

"""
Reading frames
"""
f = 0
t = 0

while True:
    ret, frame = video.read()
    if not ret:
        break
    # Reading dimensions of the frames
    if w is None or h is None:
        h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)


    # passing the blob through input layers
    network.setInput(blob)
    start = time.time()
    output_from_network = network.forward(layers_names_output)
    end = time.time()

    f += 1
    t += end - start

    boundingBoxes = []
    confidences = []
    classIndex = []

    # Going through output layers
    for result in output_from_network:
        # Going through all detections in the output layer
        for detected_objects in result:
            # Getting 80 classes of COCO datatset
            scores = detected_objects[5:]
            currentClass = np.argmax(scores)
            confidence_current = scores[currentClass]

            if confidence_current > probability_minimum:
                box_current = detected_objects[0:4] * np.array([w, h, w, h])
                x_center, y_center, box_width, box_height = box_current
                x_min = int(x_center - (box_width / 2))
                y_min = int(y_center - (box_height / 2))
                boundingBoxes.append([x_min, y_min,
                                       int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                classIndex.append(currentClass)

    results = cv2.dnn.NMSBoxes(boundingBoxes, confidences,
                               probability_minimum, thresh)

    if len(results) > 0:
        for i in results.flatten():
            x_min, y_min = boundingBoxes[i][0], boundingBoxes[i][1]
            box_width, box_height = boundingBoxes[i][2], boundingBoxes[i][3]
            currentBBox = colours[classIndex[i]].tolist()
            cv2.rectangle(frame, (x_min, y_min),
                          (x_min + box_width, y_min + box_height),
                          currentBBox, 2)
            text_box_current = '{}: {:.4f}'.format(labels[int(classIndex[i])],
                                                   confidences[i])
            cv2.putText(frame, text_box_current, (x_min, y_min - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, currentBBox, 2)
    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter('videos/result-traffic-cars.mp4', fourcc, 30,
                                 (frame.shape[1], frame.shape[0]), True)
    writer.write(frame)


print('\nTotal number of frames', f)
print('Total amount of time taken {:.5f} seconds'.format(t))
print('FPS:', round((f / t), 1))


video.release()
writer.release()