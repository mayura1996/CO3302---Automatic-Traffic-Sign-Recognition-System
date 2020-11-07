"""
Name:  Mayura Manawadu - 17/ENG/072
Detector with OpenCV dnn
"""


# Importing needed library
import os
import random

full_path_to_images = '/media/manawadu/New Volume/Sub set/images'

os.chdir(full_path_to_images)

p = []
#reding images from the path
for current_dir, dirs, files in os.walk('.'):
    for f in files:
         if f.endswith('.jpg'):
            path_to_save_into_txt_files = '/media/manawadu/New Volume/Sub set/images' + '/' + f
            p.append(path_to_save_into_txt_files + '\n')

#shuffling the readed list of images
random.shuffle(p)

#splitting the images in to ratio of 85% to 15% for train and test sets
p_test = p[:int(len(p) * 0.15)]

p = p[int(len(p) * 0.15):]

with open('train.txt', 'w') as train_txt:
    for e in p:
        train_txt.write(e)

with open('test.txt', 'w') as test_txt:
    for e in p_test:
        test_txt.write(e)

