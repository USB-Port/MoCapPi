from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
import sys
import cv2
import numpy as np
import threading
import time
from multiprocessing import Queue

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

running = False
capture_thread = None
q = Queue()


class CaptureArea(QtGui.QWidget):

    def __init__(self, QWidget):
        super(CaptureArea, self).__init__()
        self.gridLayout_2 = QtGui.QGridLayout(QWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.captureArea = QtGui.QTabWidget(QWidget)
        self.captureArea.setObjectName(_fromUtf8("captureArea"))
        self.captureArea.setTabsClosable(False)
        #self.captureArea.tabCloseRequested(lambda: self.closeTab(self.captureArea.currentIndex()))

        self.tabs = [0]
        self.gridLayouts = [0]
        self.widgets = [0]

        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.captureArea.addTab(self.tab, _fromUtf8(""))

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.widget_2 = QtGui.QWidget(self.tab_2)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 1)
        self.captureArea.addTab(self.tab_2, _fromUtf8(""))

        self.gridLayout_2.addWidget(self.captureArea, 0, 0, 1, 1)


        self.capture_thread = threading.Thread(target=self.grab, args=(0, q, 1920, 1080, 60))
        #self.setupUi(self)

        #self.startButton.clicked.connect(self.start_clicked)

        #self.window_width = self.ImgWidget.frameSize().width()
        self.window_width = self.widget.frameSize().width()
        self.window_height = self.widget.frameSize().height()
        self.ImgWidget = OwnImageWidget(self.widget)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

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
        global running
        running = True
        self.capture_thread.start()

    def update_frame(self):
        if not q.empty():
            frame = q.get()
            img = frame["img"]

            img_height, img_width, img_colors = img.shape
            scale_w = float(self.window_width) / float(img_width)
            scale_h = float(self.window_height) / float(img_height)
            scale = min([scale_w, scale_h])

            if scale == 0:
                scale = 1

            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, bpc = img.shape
            bpl = bpc * width
            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
            self.ImgWidget.setImage(image)

    def closeEvent(self, event):
        global running
        running = False

    def grab(self, cam, queue, width, height, fps):
        global running
        capture = cv2.VideoCapture(cam)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        capture.set(cv2.CAP_PROP_FPS, fps)

        while (running):
            frame = {}
            capture.grab()
            retval, img = capture.retrieve(0)
            frame["img"] = img

            if queue.qsize() < 10:
                queue.put(frame)
            else:
                print(queue.qsize())


class OwnImageWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(OwnImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        sz = image.size()
        self.setMinimumSize(sz)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QtCore.QPoint(0, 0), self.image)
        qp.end()