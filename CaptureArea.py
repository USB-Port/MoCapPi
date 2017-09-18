from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
import sys
import cv2
import numpy as np
import threading
import time
from multiprocessing import Queue
from CVHandler import *
from OpenGLHandler import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

running = False
capture_thread = None
q = Queue()
p = Queue()


class CaptureArea(QtGui.QWidget):

    def __init__(self, QWidget):
        super(CaptureArea, self).__init__()

        self.gridLayout_2 = QtGui.QGridLayout(QWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.captureArea = QtGui.QTabWidget(QWidget)
        self.captureArea.setObjectName(_fromUtf8("captureArea"))
        #self.captureArea.setTabsClosable(False)
        #self.captureArea.tabCloseRequested(lambda: self.closeTab(self.captureArea.currentIndex()))

        self.tabs = []
        self.gridLayouts = []
        self.widgets = []

        self.tabs.append(QtGui.QWidget())
        tabObjectName = "tab" + str(len(self.tabs) - 1)
        self.tabs[(len(self.tabs) - 1)].setObjectName(_fromUtf8(tabObjectName))

        self.gridLayouts.append(QtGui.QGridLayout(self.tabs[len(self.tabs) - 1]))
        gridLayoutObjectName = "gridLayout" + str(len(self.gridLayouts) - 1)
        self.gridLayouts[len(self.gridLayouts) - 1].setObjectName(_fromUtf8(gridLayoutObjectName))

        self.widgets.append(QtGui.QWidget(self.tabs[len(self.tabs) - 1]))
        widgetObjectName = "widget" + str(len(self.widgets) - 1)
        self.widgets[len(self.widgets) - 1].setObjectName(_fromUtf8(widgetObjectName))

        self.gridLayouts[len(self.gridLayouts) - 1].addWidget(self.widgets[len(self.widgets) - 1], 0, 0, 1, 1)
        self.captureArea.addTab(self.tabs[len(self.tabs) - 1], _fromUtf8(""))

        self.captureArea.setCurrentWidget(self.tabs[(len(self.tabs) - 1)])

        #self.tab = QtGui.QWidget()
        #self.tab.setObjectName(_fromUtf8("tab"))
        #self.gridLayout_3 = QtGui.QGridLayout(self.tabs[0])
        #self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        #self.widget = QtGui.QWidget(self.tab)
        #self.widget.setObjectName(_fromUtf8("widget"))
        #self.gridLayout_3.addWidget(self.widgets[0], 0, 0, 1, 1)
        #self.captureArea.addTab(self.tabs[0], _fromUtf8(""))

        #self.tab_2 = QtGui.QWidget()
        #self.tab_2.setObjectName(_fromUtf8("tab_2"))
        #self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        #self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        #self.widget_2 = QtGui.QWidget(self.tab_2)
        #self.widget_2.setObjectName(_fromUtf8("widget_2"))
        #self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 1)
        #self.captureArea.addTab(self.tab_2, _fromUtf8(""))

        self.gridLayout_2.addWidget(self.captureArea, 0, 0, 1, 1)


        #self.capture_thread = threading.Thread(target=self.grab, args=(1, q, 1920, 1080, 60))
        #self.capture_thread2 = threading.Thread(target=self.grab, args=(1, q, 1920, 1080, 60))

        #self.setupUi(self)

        #self.startButton.clicked.connect(self.start_clicked)

        #self.window_width = self.ImgWidget.frameSize().width()
        self.window_width = self.widgets[0].frameSize().width()
        self.window_height = self.widgets[0].frameSize().height()

        #self.ImgWidget = OwnImageWidget(self.widget)

        #self.cvHandler = CVHandler(self.widgets[0], 0)
        self.openGLHandler = OpenGLHandler()
        self.gridLayouts[0].addWidget(self.openGLHandler)

    def newTab(self):
        self.tabs.append(QtGui.QWidget())
        tabObjectName = "tab" + str(len(self.tabs) - 1)
        self.tabs[(len(self.tabs) - 1)].setObjectName(_fromUtf8(tabObjectName))

        self.gridLayouts.append(QtGui.QGridLayout(self.tabs[len(self.tabs) - 1]))
        gridLayoutObjectName = "gridLayout" + str(len(self.gridLayouts) - 1)
        self.gridLayouts[len(self.gridLayouts) - 1].setObjectName(_fromUtf8(gridLayoutObjectName))

        self.widgets.append(QtGui.QWidget(self.tabs[len(self.tabs) - 1]))
        widgetObjectName = "widget" + str(len(self.widgets) - 1)
        self.widgets[len(self.widgets) - 1].setObjectName(_fromUtf8(widgetObjectName))

        self.gridLayouts[len(self.gridLayouts) - 1].addWidget(self.widgets[len(self.widgets) - 1], 0, 0, 1, 1)
        self.captureArea.addTab(self.tabs[len(self.tabs) - 1], _fromUtf8(""))

        self.captureArea.setCurrentWidget(self.tabs[(len(self.tabs) - 1)])

    def removeTab(self, index):
        widget = self.captureArea.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.captureArea.removeTab(index)



    def start_clicked(self):
        #global running
        #self.cvHandler = CVHandler(self.widget)
        #self.cvHandler.start_clicked()

        self.newTab()
        self.newTab()
        self.newTab()
        self.cvHandler2 = CVHandler(self.widgets[1], 0)
        self.cvHandler2.start_clicked()

        self.cvHandler3 = CVHandler(self.widgets[2], 1)
        self.cvHandler3.start_clicked()

        #running = True
        #self.capture_thread.start()
        #self.captureArea.setCurrentWidget(self.tabs[2])
        #self.capture_thread2.start()




    def stop_playback(self):
        self.cvHandler.stop_playback()

    def stream_setup(self):
        pass
        #connectToIPWindow = Ui_connectToIPBox(QtGui.QDialog)
        #print(connectToIPWindow)

