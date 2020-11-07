import csv
import cv2
import shutil
import os
import glob

os.chdir(r'E:\Sub set\YOLO Annotations')  # the directory containing your .jpegs

directory2 = r'E:\Dataset\images'

with open('Book2.csv') as csvFile:  # Open CSV file to read CSV, note: reading and write file should be under "with"

    readCsv = csv.reader(csvFile)  # Read CSV

    for row in readCsv:

        # Get Values and manupilate in the file.write
        filename = row[5][:-5]
        print(filename)
        os.chdir(r'E:\Dataset\images')  # the directory containing your .jpegs
        for file in glob.glob("*.jpg"):  # iterates over all files in the directory ending in .jpg
            if (filename == file[:-4]):
                # Reading image and getting its real width and height
                image_ppm = cv2.imread(file)
                #                 newPath = shutil.copy(file, 'E:\Sub set\Test')
                # Slicing from tuple only first two elements
                h, w = image_ppm.shape[:2]
                print(h, w)

                xmin = row[0]
                ymin = row[1]
                ymax = row[2]
                xmax = row[3]
                label = row[4]

                xcenter = (float(xmin) + float(xmax)) / 2
                ycenter = (float(ymin) + float(ymax)) / 2

                width = float(xmax) - float(xmin)
                height = float(ymax) - float(ymin)

                Xcenter = xcenter / w
                Ycenter = ycenter / h
                Width = width / w
                Height = height / h
                # Write CSV you need format it to string if the value is an int
                os.chdir(r'E:\Sub set\YOLO Annotations')
                f = open(filename + '.txt', 'a')
                #                 f.write(label+" "+str(Xcenter)+" "+str(Ycenter)+" "+str(Width)+" "+str(Height))
                file_path = filename + '.txt'
                if os.stat(file_path).st_size == 0:
                    f = open(filename + '.txt', 'a')
                    f.write(label + " " + str(Xcenter) + " " + str(Ycenter) + " " + str(Width) + " " + str(Height))
                    f.close()
                else:
                    print('File is not empty')
                    f = open(filename + '.txt', 'a')
                    f.write(
                        "\n" + label + " " + str(Xcenter) + " " + str(Ycenter) + " " + str(Width) + " " + str(Height))

                # You Must Close the FIle after writing it.
                f.close()
                os.chdir(r'E:\Dataset\images')

print("OK")