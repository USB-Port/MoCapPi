###############################################################################
#Name:
#   CVHandler.py
#Author:
#   USB-Port
#What is this Class for:
#   This class handles all things related to OpenCV and video processing, this includes everything that OpenCV can do.
#   Open VIdeo files, Grabs frames from them, opens a stream, process the frame, convert it to a frame PYQT can read.
#   Track objects in frames, apply an mask to a frame. If it does anything with OpenCV, it goes here, in this class.
################################################################################




import sys
import cv2
import threading
import time
import numpy as np
import imutils
from collections import deque
import argparse
from multiprocessing import Queue
from OpenGL import GL
from GraphHandler import *
from Point import *
import re
import pyqtgraph.opengl as gl
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4 import QtCore, QtGui
import json
from pathlib import Path
from io import open



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s




try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


#The class still inherit from QWidget
class CVHandler(QtGui.QWidget):


    #To create a new OCV Handler you must pass in a QWidget, cam, and a OpenGLhandler. The cam veriable can be numbers 0-2 depending on how many
    #cameras you have connected, 0 being first, or a IP adderess like "tcp://192.168.2.9:9092". The OpenGLHandler being passed
    #in here is for testing ONLY. this will be done differently once we start using 6 cameras. Or it may be kept this way
    # and each camera can update the OpenGLHandler, then the OpenGLHandler can concregate the point positions.
    #The QWidget is a tab that tells the class where to put the video feed. NOTE, Once we get everything all sorted,
    # we will not need to show the video feed unless we need to, so a default None could be used.
    def __init__(self, QWidget, cam, camNum, GraphHandler=None):
        super(CVHandler, self).__init__()
        #this just assigns the class veriable to what was passed in
        self.camNum = camNum

        if(camNum == 101):
            calibrateFile = Path("./101.json")
            if calibrateFile.is_file():
                print("File found")

                data = json.load(open('./101.json'))

                self.mtx = data["mtx"]
                self.dist = data["dist"]
                self.rvecs = data["rvecs"]
                self.tvecs = data["tvecs"]


        if (camNum == 102):
            calibrateFile = Path("./102.json")
            if calibrateFile.is_file():
                print("File found")

                data = json.load(open('./102.json'))

                self.mtx = data["mtx"]
                self.dist = data["dist"]
                self.rvecs = data["rvecs"]
                self.tvecs = data["tvecs"]



        if (camNum == 103):
            calibrateFile = Path("./103.json")
            if calibrateFile.is_file():
                print("File found")

                data = json.load(open('./103.json'))

                self.mtx = data["mtx"]
                self.dist = data["dist"]
                self.rvecs = data["rvecs"]
                self.tvecs = data["tvecs"]



        if (camNum == 100):
            calibrateFile = Path("./100.json")
            if calibrateFile.is_file():
                print("File found")

                data = json.load(open('./100.json'))

                self.mtx = data["mtx"]
                self.dist = data["dist"]
                self.rvecs = data["rvecs"]
                self.tvecs = data["tvecs"]

        self.image = None
        self.running = False
        self.capture_thread = None
        self.widget = QWidget
        self.queue = Queue()


        self.points = []

        self.pos = np.empty((0, 3))
        self.posArray = []
        self.numCurrentTrackPoints = 0
        self.numLastFrameTrackPoints = 0
        self.file = None
        self.file = open("motion.txt", "a")
        self.file.write("addpoint\n")

        self.calibrationMode = False
        self.objp = np.zeros((9 * 7, 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:7, 0:9].T.reshape(-1, 2)
        #self.objp = self.objp.reshape(-1, 1, 3)
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # Arrays to store object points and image points from all the images.
        self.objpoints = []  # 3d point in real world space
        self.imgpoints = []  # 2d points in image plane.
        self.takePicture = True

        self.count = 0


        self.graphHandler = GraphHandler

        #This is how you create a thread and pass in arguments in python. The function is called  grab(cam, w, h, FPS)
        self.capture_thread = threading.Thread(target=self.grab, args=(cam, 1920, 1080, 60))

        #This is the width and height of the QWidget that was passed in
        self.window_width = QWidget.frameSize().width()
        self.window_height = QWidget.frameSize().height()

        self.ImgWidget = OwnImageWidget(QWidget)

        #These 3 lines create a Qtimer, and connects the method update_frame to it.
        #What this does, is every 1ms, call the "update Frame" methods.
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

        sensitivity = 15

        self.lower = 200
        self.upper = 255
        self.radiusBound = 1

        #These 2 lines are another way to set the mask. I was trying different ways, Not sure which way is better, both seem the same
        #self.lower = np.array([78, 158, 124])
        #self.upper = np.array([138, 255, 255])

        #This seems to be code that takes in argument from the command line. Not needed but I think it breaks if you remove.
        #Meh, remove it later
        ap = argparse.ArgumentParser()
        ap.add_argument("-v", "--video",
                        help="path to the (optional) video file")
        ap.add_argument("-b", "--buffer", type=int, default=64,
                        help="max buffer size")
        self.args = vars(ap.parse_args())
        self.pts = deque(maxlen=self.args["buffer"])

    #####################################################################################
        ###############THE below code is just for testing Will either delete this or move it#######
        # This code is just for debugging the mask on the cameras, cool to play around with.


        self.setObjectName(_fromUtf8("Form"))
        self.resize(568, 184)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 2, 1, 2, 1)
        self.textEdit_3 = QtGui.QTextEdit(self)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout.addWidget(self.textEdit_3, 4, 1, 2, 1)
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(self)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.gridLayout.addWidget(self.horizontalSlider_2, 3, 0, 1, 1)
        self.horizontalSlider_3 = QtGui.QSlider(self)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.gridLayout.addWidget(self.horizontalSlider_3, 5, 0, 1, 1)

        self.horizontalSlider.setRange(0, 255)
        self.horizontalSlider_2.setRange(0,255)
        self.horizontalSlider_3.setRange(0,100)
        self.pushButton.clicked.connect(self.updateMasking)

        self.horizontalSlider.setValue(240)
        self.horizontalSlider_2.setValue(255)
        self.horizontalSlider_3.setValue(45)


        self.connect(self.horizontalSlider, QtCore.SIGNAL("valueChanged(int)"),self.updateMasking)
        self.connect(self.horizontalSlider_2, QtCore.SIGNAL("valueChanged(int)"), self.updateMasking)
        self.connect(self.horizontalSlider_3, QtCore.SIGNAL("valueChanged(int)"), self.updateMasking)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def updateMasking(self):
        self.lower = self.horizontalSlider.value()
        print("lower "+str(self.lower))
        self.textEdit.setText(str(self.lower))

        self.upper = self.horizontalSlider_2.value()
        self.textEdit_2.setText(str(self.upper))

        self.radiusBound = self.horizontalSlider_3.value()
        self.textEdit_3.setText(str(self.radiusBound))

    def valuechange(self):
        self.textEdit.setText(str(self.horizontalSlider.value()))
        self.textEdit_2.setText(str(self.horizontalSlider_2.value()))
        self.textEdit_3.setText(str(self.horizontalSlider_3.value()))

        # END of Debug mask stuff
        #####################################################################################

    def retranslateUi(self):
        self.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Lower Bound", None))
        self.label_2.setText(_translate("Form", "Upper Bound", None))
        self.pushButton_2.setText(_translate("Form", "Quit", None))
        self.pushButton.setText(_translate("Form", "Set", None))
        self.label_3.setText(_translate("Form", "Radius", None))


    #########################################

    #This button is called from the captureArea which is from the Main.py. The green play button. I tend to use this method
    #for debuggin stuff.
    def start_clicked(self):
        self.running = True
        self.capture_thread.start()

    #This is the red stop button, simular to the Green play button. This works great. Stops the video
    #But can someone figure out how to call this when the user quits the application while the video is playing. That's a crash
    def stop_playback(self):
        self.running = False
        self.capture_thread.join()
        self.deleteLater()

    #This function is called every 1ms because of the timer.
    #so to fix bugs, I added in the
    #self.running == True. Change this to false when you want to stop the video or timer.
    def update_frame(self):

        #So this is the bulk of the class. This grabs the frame from the camera and do stuff with it.

        #The grab method puts every frame in a queue. so if the queue is not empty and we are running, then there is a
        #frame that needs processing.
        if not self.queue.empty() and self.running == True:

            #The will get us the first frame in the queue and then remove it from the queue, like a 2 in 1
            frame = self.queue.get()

            #frame is a dictionry, so this will give us the data accotiated with the key value "img"
            img = frame["img"]

            height, width, bpc = img.shape
            bpl = bpc * width

            #These 3 lines are to keep the correct aspect ratio. This might not be needed.
            scale_w = float(self.window_width) / float(width)
            scale_h = float(self.window_height) / float(height)
            scale = min([scale_w, scale_h])

            #Can't have a scale of 0 for some reason
            if scale == 0:
                scale = 1

            ### Checker Board Calibration Code ###
            if (self.calibrationMode == True and self.takePicture == True):
                self.takePicture = False
                self.__takeCalibrationPhoto(img)

            ##End Checker Board Calibration code ###


            ### STart of tracking code
            if(self.calibrationMode == False):
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


                newcameramtx, roi = cv2.getOptimalNewCameraMatrix(np.asarray(self.mtx), np.asarray(self.dist), (width, height), 1, (width, height))
                img = cv2.undistort(img, np.asarray(self.mtx), np.asarray(self.dist), None, newcameramtx)


                blurred = cv2.GaussianBlur(img, (11,11), 0)
                threshed = cv2.threshold(blurred, self.lower, self.upper, cv2.THRESH_BINARY)[1]
                threshed = cv2.erode(threshed, None, iterations=2)
                threshed = cv2.dilate(threshed, None, iterations=4)


                cnts = cv2.findContours(threshed.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)[-2]


                i = 0

                ###self.pos = np.empty((len(self.points), 3))

                self.numCurrentTrackPoints = 0

                for (i, c) in enumerate(cnts):

                    ((x, y), radius) = cv2.minEnclosingCircle(c)


                    M = cv2.moments(c)

                    # this is center of a circle
                    center = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])

                    # These 2 points are the center of the mask object found. This only works on Balls
                    xx = int(M['m10'] / M['m00'])
                    yy = int(M['m01'] / M['m00'])


                    ###self.pos[self.t] = (xx, yy, 0)
                    self.posArray.append([xx, yy, 0])
                    #print(str(self.posArray))
                    self.numCurrentTrackPoints = self.numCurrentTrackPoints + 1

                    # only proceed if the radius meets a minimum size
                    ###if radius < self.radiusBound:
                        # draw the circle and centroid on the frame,
                        # then update the list of tracked points
                    cv2.circle(img, (int(xx), int(yy)), int(radius),
                                   (0, 255, 255), 2)
                    cv2.circle(img, center, 5, (0, 0, 255), -1)

                ###if self.pos.shape[0] != len(cnts):
                    ###self.graphHandler.setPoints(self.pos)

                if self.numCurrentTrackPoints != self.numLastFrameTrackPoints:
                    if(self.file is not None):
                        for line in self.pos:

                            self.file.write("%s " % line)
                        #self.file.write("\n")
                        self.file.write("\naddpoint\n")
                    self.pos = np.asarray(self.posArray)
                    #print(str(self.pos))

                    ###############
                    # Instead of passing to graphHandler, Pass to a different class to handle all point data

                    self.graphHandler.setPoints(self.pos)


                elif self.graphHandler:
                    if (self.file is not None):

                        for line in self.pos:
                            self.file.write("%s " % line)
                        #self.file.write("\n")
                        self.file.write("\ntranspoint\n")

                    #print(str(self.pos))
                    self.pos = np.asarray(self.posArray)

                    ###############
                    #Instead of passing to graphHandler, Pass to a different class to handle all point data

                    self.graphHandler.translatePoints(self.pos)

                #clear out whole list
                del self.posArray[:]

                self.numLastFrameTrackPoints = self.numCurrentTrackPoints

            ####### End of tracking code #######
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

            #convert the img data to a QImage Format
            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)

            #pass that image to get updated
            self.ImgWidget.setImage(image)
            #cv2.imshow("Frame", img)

            #IF running is false, stop the timer
            if self.running == False:
                self.timer.stop()


    def grab(self, cam, width, height, fps):

        #Open up a video camera or stream
        #This is the line that does not work in Linux, so if someone finds a way to make this line work in other OS's
        #we could support more OS's
        capture = cv2.VideoCapture(cam)
        #Set various things about the captured feed
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        capture.set(cv2.CAP_PROP_FPS, fps)

        #While we are running, we have frames to gather
        while (self.running):
            self.frame = {}

            #The grab and retrive method is the same as a "capture.read()" Just grabs and retrive, Docs can explain it better
            capture.grab()
            ret, img = capture.retrieve(0)

            #flip the image
            img = cv2.flip(img, 1)

            #If the captrue cannot retrive a frame from the camera, then ret will be false. so running = false now
            if(ret == False):
                self.running = False

            #retval, img = capture.read()

            #add img to the key value of img, recall frame is a dictionary
            self.frame["img"] = img

            #If the queue is less than 10, add the frame to the queue, else, drop the frame into the void
            if self.queue.qsize() < 10:
                self.queue.put(self.frame)
                #self.queue.put(img)
            else:
                pass
                #Here you can print out a message so you can tell how many frames you are dropping
                #print(self.queue.qsize())
            
    #This method is for opening a video file
    def openVideoFile(self, fileName):
        self.capture_thread = threading.Thread(target=self.grab, args=(fileName, 1920, 1080, 60))
        self.running = True
        self.capture_thread.start()

    #This is for the OpenGLHandler
    def getPos(self):
        temp = []
        temp.append(self.cx)
        temp.append(self.cy)
        return temp


    #Not Implemented
    def stream_setup(self):
        pass
        #connectToIPWindow = Ui_connectToIPBox(QtGui.QDialog)
        #print(connectToIPWindow)

    def isRunning(self):
        return self.running

    def recordMotion(self):
        self.file = open("motion.txt", "+w")

    def stopRecording(self):
        self.file.close()
        self.file = None

    def setPoints(self):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(img, (11, 11), 0)
        threshed = cv2.threshold(blurred, self.lower, self.upper, cv2.THRESH_BINARY)[1]
        threshed = cv2.erode(threshed, None, iterations=2)
        threshed = cv2.dilate(threshed, None, iterations=4)

        cnts = cv2.findContours(threshed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        i = 0
        self.points = []
        print("Found "+str(len(cnts))+" points")
        for (i, c) in enumerate(cnts):
            # print("I is :" + str(i))
            point = Point()
            #self.points.append(point)

            ((x, y), radius) = cv2.minEnclosingCircle(c)

            point.setX(x)
            point.setY(y)
            point.setZ(0)
            point.setRadius(radius)

            M = cv2.moments(c)

            # this is center of a circle
            point.setCenter((int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])))

            # These 2 points are the center of the mask object found. This only works on Balls
            xx = int(M['m10'] / M['m00'])
            yy = int(M['m01'] / M['m00'])
            point.setPosition(xx, yy, 0)

            # self.openGLHandler.setPos(self.cx, self.cy)

            # print("cx is: " + str(cx))
            # print("cy is: " + str(cy))

            # only proceed if the radius meets a minimum size
            if point.getRadius() < self.radiusBound:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                #cv2.circle(img, (int(self.points[i].getX()), int(self.points[i].getY())),
                #           int(self.points[i].getRadius()),
                #           (0, 255, 255), 2)
                self.points.append(point)
                #point.printPosition()
                print("There is only " + str(len(self.points)))
                cv2.circle(img, point.getCenter(), 5, (0, 0, 255), -1)

        cv2.imshow("test", img)

        self.pos = np.empty((len(self.points), 3))
        t = 0
        for t in range(0, len(self.points)):
            self.pos[t] = (self.points[t].getX(), self.points[t].getY(), self.points[t].getZ())

        #print(str(self.pos))

        #self.graphHandler.setPoints(self.points)
        print(str(self.pos))
        self.graphHandler.setPoints(self.pos)
        #self.pts =self.points
        #if self.graphHandler:
            #self.graphHandler.addPoints(self.pts)

    def takeCalibrationPic(self):
        self.takePicture = True

    def __takeCalibrationPhoto(self, image):
        img = image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (7, 9), None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            self.objpoints.append(self.objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
            self.imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (7, 9), corners2, ret)
            #cv2.imshow("img", img)
            self.count = self.count + 1
            if(self.count == 50):
                ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(self.objpoints, self.imgpoints, gray.shape[::-1], None, None)

                mtx = mtx.tolist()
                dist = dist.tolist()
                rvecs = np.asarray(rvecs).tolist()
                tvecs = np.asarray(tvecs).tolist()

                data = {"mtx": mtx, "dist": dist, "rvecs": rvecs, "tvecs": tvecs}
                fname = "102.json"

                with open(fname, "w") as f:
                    json.dump(data, f)







#This class is for updating the QWidget with the video frame gotten from OpenCV, don't need to change it.
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



