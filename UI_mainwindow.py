# -*- coding: utf-8 -*-

import csv
from PyQt5 import QtCore, QtGui, QtWidgets
'''
path = './csv/comparison_table.csv'
with open(path,'r',encoding="utf_8") as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
'''        
       
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setStyleSheet("color: blue;")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 40, 141, 31))
        self.comboBox.setObjectName("comboBox")
        for row in range(23):
            self.comboBox.addItem("")
            
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 40, 141, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        
        path = './csv/comparison_table.csv'
        value=self.comboBox.currentText()
        with open(path,'r',encoding="utf_8") as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:
                if value in row:
                    self.comboBox_2.addItem("")
                
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 32, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 110, 211, 121))
        self.frame.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.temperature = QtWidgets.QLabel(self.frame)
        self.temperature.setGeometry(QtCore.QRect(20, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.temperature.setFont(font)
        self.temperature.setObjectName("temperature")
        self.body_tem = QtWidgets.QLabel(self.frame)
        self.body_tem.setGeometry(QtCore.QRect(130, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.body_tem.setFont(font)
        self.body_tem.setObjectName("body_tem")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(290, 110, 211, 121))
        self.frame_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.wet_per = QtWidgets.QLabel(self.frame_2)
        self.wet_per.setGeometry(QtCore.QRect(20, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.wet_per.setFont(font)
        self.wet_per.setObjectName("wet_per")
        self.rain_per = QtWidgets.QLabel(self.frame_2)
        self.rain_per.setGeometry(QtCore.QRect(120, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.rain_per.setFont(font)
        self.rain_per.setObjectName("rain_per")
        
        self.linedisplay = QtWidgets.QGroupBox(self.centralwidget)
        self.linedisplay.setGeometry(QtCore.QRect(40, 280, 471, 321))
        self.linedisplay.setObjectName("LineDisplay")
        
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(60, 650, 220, 35))
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        
        self.pic_label = QtWidgets.QLabel(self.linedisplay)
        self.pic_label.setGeometry(QtCore.QRect(25, 20, 421, 280))
        self.pic_label.setObjectName("pic_label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "天氣即時系統"))
        self.comboBox.setItemText(0, _translate("MainWindow", "選擇縣市"))
        self.comboBox.setItemText(1, _translate("MainWindow", "基隆市"))
        self.comboBox.setItemText(2, _translate("MainWindow", "台北市"))
        self.comboBox.setItemText(3, _translate("MainWindow", "新北市"))
        self.comboBox.setItemText(4, _translate("MainWindow", "桃園市"))
        self.comboBox.setItemText(5, _translate("MainWindow", "新竹市"))
        self.comboBox.setItemText(6, _translate("MainWindow", "新竹縣"))
        self.comboBox.setItemText(7, _translate("MainWindow", "苗栗縣"))
        self.comboBox.setItemText(8, _translate("MainWindow", "台中市"))
        self.comboBox.setItemText(9, _translate("MainWindow", "彰化縣"))
        self.comboBox.setItemText(10, _translate("MainWindow", "南投縣"))
        self.comboBox.setItemText(11, _translate("MainWindow", "雲林縣"))
        self.comboBox.setItemText(12, _translate("MainWindow", "嘉義市"))
        self.comboBox.setItemText(13, _translate("MainWindow", "嘉義縣"))
        self.comboBox.setItemText(14, _translate("MainWindow", "台南市"))
        self.comboBox.setItemText(15, _translate("MainWindow", "高雄市"))
        self.comboBox.setItemText(16, _translate("MainWindow", "屏東縣"))
        self.comboBox.setItemText(17, _translate("MainWindow", "宜蘭縣"))
        self.comboBox.setItemText(18, _translate("MainWindow", "花蓮縣"))
        self.comboBox.setItemText(19, _translate("MainWindow", "臺東縣"))
        self.comboBox.setItemText(20, _translate("MainWindow", "澎湖縣"))
        self.comboBox.setItemText(21, _translate("MainWindow", "金門縣"))
        self.comboBox.setItemText(22, _translate("MainWindow", "連江縣"))
        
        self.comboBox_2.setItemText(0, _translate("MainWindow", "選擇鄉鎮"))
        
        self.pushButton.setText(_translate("MainWindow", "確定"))
        self.label_2.setText(_translate("MainWindow", "溫度"))
        self.label_3.setText(_translate("MainWindow", "體感溫度"))
        self.label_2.setStyleSheet("color: rgb(255, 115, 0)")
        self.label_3.setStyleSheet("color: rgb(255, 115, 0)")
        self.temperature.setText(_translate("MainWindow", ""))
        self.body_tem.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "濕度"))
        self.label_5.setText(_translate("MainWindow", "降雨機率"))
        self.label_4.setStyleSheet("color: rgb(255, 115, 0)")
        self.label_5.setStyleSheet("color: rgb(255, 115, 0)")
        self.wet_per.setText(_translate("MainWindow", ""))
        self.rain_per.setText(_translate("MainWindow", ""))
        self.linedisplay.setTitle(_translate("MainWindow", ""))
        self.pic_label.setText(_translate("MainWindow", "pic"))
