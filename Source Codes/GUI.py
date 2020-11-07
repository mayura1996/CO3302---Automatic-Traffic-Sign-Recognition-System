# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup

lang = ''
list1 = []
list1.append('')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 751)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image:url(\"roundaboutImg/background.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 170, 91, 81))
        self.groupBox.setStyleSheet("background-image:url(\"roundaboutImg/roundabout.png\");\n"
"background-size:cover;\n"
"background-repeat: no-repeat;\n"
"border:none;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 170, 131, 81))
        self.groupBox_2.setStyleSheet("background-image:url(\"roundaboutImg/50-sign.png\");\n"
"background-size:center;\n"
"background-repeat:no-repeat;\n"
"margin-left:50%;\n"
"border:none;\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(660, 180, 61, 61))
        self.groupBox_3.setStyleSheet("background-image:url(\"roundaboutImg/70-sign.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(660, 310, 81, 81))
        self.groupBox_4.setStyleSheet("background-image:url(\"roundaboutImg/rail.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(170, 310, 81, 80))
        self.groupBox_6.setStyleSheet("background-image:url(\"roundaboutImg/stop.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(400, 310, 81, 80))
        self.groupBox_7.setStyleSheet("background-image:url(\"roundaboutImg/pedestrian.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(400, 450, 81, 80))
        self.groupBox_9.setStyleSheet("background-image:url(\"roundaboutImg/bend left.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(170, 450, 81, 81))
        self.groupBox_10.setStyleSheet("background-image:url(\"roundaboutImg/bend right.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.groupBox_12 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_12.setGeometry(QtCore.QRect(290, 590, 81, 80))
        self.groupBox_12.setStyleSheet("background-image:url(\"roundaboutImg/u turn.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_14 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_14.setGeometry(QtCore.QRect(550, 590, 91, 80))
        self.groupBox_14.setStyleSheet("background-image:url(\"roundaboutImg/yield.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_15 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_15.setGeometry(QtCore.QRect(660, 450, 81, 80))
        self.groupBox_15.setStyleSheet("background-image:url(\"roundaboutImg/school zone.png\");\n"
"background-size:cover;\n"
"background-repeat:no-repeat;\n"
"border:none;")
        self.groupBox_15.setTitle("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 670, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:white")
        self.pushButton.setObjectName("pushButton")
        self.English = QtWidgets.QRadioButton(self.centralwidget)
        self.English.setGeometry(QtCore.QRect(240, 80, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.English.setFont(font)
        self.English.setStyleSheet("color:white")
        self.English.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.English.setObjectName("English")
        self.Sinhala = QtWidgets.QRadioButton(self.centralwidget)
        self.Sinhala.setGeometry(QtCore.QRect(370, 80, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sinhala.setFont(font)
        self.Sinhala.setStyleSheet("color:white")
        self.Sinhala.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.Sinhala.setObjectName("Sinhala")
        self.Tamil = QtWidgets.QRadioButton(self.centralwidget)
        self.Tamil.setGeometry(QtCore.QRect(500, 80, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Tamil.setFont(font)
        self.Tamil.setStyleSheet("color:white")
        self.Tamil.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.Tamil.setObjectName("Tamil")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")

        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.roundAbout = QtWidgets.QRadioButton(self.centralwidget)
        self.roundAbout.setGeometry(QtCore.QRect(150, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.roundAbout.setFont(font)
        self.roundAbout.setStyleSheet("color:white")
        self.roundAbout.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.roundAbout.setObjectName("roundAbout")
        self.MaxSpeedLimit50 = QtWidgets.QRadioButton(self.centralwidget)
        self.MaxSpeedLimit50.setGeometry(QtCore.QRect(370, 140, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.MaxSpeedLimit50.setFont(font)
        self.MaxSpeedLimit50.setStyleSheet("color:white")
        self.MaxSpeedLimit50.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.MaxSpeedLimit50.setObjectName("MaxSpeedLimit50")
        self.MaxSpeedLimit70 = QtWidgets.QRadioButton(self.centralwidget)
        self.MaxSpeedLimit70.setGeometry(QtCore.QRect(600, 140, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.MaxSpeedLimit70.setFont(font)
        self.MaxSpeedLimit70.setStyleSheet("color:white")
        self.MaxSpeedLimit70.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.MaxSpeedLimit70.setObjectName("MaxSpeedLimit70")
        self.Stop = QtWidgets.QRadioButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(160, 280, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Stop.setFont(font)
        self.Stop.setStyleSheet("color:white")
        self.Stop.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.Stop.setObjectName("Stop")
        self.PedestrainCrossing = QtWidgets.QRadioButton(self.centralwidget)
        self.PedestrainCrossing.setGeometry(QtCore.QRect(360, 280, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.PedestrainCrossing.setFont(font)
        self.PedestrainCrossing.setStyleSheet("color:white")
        self.PedestrainCrossing.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.PedestrainCrossing.setObjectName("PedestrainCrossing")
        self.RailwayCrossing = QtWidgets.QRadioButton(self.centralwidget)
        self.RailwayCrossing.setGeometry(QtCore.QRect(620, 280, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.RailwayCrossing.setFont(font)
        self.RailwayCrossing.setStyleSheet("color:white")
        self.RailwayCrossing.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.RailwayCrossing.setObjectName("RailwayCrossing")
        self.BendRight = QtWidgets.QRadioButton(self.centralwidget)
        self.BendRight.setGeometry(QtCore.QRect(160, 420, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.BendRight.setFont(font)
        self.BendRight.setStyleSheet("color:white")
        self.BendRight.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.BendRight.setObjectName("BendRight")
        self.BendLeft = QtWidgets.QRadioButton(self.centralwidget)
        self.BendLeft.setGeometry(QtCore.QRect(390, 420, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.BendLeft.setFont(font)
        self.BendLeft.setStyleSheet("color:white")
        self.BendLeft.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.BendLeft.setObjectName("BendLeft")
        self.SchoolZone = QtWidgets.QRadioButton(self.centralwidget)
        self.SchoolZone.setGeometry(QtCore.QRect(640, 420, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.SchoolZone.setFont(font)
        self.SchoolZone.setStyleSheet("color:white")
        self.SchoolZone.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.SchoolZone.setObjectName("SchoolZone")
        self.NoUTurn = QtWidgets.QRadioButton(self.centralwidget)
        self.NoUTurn.setGeometry(QtCore.QRect(280, 560, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.NoUTurn.setFont(font)
        self.NoUTurn.setStyleSheet("color:white")
        self.NoUTurn.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.NoUTurn.setObjectName("NoUTurn")
        self.GiveWay = QtWidgets.QRadioButton(self.centralwidget)
        self.GiveWay.setGeometry(QtCore.QRect(540, 560, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.GiveWay.setFont(font)
        self.GiveWay.setStyleSheet("color:white")
        self.GiveWay.setStyleSheet("QRadioButton::checked:pressed"
                                        "{"
                                        "background-color : red"
                                        "}")
        self.GiveWay.setObjectName("GiveWay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setToolTipDuration(3)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btngroup1 = QButtonGroup()
        self.btngroup2 = QButtonGroup()
        self.btngroup3 = QButtonGroup()
        self.btngroup4 = QButtonGroup()
        self.btngroup5 = QButtonGroup()
        self.btngroup6 = QButtonGroup()
        self.btngroup7 = QButtonGroup()
        self.btngroup8 = QButtonGroup()
        self.btngroup9 = QButtonGroup()
        self.btngroup10 = QButtonGroup()
        self.btngroup11 = QButtonGroup()
        self.btngroup12 = QButtonGroup()

        self.btngroup1.addButton(self.English)
        self.btngroup1.addButton(self.Sinhala)
        self.btngroup1.addButton(self.Tamil)
        self.btngroup2.addButton(self.roundAbout)
        self.btngroup3.addButton(self.MaxSpeedLimit50)
        self.btngroup4.addButton(self.MaxSpeedLimit70)
        self.btngroup5.addButton(self.Stop)
        self.btngroup6.addButton(self.PedestrainCrossing)
        self.btngroup7.addButton(self.RailwayCrossing)
        self.btngroup8.addButton(self.BendRight)
        self.btngroup9.addButton(self.BendLeft)
        self.btngroup10.addButton(self.SchoolZone)
        self.btngroup11.addButton(self.NoUTurn)
        self.btngroup12.addButton(self.GiveWay)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Traffic Sign Detection"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.English.setText(_translate("MainWindow", "English"))
        self.Sinhala.setText(_translate("MainWindow", "SInhala"))
        self.Tamil.setText(_translate("MainWindow", "Tamil"))
        self.label.setText(_translate("MainWindow", "Automatic Traffic Sign Detection System"))
        self.label_2.setText(_translate("MainWindow", "Select Langugae    :"))
        self.roundAbout.setText(_translate("MainWindow", "Roundabout"))
        self.MaxSpeedLimit50.setText(_translate("MainWindow", "Maximum Speed 50"))
        self.MaxSpeedLimit70.setText(_translate("MainWindow", "Maximum Speed Limit 70"))
        self.Stop.setText(_translate("MainWindow", "Stop Sign"))
        self.PedestrainCrossing.setText(_translate("MainWindow", "Pedestrian Crossing"))
        self.RailwayCrossing.setText(_translate("MainWindow", "Railway Crossing"))
        self.BendRight.setText(_translate("MainWindow", "Bend Right"))
        self.BendLeft.setText(_translate("MainWindow", "Bend Left"))
        self.SchoolZone.setText(_translate("MainWindow", "School Zone"))
        self.NoUTurn.setText(_translate("MainWindow", "No U Turn"))
        self.GiveWay.setText(_translate("MainWindow", "Give Way"))

        self.roundAbout.clicked.connect(self.roundabout)
        self.MaxSpeedLimit50.clicked.connect(self.speed50)
        self.MaxSpeedLimit70.clicked.connect(self.speed70)
        self.RailwayCrossing.clicked.connect(self.railway)
        # self.MaxSpeed100.clicked.connect(self.speed100)
        self.Stop.clicked.connect(self.stop)
        self.PedestrainCrossing.clicked.connect(self.pedestrian)
        # self.EndOfSpeed.clicked.connect(self.endOfSpeed)
        # self.radioButton_9.clicked.connect(self.radioButton)
        self.BendRight.clicked.connect(self.bendRight)
        self.BendLeft.clicked.connect(self.bendLeft)
        self.NoUTurn.clicked.connect(self.uTurn)
        self.GiveWay.clicked.connect(self.giveWay)
        self.SchoolZone.clicked.connect(self.schoolZone)
        # self.OtherSign.clicked.connect(self.otherSign)
        self.pushButton.clicked.connect(self.button_pressed)
        self.English.clicked.connect(self.english)
        self.Sinhala.clicked.connect(self.sinhala)
        self.Tamil.clicked.connect(self.tamil)

    def english(self):
        global lang
        if self.English.isChecked():
                lang=''
                print("English")



    def sinhala(self):
        global lang
        if self.Sinhala.isChecked():
                lang='SI'
                print("Sinhala")
                print(lang)

    def tamil(self):
        global lang
        if self.Tamil.isChecked():
                print("Tamil")
                lang='TA'
                print(lang)

    def roundabout(self):
        global list1
        if self.roundAbout.isChecked():
                print("sdsdsd")
                list1.append('0')

    def speed50(self):
        global list1
        if self.MaxSpeedLimit50.isChecked():
                print("kkk")
                list1.append('1')

    def speed70(self):
        global list1
        if self.MaxSpeedLimit70.isChecked():
                print("mmmm")
                list1.append('2')
    def railway(self):
        global list1
        if self.RailwayCrossing.isChecked():
                print("yytyyt")
                list1.append('3')


    def stop(self):
        global list1
        if self.Stop.isChecked():
                print("lllll")
                list1.append('5')

    def pedestrian(self):
         global list1
         if self.PedestrainCrossing.isChecked():
                print("uuuuuu")
                list1.append('6')

    def bendLeft(self):
        global list1
        if self.BendLeft.isChecked():
                print("ttttt")
                list1.append('7')

    def bendRight(self):
         global list1
         if self.BendRight.isChecked():
                print("44444")
                list1.append('8')


    def uTurn(self):
        global list1
        if self.NoUTurn.isChecked():
                print("000000")
                list1.append('9')

    def giveWay(self):
        global list1
        if self.GiveWay.isChecked():
                print("444444")
                list1.append('10')
    def schoolZone(self):
        global list1
        if self.SchoolZone.isChecked():
                 print("22222")
                 list1.append('4')
    # def otherSign(self):
    #      global x
    #      if self.OtherSign.isChecked():
    #             print("343434")
    #             x=x+6


    import os
    def button_pressed(self):
        global lang
        global list1
        print("pressed")
        # i=0
        # while (i <= 10):
        #         print(x)
        signList = {"0": 0, "1": 0, "2": 0,
                    "3": 0, "4": 0,
                    "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
                    "10": 0, "11": 0, "12": 0, "13": 0,
                    "14": 0, "15": 0}

        # with u turn replaced bump

        i = 1
        file1 = open("/home/manawadu/PycharmProjects/CO_PROJECT/Darknet - 3 (28 08 2020)/darknet/example.txt", "w")
        file_path = "/home/manawadu/PycharmProjects/CO_PROJECT/Darknet - 3 (28 08 2020)/darknet/example.txt"
        checkString = ''
        while i < 10:
            # print(list1)
            file1 = open("/home/manawadu/PycharmProjects/CO_PROJECT/Darknet - 3 (28 08 2020)/darknet/example.txt", "r+")
            if os.stat(file_path).st_size != 0:
                x = file1.readline()
                print(x)
                # y=int(x[0])
                # print(y)
                if x in list1:
                    print("yes")
                    if (x != checkString):
                        os.system('mpg123 /home/manawadu/PycharmProjects/NEW-GUI ' + x + lang+'.mp3')
                checkString = x
            else:
                print("empty")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

