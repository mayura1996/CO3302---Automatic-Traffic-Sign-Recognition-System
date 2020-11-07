import json
import csv
import numpy as np
import shutil
import os

directory = r'E:\Sub set\annotations'  # directory containg
directory1 = r'E:\Dataset\annotations'
directory2 = r'E:\Dataset\images'
os.chdir(r'C:\Users\ASUS')
classlist = []  # to store the list of all the available classes in the dataset
a_file = open("sample.csv", "w")
writer = csv.writer(a_file)

count = 0

############################################################

classNameDict = {}  # holds the generalized class names and their annotations (filtering from the mapillary dataset which is of 50,000 images)

file1 = open(r'E:\Sub set\namelist40.txt', 'r')
classNames = file1.readlines()

file2 = open(r'E:\Sub set\idices40.txt', 'r')
indices = file2.readlines()

classNameArray = []
i = 0

for className in classNames:
    classNameArray.append(className[:-1])

for index in indices:
    classNameDict.update({classNameArray[i]: index[:-1]})  # holding class name and the generalized annotation valie
    i += 1

# print(classNameDict)
fileCount = 0

classCount = []

for i in range(11):
    classCount.append(0)

print(classCount)

finalList = []
###########################################################
# wrting to csv
for filename1 in os.listdir(directory1):
    if filename1.endswith(".json"):
        for filename2 in os.listdir(directory2):
            if (filename1[:-5] == filename2[:-4]):
                # print("yes")

                with open(os.path.join(directory1, filename1)) as json_file:
                    data = json.load(json_file)

                employee_data = data['objects']

                for emp in employee_data:
                    for temp in classNameDict:
                        if (emp['label'][:-4] == temp):
                            if classCount[int(classNameDict[temp])] <= 1999:
                                os.chdir(r'E:\Dataset\annotations')
                                classCount[int(classNameDict[temp])] += 1
                                print(classCount)
                                newPath = shutil.copy(filename1, 'E:\Sub set\Annotations')
                                os.chdir(r'E:\Dataset\images')
                                newPath = shutil.copy(filename2, 'E:\Sub set\images')
                                emp['bbox'].update({'label': classNameDict[temp]})
                                emp['bbox'].update({'filename': filename1})
                                if count == 0:
                                    emp.update({'before': 23})
                                    header = emp['bbox'].keys()
                                    os.chdir(r'C:\Users\ASUS')
                                    writer.writerow(header)
                                    count += 1
                                os.chdir(r'C:\Users\ASUS')
                                writer.writerow(emp['bbox'].values())

    else:
        continue
    exitVariable = 1
    for i in range(11):
        if classCount[i] != 2000:
            exitVariable = 0
    if (exitVariable):
        # csv_writer.close()
        a_file.close()
        break
