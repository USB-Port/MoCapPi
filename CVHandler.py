from PyQt4 import QtCore, QtGui
import sys
import cv2
import threading
import time
import numpy as np
from multiprocessing import Queue

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class CVHandler(QtGui.QWidget):
    def __init__(self, QWidget, cam):
        super(CVHandler, self).__init__()
        self.image = None
        self.running = False
        self.capture_thread = None
        self.widget = QWidget
        self.queue = Queue()
        self.capture_thread = threading.Thread(target=self.grab, args=(cam, 1920, 1080, 60))

        self.window_width = QWidget.frameSize().width()
        self.window_height = QWidget.frameSize().height()

        self.ImgWidget = OwnImageWidget(QWidget)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)


    def start_clicked(self):
        self.running = True
        self.capture_thread.start()

    def stop_playback(self):
        self.running = False


    def update_frame(self):
        if not self.queue.empty():
            frame = self.queue.get()
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


    def grab(self, cam, width, height, fps):
        capture = cv2.VideoCapture(cam)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        capture.set(cv2.CAP_PROP_FPS, fps)

        while (self.running):
            frame = {}
            capture.grab()
            retval, img = capture.retrieve(0)
            frame["img"] = img

            if self.queue.qsize() < 10:
                self.queue.put(frame)
            else:
                print(self.queue.qsize())

    def openVideoFile(self, fileName):
        self.capture_thread = threading.Thread(target=self.grab, args=(fileName, 1920, 1080, 60))
        self.running = True
        self.capture_thread.start()



    def stream_setup(self):
        pass
        #connectToIPWindow = Ui_connectToIPBox(QtGui.QDialog)
        #print(connectToIPWindow)


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
