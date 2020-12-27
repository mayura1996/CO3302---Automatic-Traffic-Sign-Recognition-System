# CO3302 Automatic Traffic Sign Recognition System

Automatic Traffic Sign Recognition System Detects traffic signs realtime with a 65 FPS speed and with a mean average precision of 64.1%. The system is built on top of YOLOv4 network.

# Installation Guide

1.	Download or clone the setup files available here in my repository.
2.	Extract the files to the Linux Environment.
3.	Run GUI.py file
4.	Open the Linux terminal and locate the root folder (folder name : Darknet Framework) of the extracted location or Right Click on the extracted folder and click Open in Terminal.
-	At the Terminal type the following commands;
    -	Activate the Anaconda Environment where you have setup the mentioned libraries and modules above.
    -	
```sh
$ conda activate myenv
```

> Insert the following codes to run the Traffic Sign Detector;

> If you are using an IP camera on a mobile device;
        a)	Download for Android phone mjpeg-stream soft: IP Webcam
        b)	Connect the Android phone to computer through a WIFI router or USB
        c)	 Start IP Webcam on your phone
        d)	Run the following code in the terminal by replacing the address as shown in the app.

```sh
$ ./darknet detector demo cfg/ts_data.data cfg/Traffic_test_pipeline.cfg weights/TrafficSigns.weights http://192.168.0.80:8080/video?dummy=param.mjpg -i 0
```
>  If you are using a webcam to input the video feed ;

```sh
$ ./darknet detector demo cfg/ts_data.data cfg/Traffic_test_pipeline.cfg weights/TrafficSigns.weights -c 0
```
> To save the recorder video to an output file:

```sh
$ ./darknet detector demo cfg/ts_data.data cfg/Traffic_test_pipeline.cfg weights/TrafficSigns.weights inputVIdeoName.mp4 -out_filename result.avi
```

> If you are using a pre reordered video to test on the detector. (Copy the video in to the data folder)

```sh
$ ./darknet detector demo cfg/ts_data.data cfg/Traffic_test_pipeline.cfg weights/TrafficSigns.weights data/ inputVIdeoName.mp4
```

## Sytem Requirements
- RAM 				– 8 GB DDR4 or above
- GPU 				– 4GB - NVIDIA GeForce GTX 1050 or above (NVIDIA Pascal/Titan GPU)
- Operating System		– Ubuntu 18.04 or above
- CUDA Version 			– 10.0
- cuDNN Version 		– 7.6.4
- OpenCV version		–  3.2.0
- Python 3.7 or above
- GNU compiler
- Anaconda environment

>Please note that the versions given above are compatible with NVIDIA GeForce GTX 1050 GPU. You may need to change the CUDA, cuDNN and OpenCV versions depending on the model of your GPU. Please check the Setting Up the Development Environment Document. 

## Software and Library Requirements

- PyQT 5
- Google Text to Speech
- mpg123
- TensorFlow, Keras, NumPy, Pandas,

> Please check the “Setting Up the Development Environment” document to set up the prerequisites on your device. 

# License

MIT

 # © Mayura Manawadu | 17/ENG/072 | EN 86191
