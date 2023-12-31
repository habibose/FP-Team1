# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Projectfiexsed1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from paho.mqtt.client import Client

import socket
from PyQt5.QtCore import QTimer, Qt, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
##import cv2
import numpy as np
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout
import sys
from PyQt5.QtWidgets import QVBoxLayout
import cv2

# camera ip
camera_ip = 'http://192.168.137.15:8080/video'
from pyzbar.pyzbar import decode

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
argument = 'T'

class Ui_GripperRobotController(object):
    def setupUi(self, GripperRobotController):
        GripperRobotController.setObjectName("GripperRobotController")
        GripperRobotController.resize(1444, 872)
        font = QtGui.QFont()
        font.setFamily("Arial")
        GripperRobotController.setFont(font)
        GripperRobotController.setAcceptDrops(False)
        GripperRobotController.setStyleSheet("selection-background-color: rgb(85, 255, 0);")
        GripperRobotController.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(GripperRobotController)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1431, 851))
        self.widget.setStyleSheet("background-color: rgb(164, 170, 255);")
        self.widget.setObjectName("widget")
        self.Control = QtWidgets.QFrame(self.widget)
        self.Control.setGeometry(QtCore.QRect(10, 510, 701, 331))
        self.Control.setStyleSheet("background-color: rgb(255, 160, 160);")
        self.Control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Control.setObjectName("Control")
        self.Left = QtWidgets.QPushButton(self.Control)
        self.Left.setGeometry(QtCore.QRect(10, 210, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Left.setFont(font)
        self.Left.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Left.setObjectName("Left")
        self.Right = QtWidgets.QPushButton(self.Control)
        self.Right.setEnabled(True)
        self.Right.setGeometry(QtCore.QRect(170, 210, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Right.setFont(font)
        self.Right.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Right.setObjectName("Right")
        self.Forward = QtWidgets.QPushButton(self.Control)
        self.Forward.setGeometry(QtCore.QRect(90, 130, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Forward.setFont(font)
        self.Forward.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Forward.setObjectName("Forward")
        self.Backward = QtWidgets.QPushButton(self.Control)
        self.Backward.setGeometry(QtCore.QRect(90, 210, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Backward.setFont(font)
        self.Backward.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Backward.setObjectName("Backward")
        self.GripperExpand = QtWidgets.QPushButton(self.Control)
        self.GripperExpand.setGeometry(QtCore.QRect(490, 40, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.GripperExpand.setFont(font)
        self.GripperExpand.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.GripperExpand.setObjectName("GripperExpand")
        self.Gripperwrap = QtWidgets.QPushButton(self.Control)
        self.Gripperwrap.setGeometry(QtCore.QRect(490, 160, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.Gripperwrap.setFont(font)
        self.Gripperwrap.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Gripperwrap.setObjectName("Gripperwrap")
        self.frame = QtWidgets.QFrame(self.Control)
        self.frame.setGeometry(QtCore.QRect(0, 0, 141, 51))
        self.frame.setStyleSheet("background-color: rgb(6, 10, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Forward_2 = QtWidgets.QPushButton(self.Control)
        self.Forward_2.setGeometry(QtCore.QRect(340, 170, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Forward_2.setFont(font)
        self.Forward_2.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Forward_2.setObjectName("Forward_2")
        self.Right_2 = QtWidgets.QPushButton(self.Control)
        self.Right_2.setEnabled(True)
        self.Right_2.setGeometry(QtCore.QRect(400, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Right_2.setFont(font)
        self.Right_2.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Right_2.setObjectName("Right_2")
        self.Backward_2 = QtWidgets.QPushButton(self.Control)
        self.Backward_2.setGeometry(QtCore.QRect(340, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Backward_2.setFont(font)
        self.Backward_2.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Backward_2.setObjectName("Backward_2")
        self.Left_2 = QtWidgets.QPushButton(self.Control)
        self.Left_2.setGeometry(QtCore.QRect(280, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Left_2.setFont(font)
        self.Left_2.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Left_2.setObjectName("Left_2")
        self.label_15 = QtWidgets.QLabel(self.Control)
        self.label_15.setGeometry(QtCore.QRect(30, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Control)
        self.label_16.setGeometry(QtCore.QRect(280, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Control)
        self.label_17.setGeometry(QtCore.QRect(490, 0, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Control)
        self.label_18.setGeometry(QtCore.QRect(490, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_18.setObjectName("label_18")
        self.Stop = QtWidgets.QPushButton(self.Control)
        self.Stop.setGeometry(QtCore.QRect(500, 280, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.Stop.setFont(font)
        self.Stop.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Stop.setObjectName("Stop")
        self.label_19 = QtWidgets.QLabel(self.Control)
        self.label_19.setGeometry(QtCore.QRect(500, 250, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setObjectName("label_19")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 701, 481))
        self.widget_2.setStyleSheet("background-color: rgb(252, 255, 76);")
        self.widget_2.setObjectName("widget_2")
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 121, 51))
        self.frame_2.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Camera = QtWidgets.QLabel(self.widget_2)
        self.Camera.setGeometry(QtCore.QRect(20, 70, 661, 381))
        self.Camera.setText("")
        self.Camera.setObjectName("Camera")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(720, 10, 701, 481))
        self.widget_3.setStyleSheet("\n"
"background-color: rgb(255, 0, 127);")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 121, 51))
        self.widget_4.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.GraphWidget = QtWidgets.QWidget(self.widget_3)
        self.GraphWidget.setGeometry(QtCore.QRect(20, 70, 661, 381))
        self.GraphWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GraphWidget.setObjectName("GraphWidget")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(720, 510, 701, 331))
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 161, 51))
        self.widget_6.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.widget_6.setObjectName("widget_6")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(17, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setGeometry(QtCore.QRect(17, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setGeometry(QtCore.QRect(17, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setGeometry(QtCore.QRect(17, 190, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setGeometry(QtCore.QRect(17, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_5)
        self.label_10.setGeometry(QtCore.QRect(17, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.BoxesScanned = QtWidgets.QLabel(self.widget_5)
        self.BoxesScanned.setGeometry(QtCore.QRect(177, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.BoxesScanned.setFont(font)
        self.BoxesScanned.setText("")
        self.BoxesScanned.setObjectName("BoxesScanned")
        self.MovedBoxes = QtWidgets.QLabel(self.widget_5)
        self.MovedBoxes.setGeometry(QtCore.QRect(177, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.MovedBoxes.setFont(font)
        self.MovedBoxes.setText("")
        self.MovedBoxes.setObjectName("MovedBoxes")
        self.GripperStatue = QtWidgets.QLabel(self.widget_5)
        self.GripperStatue.setGeometry(QtCore.QRect(177, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.GripperStatue.setFont(font)
        self.GripperStatue.setText("")
        self.GripperStatue.setObjectName("GripperStatue")
        self.Speed = QtWidgets.QLabel(self.widget_5)
        self.Speed.setGeometry(QtCore.QRect(177, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.Speed.setFont(font)
        self.Speed.setText("")
        self.Speed.setObjectName("Speed")
        self.XAxisPosition = QtWidgets.QLabel(self.widget_5)
        self.XAxisPosition.setGeometry(QtCore.QRect(177, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.XAxisPosition.setFont(font)
        self.XAxisPosition.setText("")
        self.XAxisPosition.setObjectName("XAxisPosition")
        self.YAxisPosition = QtWidgets.QLabel(self.widget_5)
        self.YAxisPosition.setGeometry(QtCore.QRect(177, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.YAxisPosition.setFont(font)
        self.YAxisPosition.setText("")
        self.YAxisPosition.setObjectName("YAxisPosition")
        self.line = QtWidgets.QFrame(self.widget_5)
        self.line.setGeometry(QtCore.QRect(7, 100, 251, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget_5)
        self.line_2.setGeometry(QtCore.QRect(149, 80, 20, 221))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.widget_5)
        self.line_3.setGeometry(QtCore.QRect(7, 140, 251, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.widget_5)
        self.line_4.setGeometry(QtCore.QRect(7, 180, 251, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget_5)
        self.line_5.setGeometry(QtCore.QRect(7, 220, 251, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.widget_5)
        self.line_6.setGeometry(QtCore.QRect(7, 260, 251, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.widget_5)
        self.line_7.setGeometry(QtCore.QRect(7, 300, 271, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.widget_5)
        self.line_8.setGeometry(QtCore.QRect(530, 80, 20, 151))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.widget_5)
        self.line_9.setGeometry(QtCore.QRect(320, 190, 331, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.widget_5)
        self.line_10.setGeometry(QtCore.QRect(320, 230, 331, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.widget_5)
        self.line_11.setGeometry(QtCore.QRect(320, 150, 331, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.widget_5)
        self.line_12.setGeometry(QtCore.QRect(320, 110, 321, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.widget_5)
        self.line_13.setGeometry(QtCore.QRect(270, 80, 20, 221))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.label_14 = QtWidgets.QLabel(self.widget_5)
        self.label_14.setGeometry(QtCore.QRect(330, 200, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.widget_5)
        self.label_11.setGeometry(QtCore.QRect(330, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setGeometry(QtCore.QRect(330, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_5)
        self.label_13.setGeometry(QtCore.QRect(330, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.YDisitination = QtWidgets.QLabel(self.widget_5)
        self.YDisitination.setGeometry(QtCore.QRect(550, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.YDisitination.setFont(font)
        self.YDisitination.setText("")
        self.YDisitination.setObjectName("YDisitination")
        self.BoxYPosition = QtWidgets.QLabel(self.widget_5)
        self.BoxYPosition.setGeometry(QtCore.QRect(550, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.BoxYPosition.setFont(font)
        self.BoxYPosition.setText("")
        self.BoxYPosition.setObjectName("BoxYPosition")
        self.BoxXPosition = QtWidgets.QLabel(self.widget_5)
        self.BoxXPosition.setGeometry(QtCore.QRect(550, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.BoxXPosition.setFont(font)
        self.BoxXPosition.setText("")
        self.BoxXPosition.setObjectName("BoxXPosition")
        self.XDistination = QtWidgets.QLabel(self.widget_5)
        self.XDistination.setGeometry(QtCore.QRect(550, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.XDistination.setFont(font)
        self.XDistination.setText("")
        self.XDistination.setObjectName("XDistination")
        self.line_14 = QtWidgets.QFrame(self.widget_5)
        self.line_14.setGeometry(QtCore.QRect(640, 80, 20, 151))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.widget_5)
        self.line_15.setGeometry(QtCore.QRect(310, 80, 20, 151))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.widget_6.raise_()
        self.label_6.raise_()
        self.MovedBoxes.raise_()
        self.XAxisPosition.raise_()
        self.YAxisPosition.raise_()
        self.line.raise_()
        self.label_5.raise_()
        self.BoxesScanned.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_2.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.Speed.raise_()
        self.label_7.raise_()
        self.GripperStatue.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_13.raise_()
        self.label_14.raise_()
        self.label_11.raise_()
        self.line_14.raise_()
        self.line_15.raise_()
        self.label_13.raise_()
        self.line_12.raise_()
        self.line_8.raise_()
        self.label_12.raise_()
        self.BoxYPosition.raise_()
        self.BoxXPosition.raise_()
        self.XDistination.raise_()
        self.YDisitination.raise_()

        self.retranslateUi(GripperRobotController)
        QtCore.QMetaObject.connectSlotsByName(GripperRobotController)
        self.Forward.setShortcut('w')
        self.Forward.pressed.connect(self.forward)
        self.Backward.setShortcut('s')
        self.Backward.pressed.connect(self.backward)
        self.Right.setShortcut('d')
        self.Right.pressed.connect(self.right)
        self.Left.setShortcut('a')
        self.Left.pressed.connect(self.left)
        self.GripperExpand.setShortcut('E')
        self.GripperExpand.pressed.connect(self.gripper_expand)
        self.Gripperwrap.setShortcut('Q')
        self.Gripperwrap.pressed.connect(self.gripper_wrap)
        self.Forward_2.setShortcut('Ctrl+W')
        self.Forward_2.pressed.connect(self.sforward)
        self.Backward_2.setShortcut('Ctrl+S')
        self.Backward_2.pressed.connect(self.sbackward)
        self.Right_2.setShortcut('Ctrl+D')
        self.Right_2.pressed.connect(self.sright)
        self.Left_2.setShortcut('Ctrl+A')
        self.Left_2.pressed.connect(self.sleft)
        self.Stop.setShortcut('F')
        self.Stop.pressed.connect(self.Stop1)
        graph = QVBoxLayout(self.GraphWidget)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        graph.addWidget(self.canvas)
        
        #camera feed
        self.cap = cv2.VideoCapture(camera_ip)

        # Create a timer to update the camera feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(0)  # Update every 20 milliseconds (50 frames per second)
        self.info = None
        
    
    ## Frame Update
    def update_frame(self):
        ret, frame = self.cap.read()
        self.frame = frame
        if ret:
            # Convert the OpenCV frame to a QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(q_image)

            # display camera on lapel called "self.camera"
            self.Camera.setPixmap(pixmap)
            decoded_objects = decode(frame)
            self.read_qr()
            
    # separate x and y in two variables
    def read_qr(self):
        qcd = cv2.QRCodeDetector()
        retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(self.frame)
        if retval:
            if self.info != decoded_info:
                print(decoded_info)
                self.decoded = decoded_info
                #self.camera_output()
                return decoded_info
            else:
                return self.info 
                
        
    def camera_output(self):
        decoded = self.decoded
        assignments = decoded.split(',')
        for assignment in assignments:
            var_name, var_value = assignment.split('=')
            if var_name == 'x':
                self.xdistination = int(var_value)
            elif var_name == 'y':
                self.ydistination = int(var_value)




    # wifi with esp
    def send_data(self):
        esp32_ip = '192.168.137.19'  # Replace with the ESP32's IP address
        esp32_port = 80  # Replace with the port your ESP32 is listening on
        data = self.argument

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((esp32_ip, esp32_port))
            sock.send(data.encode('utf-8'))
            self.xcoordinate = sock.recv(1024).decode('utf-8')
            self.ycoordinate = sock.recv(1024).decode('utf-8')
            print(self.xcoordinate)
            print(self.ycoordinate)
##Graph funtion
    def plot_data(self):
        XCoordinate = self.xcoordinate
        YCoordinate = self.ycoordinate
        XDistination = self.ydistination
        YDistination = self.ydistination
        x = [XCoordinate, XDistination]
        y = [YCoordinate, YDistination]
        plt.plot(x, y)
        plt.title("Room Coordinates")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        self.canvas.draw()
##Control functions
    def forward(self):
        self.argument = 'F '
        self.Speed.setText("Fast")
        ##soc.send(self.argument.encode())
        self.send_data()
        self.plot_data()
    def backward(self):
        self.argument = 'B '
        self.Speed.setText("Fast")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
        ##ser.write([argument])
    def right(self):
        self.argument = 'R '
        self.Speed.setText("Fast")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
        ##ser.write([argument])          
    def left(self):
        self.argument = 'L '
        self.Speed.setText("Fast")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
        ##ser.write([argument])
    def gripper_expand(self):
        self.argument = 'GE '
        self.GripperStatue.setText("Expanded")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
        ##ser.write([argument])
    def gripper_wrap(self):
        self.argument = 'GW '
        self.GripperStatue.setText("Wrapped")
        self.send_data()
        ##soc.send(self.argument.encode())
        ##ser.write([argument])
    def sforward(self):
        self.argument = 'SF '
        ##ser.write([argument])
        self.Speed.setText("Slow")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
    def sbackward(self):
        self.argument = 'SB '
        ##ser.write([argument])
        self.Speed.setText("Slow")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
    def sright(self):
        self.argument = 'SR '
        ##ser.write([argument])
        self.Speed.setText("Slow")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
    def sleft(self):
        self.argument = 'SL '
        ##ser.write([argument])
        self.Speed.setText("Slow")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())
    def Stop1(self):
        self.argument = 'S '
        ##ser.write([argument])
        self.Speed.setText("Stopped")
        self.send_data()
        self.plot_data()
        ##soc.send(self.argument.encode())

    def retranslateUi(self, GripperRobotController):
        _translate = QtCore.QCoreApplication.translate
        GripperRobotController.setWindowTitle(_translate("GripperRobotController", "Gripper Robot Controller"))
        self.Left.setText(_translate("GripperRobotController", "◄"))
        self.Right.setText(_translate("GripperRobotController", "►"))
        self.Forward.setText(_translate("GripperRobotController", "▲"))
        self.Backward.setText(_translate("GripperRobotController", "▼"))
        self.GripperExpand.setText(_translate("GripperRobotController", "◄▬►"))
        self.Gripperwrap.setText(_translate("GripperRobotController", "►▬◄"))
        self.label.setText(_translate("GripperRobotController", "Controller"))
        self.Forward_2.setText(_translate("GripperRobotController", "▲"))
        self.Right_2.setText(_translate("GripperRobotController", "►"))
        self.Backward_2.setText(_translate("GripperRobotController", "▼"))
        self.Left_2.setText(_translate("GripperRobotController", "◄"))
        self.label_15.setText(_translate("GripperRobotController", "Fast (W,A,S,D)"))
        self.label_16.setText(_translate("GripperRobotController", "Slow(shift+W,A,S,D)"))
        self.label_17.setText(_translate("GripperRobotController", "Gripper Expand (E)"))
        self.label_18.setText(_translate("GripperRobotController", "Gripper Wrap (Q)"))
        self.Stop.setText(_translate("GripperRobotController", "Stop"))
        self.label_19.setText(_translate("GripperRobotController", "Stop (F)"))
        self.label_2.setText(_translate("GripperRobotController", "Camera"))
        self.label_3.setText(_translate("GripperRobotController", "Graph"))
        self.label_4.setText(_translate("GripperRobotController", "Informations"))
        self.label_5.setText(_translate("GripperRobotController", "Boxes Scanned"))
        self.label_6.setText(_translate("GripperRobotController", "Moved Boxes"))
        self.label_7.setText(_translate("GripperRobotController", "Gripper Statue"))
        self.label_8.setText(_translate("GripperRobotController", "Speed"))
        self.label_9.setText(_translate("GripperRobotController", "Y-Coordinate"))
        self.label_10.setText(_translate("GripperRobotController", "X-Coordinate"))
        self.label_14.setText(_translate("GripperRobotController", "Y-Coordinate Distination"))
        self.label_11.setText(_translate("GripperRobotController", "Box X-Coordinate"))
        self.label_12.setText(_translate("GripperRobotController", "Box Y-Coordinate"))
        self.label_13.setText(_translate("GripperRobotController", "X-Coordinate Distination"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GripperRobotController = QtWidgets.QDialog()
    ui = Ui_GripperRobotController()
    ui.setupUi(GripperRobotController)
    GripperRobotController.show()
    sys.exit(app.exec_())
