# -*- coding: utf-8 -*-

from matplotlib.gridspec import GridSpec
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys



class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100, Ttype=1):
        # 创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        
        # 在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)
        self.InitSub(Ttype)

    def InitSub(self, Ttype):
        self.fig.clear()
        # Type表示绘图的类型，我需要画两幅图，两幅图下面的子图位置和子图显示的方式不同
        if Ttype == 1:
            gs = GridSpec(2, 3)
            self.ax1 = self.fig.add_subplot(gs[:, :2])
            self.ax2 = self.fig.add_subplot(gs[0, 2], polar=True)
            self.ax3 = self.fig.add_subplot(gs[1, 2])
        elif Ttype == 2:
            gs = GridSpec(2, 4)
            self.ax1 = self.fig.add_subplot(gs[0, 0])
            self.ax2 = self.fig.add_subplot(gs[0, 1])
            self.ax3 = self.fig.add_subplot(gs[0, 2])
            self.ax4 = self.fig.add_subplot(gs[0, 3])
            self.ax5 = self.fig.add_subplot(gs[1, 0])
            self.ax6 = self.fig.add_subplot(gs[1, 1])
            self.ax7 = self.fig.add_subplot(gs[1, 2])
            self.ax8 = self.fig.add_subplot(gs[1, 3])

    def get_ax(self, Num):
        if Num == 0:
            return self.ax1
        elif Num == 1:
            return self.ax2
        elif Num == 2:
            return self.ax3
        elif Num == 3:
            return self.ax4
        elif Num == 4:
            return self.ax5
        elif Num == 5:
            return self.ax6
        elif Num == 6:
            return self.ax7
        elif Num == 7:
            return self.ax8

    def plot_pie(self):
        matplotlib.rcParams['font.family'] = 'SimHei'
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        citys = ["北京市", "上海市", "广州市", "深圳市", "南京市", "成都市", "杭州市", "武汉市"]
        types = ['设计师', '工程师', '运维', '产品经理', '运营']
        typeLength = len(types)
        # 产生绘图数据
        data = np.random.randint(500, 2000, size=len(types) * len(citys)).reshape(len(citys), len(types))
        for i in range(len(citys)):
            ax = self.get_ax(i)
            ax.pie(data[i], autopct='%3.1f%%', labels=types)
            ax.set_title(citys[i])

# 此处代码使用qt designer设计产生的
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class MyDialog(QMainWindow, Ui_Form):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.currentPage = 0
        self.setupUi(self)
        self.setCentralWidget(self.widget)
        self.canvas = MyFigure(Ttype=2)
        self.canvas.plot_pie()
        self.canvas.get_ax(0).cla()
        self.gridlayout = QGridLayout(self.widget)
        self.gridlayout.addWidget(self.canvas, 0, 0)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MyDialog()
    main.show()
    sys.exit(app.exec_())