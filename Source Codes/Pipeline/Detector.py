"""
Name:  Mayura Manawadu - 17/ENG/072
Detector with OpenCV dnn
"""

"""
This python script was developed as the detector of YOLO network in order to detect the objects. The purpose of 
developing the dectector was to determine the detections at YOLO head. And this model was used to experiemnt on the
speed of the network.
"""

# Importing necessary libraries
import colorsys
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import time


import numpy as np
from keras import backend as K
from keras.models import load_model
from keras.layers import Input
from configs.model import yolo_eval, yolo_body, tiny_yolo_body
from configs.utilities import image_preporcess


class YOLOv3Detector(object):
    _defaults = {
        "weightFIle": 'yolo_weights.h5',
        "anchorFile": 'yolo_anchors.txt',
        "classesFile": 'coco_classes.txt',
        "score" : 0.3,
        "iou" : 0.45,
        "inputImageSize" : (416, 416),
        "fontSize" : 1,
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Error '" + n + "'"


    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
        self.class_names = self._get_class()
        self.anchors = self._get_anchors()
        self.sess = K.get_session()
        self.boxes, self.scores, self.classes = self.generate()

#obtaining hte class names from the labeled class list
    def _get_class(self):
        classesFile = os.path.expanduser(self.classesFile)
        with open(classesFile) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        return class_names

#obtaining the anchor box sizes
    def _get_anchors(self):
        anchorFile = os.path.expanduser(self.anchorFile)
        with open(anchorFile) as f:
            anchors = f.readline()
        anchors = [float(x) for x in anchors.split(',')]
        return np.array(anchors).reshape(-1, 2)

#output generaor
    def generate(self):
        weightFIle = os.path.expanduser(self.weightFIle)
        assert weightFIle.endswith('.h5'), 'Must be a .h5 file.'

        num_anchors = len(self.anchors)
        num_classes = len(self.class_names)
        is_tiny_version = num_anchors==6 # default setting
        try:
            self.yolo_model = load_model(weightFIle, compile=False)
        except:
            self.yolo_model = tiny_yolo_body(Input(shape=(None,None,3)), num_anchors//2, num_classes) \
                if is_tiny_version else yolo_body(Input(shape=(None,None,3)), num_anchors//3, num_classes)
            self.yolo_model.load_weights(self.weightFIle) 
        else:
            assert self.yolo_model.layers[-1].output_shape[-1] == \
                num_anchors/len(self.yolo_model.output) * (num_classes + 5), \
                'Mismatch'

        # bounding boxes with colors
        hsv_tuples = [(x / len(self.class_names), 1., 1.)
                      for x in range(len(self.class_names))]
        self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
        self.colors = list(
            map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)),
                self.colors))

        np.random.shuffle(self.colors)

        #output tensor
        self.input_image_shape = K.placeholder(shape=(2, ))
        boxes, scores, classes = yolo_eval(self.yolo_model.output, self.anchors,
                len(self.class_names), self.input_image_shape,
                score_threshold=self.score, iou_threshold=self.iou)
        return boxes, scores, classes

    def detect_image(self, image):
        if self.inputImageSize != (None, None):
            assert self.inputImageSize[0]%32 == 0, 'Multiples of 32 required'
            assert self.inputImageSize[1]%32 == 0, 'Multiples of 32 required'
            boxed_image = image_preporcess(np.copy(image), tuple(reversed(self.inputImageSize)))
            image_data = boxed_image

        out_boxes, out_scores, out_classes = self.sess.run(
            [self.boxes, self.scores, self.classes],
            feed_dict={
                self.yolo_model.input: image_data,
                self.input_image_shape: [image.shape[0], image.shape[1]],#[image.size[1], image.size[0]],
                K.learning_phase(): 0
            })


        thickness = (image.shape[0] + image.shape[1]) // 600
        fontScale=1
        ObjectsList = []
        
        for i, c in reversed(list(enumerate(out_classes))):
            predicted_class = self.class_names[c]
            box = out_boxes[i]
            score = out_scores[i]

            label = '{} {:.2f}'.format(predicted_class, score)
            scores = '{:.2f}'.format(score)

            top, left, bottom, right = box
            top = max(0, np.floor(top + 0.5).astype('int32'))
            left = max(0, np.floor(left + 0.5).astype('int32'))
            bottom = min(image.shape[0], np.floor(bottom + 0.5).astype('int32'))
            right = min(image.shape[1], np.floor(right + 0.5).astype('int32'))

            mid_h = (bottom-top)/2+top
            mid_v = (right-left)/2+left
            #bounding boxes
            cv2.rectangle(image, (left, top), (right, bottom), self.colors[c], thickness)
            (test_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, thickness/self.text_size, 1)
            cv2.rectangle(image, (left, top), (left + test_width, top - text_height - baseline), self.colors[c], thickness=cv2.FILLED)
            cv2.putText(image, label, (left, top-2), cv2.FONT_HERSHEY_SIMPLEX, thickness/self.text_size, (0, 0, 0), 1)

            ObjectsList.append([top, left, bottom, right, mid_v, mid_h, label, scores])

        return image, ObjectsList

    def close_session(self):
        self.sess.close()

    def detect_img(self, image):
        original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        original_image_color = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        
        r_image, ObjectsList = self.detect_image(original_image_color)
        return r_image, ObjectsList

    
if __name__=="__main__":
    yolov3 = YOLOv3Detector()


    start_time = time.time()
    # output framrate withg 2 secons intervals
    display_time = 2

    fps = 0
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Error in WEBCAM")

    while True:
        ret, frame = cap.read()
        # resize our captured frame if we need
        frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)

        # detect object on our frame
        r_image, ObjectsList = yolov3.detect_img(frame)

        #output frames with detections
        cv2.imshow("Webcam feed", r_image)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

        # calculateing the FPS value
        fps += 1
        TIME = time.time() - start_time
        if TIME > display_time:
            print("FPS:", fps / TIME)
            fps = 0 
            start_time = time.time()



    cap.release()
    cv2.destroyAllWindows()
    yolov3.close_session()
