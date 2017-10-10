from PyQt4 import QtCore, QtGui
import sys
import cv2
import threading
import time
import numpy as np
import imutils
from collections import deque
import argparse
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

        #New Stuff for Tracking
        sensitivity = 15
        self.lower = (0, 100, 100)
        self.upper = (20, 255, 255)

        #self.lower = np.array([78, 158, 124])
        #self.upper = np.array([138, 255, 255])
        ap = argparse.ArgumentParser()
        ap.add_argument("-v", "--video",
                        help="path to the (optional) video file")
        ap.add_argument("-b", "--buffer", type=int, default=64,
                        help="max buffer size")
        self.args = vars(ap.parse_args())
        self.pts = deque(maxlen=self.args["buffer"])


    def start_clicked(self):
        self.running = True
        self.capture_thread.start()

    def stop_playback(self):
        self.running = False
        self.capture_thread.join()
        self.deleteLater()


    def update_frame(self):
        if not self.queue.empty() and self.running == True:
            frame = self.queue.get()
            img = frame["img"]


            img_height, img_width, img_colors = img.shape
            scale_w = float(self.window_width) / float(img_width)
            scale_h = float(self.window_height) / float(img_height)
            scale = min([scale_w, scale_h])

            if scale == 0:
                scale = 1

            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

            #changes this from BGR2RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            height, width, bpc = img.shape
            bpl = bpc * width

            #image = QtGui.QImage(frame.tostring(), 640, 480, QtGui.QImage.Format_RGB888).rgbSwapped()
            #pixmap = QtGui.QPixmap.fromImage(image)

            #New Stuff for Tracking
            self.mask = cv2.inRange(img, self.lower, self.upper)
            self.mask = cv2.erode(self.mask, None, iterations=2)
            self.mask = cv2.dilate(self.mask, None, iterations=2)

            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(self.mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # only proceed if the radius meets a minimum size
                if radius > 10:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(img, (int(x), int(y)), int(radius),
                               (0, 255, 255), 2)
                    cv2.circle(img, center, 5, (0, 0, 255), -1)

            # update the points queue
            self.pts.appendleft(center)

            # loop over the set of tracked points
            for i in range(1, len(self.pts)):
                # if either of the tracked points are None, ignore
                # them
                if self.pts[i - 1] is None or self.pts[i] is None:
                    continue

                # otherwise, compute the thickness of the line and
                # draw the connecting lines
                thickness = int(np.sqrt(self.args["buffer"] / float(i + 1)) * 2.5)
                #cv2.line(img, self.pts[i - 1], self.pts[i], (0, 0, 255), thickness)

            #End new stuff, This comment is here just in case I break things


            #After tracking is done, convert to RGB for PyQt
            img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
            self.ImgWidget.setImage(image)
            cv2.imshow("Frame", img)
            if self.running == False:
                self.timer.stop()


    def grab(self, cam, width, height, fps):


        capture = cv2.VideoCapture(cam)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        capture.set(cv2.CAP_PROP_FPS, fps)

        while (self.running):
            frame = {}
            capture.grab()
            ret, img = capture.retrieve(0)

            if(ret == False):
                self.running = False

            #retval, img = capture.read()
            frame["img"] = img

            if self.queue.qsize() < 10:
                self.queue.put(frame)
                #self.queue.put(img)
            else:
                pass
                #print(self.queue.qsize())
            

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

