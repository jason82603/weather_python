# -*- coding: utf-8 -*-

import sys
from UI_mainwindow import Ui_MainWindow
from fetch_weather_data import get_weather_72_statememt
from sql_load import sqloutput
from sql_create import recreate_tables
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF,QDate,QDateTime,QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import csv
import matplotlib as plt
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import datetime

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Controller(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.timer=QTimer()
        self.timer.timeout.connect(self.showtime)      
        self.pushButton.clicked.connect(self.clicked_button)
        self.pushButton.clicked.connect(self.startTimer)
        self.comboBox.activated[str].connect(self.combobox_is_selected)
        self.pic_label.setPixmap(QPixmap('./img/cloud.jpg'))

        self.show()
    
    def clicked_button(self):       
        if self.comboBox_2.currentText()!='選擇鄉鎮':
            local_name=self.comboBox.currentText()    
            religion_name=self.comboBox_2.currentText()    
            path = './csv/comparison_table.csv'
            with open(path,'r',encoding="utf_8") as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    if local_name  in row and religion_name in row :
                        religion_num=row[0]
                        datas=get_weather_72_statememt(religion_num)  #fetch_weather_data裡
                        recreate_tables()      #sql_create              
                        sqloutput(religion_num) #sql_load
                        self.temperature.setText('     '+datas.iloc[0,3])
                        self.body_tem.setText('    '+datas.iloc[0,4])
                        self.rain_per.setText('    '+datas.iloc[0,5])
                        self.wet_per.setText('    '+datas.iloc[0,6])
                        print(datas)
                        
                        self.time_label.setStyleSheet("background-color: rgb(255, 255, 255);")
            '''            
            self.F = Figure_Canvas(3.9, 2.7, 100)
            self.LineFigureLayout = QGridLayout(self.linedisplay)  # 继承容器groupBox
            self.LineFigureLayout.addWidget(self.F)
            '''
            self.PrepareLineCanvas()
            
                
        
    def combobox_is_selected(self) :
        count=0
        self.comboBox_2.clear()
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0,'選擇鄉鎮')
        if self.comboBox.currentText()!='選擇縣市':
            
            value=self.comboBox.currentText()  
            path = './csv/comparison_table.csv'
            with open(path,'r',encoding="utf_8") as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    if value in row:
                        #religion_num=row[0]
                        religion_name=row[2]
                        #print(religion_name)
                        count+=1
                        self.comboBox_2.addItem("")
                        self.comboBox_2.setItemText(count,religion_name)
    def showtime(self):
        time=QDateTime.currentDateTime()#獲取當前時間
        timedisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化一下時間
    
        self.time_label.setText(timedisplay)
        
        
    def startTimer(self):
        self.timer.start(1000)   
                         
    def PrepareLineCanvas(self):
        local_name=self.comboBox.currentText()    
        religion_name=self.comboBox_2.currentText()    
        path = './csv/comparison_table.csv'
        with open(path,'r',encoding="utf_8") as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:
                if local_name  in row and religion_name in row :
                    religion_num=row[0]
                    datas=get_weather_72_statememt(religion_num)         
                    datas.iloc[:,2]

        a=[]        
        for i in range(17):
            a.append(datas.iloc[i,3])
        
        b=[]
        for i in range(17):
            b.append((datas.iloc[i,1])[0]+(datas.iloc[i,1])[1])
        
        int_list_y = list(map(int,a))
        int_list_x = list(map(str,b))

        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.linedisplay)
        self.LineFigureLayout.addWidget(self.LineFigure)
    
        x_range=np.arange(len(int_list_x))    #產生[ 0,1,2,3,4,........,16 ]
        self.LineFigure.ax.bar(x_range, int_list_y, tick_label=int_list_x) 

        
        self.LineFigure.ax.set_title('72hr-weather', fontsize=18)
        self.LineFigure.ax.text(0.5, -0.12, 'time',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=12, color='red',
        transform=self.LineFigure.ax.transAxes)
        self.LineFigure.ax.set_ylabel("temperature(°C)",color='red',fontsize=12)
        #self.LineFigure.ax.show()
        
        self.LineFigureLayout.removeWidget(self.LineFigure)
        self.LineFigureLayout.deleteLater()
     
                       
class Figure_Canvas(FigureCanvas):
    def __init__(self,parent=None,width=4.8,height=3.2,dpi=100):
        self.fig=Figure(figsize=(width,height),dpi=dpi)        
        super(Figure_Canvas,self).__init__(self.fig)
        self.ax=self.fig.add_subplot(111)
        


           
if __name__=="__main__":
    app=QApplication(sys.argv)  
    window=Controller()
    sys.exit(app.exec_()) 