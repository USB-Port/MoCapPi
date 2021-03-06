###############################################################################
#Name:
#   CaptureArea.py
#Author:
#   USB-Port
#What is this Class for:
#   This class handles the center Widget. The one with tabs. The ideal behind this tabs is to be able to open and view
#   several different motion captures at once in easy to use tabs. The first tab will always show a live view, while other
#   tabs can show recorded motions in either from a video or from a recorded motion file that can be played in OpenGL.
#   Since this class handles playback and one day recording of motion, this is a very import class for this project and
#   the one class that matters the most.
################################################################################


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
from MaskingDebug import  *
from GraphHandler import *
from ConsoleOutput import *
import pyqtgraph.opengl as gl




try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

running = False
capture_thread = None
q = Queue()
p = Queue()


#Every single class that makes something that goes on the Main App, has to inherent from QtGui.QWidget
class CaptureArea(QtGui.QWidget):


    #This is how you pass a QWidget (MainWindow from main.py) to a class
    def __init__(self, QWidget, consoleOutput, parent=None):
        QtGui.QWidget.__init__(self,parent)
        #Unlike better languages, you have to manually call the super constructor
        super(CaptureArea, self).__init__()

        #this is just used to print to console output
        self.consoleOut = consoleOutput

        #This is auto generated code. Notice the names
        self.gridLayout_2 = QtGui.QGridLayout(QWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.captureArea = QtGui.QTabWidget(QWidget)
        self.captureArea.setObjectName(_fromUtf8("captureArea"))

        #Stores the 4 camera threads
        self.cvObjectLists = []

        #The graph handler object
        self.graphHandler = GraphHandler(self, consoleOutput)

        #Each tabs has 3 parts, they are lists so the user can make unlimited tabs
        self.tabs = []
        self.gridLayouts = []
        self.widgets = []

        self.captureArea.insertTab(3, self.graphHandler, "plot")

        #after creating all the tabs for capture area, add it to the layout. This is the whole otter layout.
        self.gridLayout_2.addWidget(self.captureArea, 0, 0, 1, 1)

        self.connect(self.gridLayout_2, QtCore.SIGNAL("resized()"), self.onResize)

        self.newTab()
        self.newTab()
        self.newTab()


    def resizeEvent(self, evt=None):
        print("HEYT \n")
        self.emit(QtCore.SIGNAL("resize()"))
        print("HEYT \n")

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

        #this sets the last tab is the current tab
        #self.captureArea.setCurrentWidget(self.tabs[(len(self.tabs) - 1)])

    def removeTab(self, index):
        widget = self.captureArea.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.captureArea.removeTab(index)



    def start_clicked(self):
        lastWidget = self.getWidget()
        self.cvHandler3 = CVHandler(self.widgets[lastWidget], "tcp://192.168.2.6:9092", self.graphHandler)
        self.cvHandler3.start_clicked()

    def connectToCameras(self):
        print("TEST")
        self.captureArea.setCurrentWidget(self.tabs[0])

        lastWidget = self.getWidget()

        try:
            cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.100:9092",100, self.graphHandler)
            self.cvObjectLists.append(cvHandler)
            self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.100")

        try:
            #cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.101:9092", 101, self.graphHandler)
            #self.cvObjectLists.append(cvHandler)
            self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.101")

        lastWidget = self.getWidget()

        try:
            #cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.102:9092", 102, self.graphHandler)
            #self.cvObjectLists.append(cvHandler)
            self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.102")

        lastWidget = self.getWidget()

        try:
            cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.103:9092",103, self.graphHandler)
            #self.cvObjectLists.append(cvHandler)
            #self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.103")

        lastWidget = self.getWidget()

        for cv in self.cvObjectLists:
            cv.start_clicked()



    def deleteThisLater(self):
        self.graphHandler.testtest()

    def recordMotion(self):
        #self.cvHandler2.recordMotion()
        if (len(self.cvObjectLists) > 0):
            for cv in self.cvObjectLists:
                cv.recordMotion()
        else:
            self.consoleOut.outputText("No cameras connected")

    def stopRecording(self):
        if (len(self.cvObjectLists) > 0):
            for cv in self.cvObjectLists:
                cv.stopRecording()
        else:
            self.consoleOut.outputText("No cameras connected")

    def takeCalibrationPicture(self):
        if(len(self.cvObjectLists) > 0):
            for cv in self.cvObjectLists:
                self.consoleOut.outputText("Taking Pictures")
                cv.takeCalibrationPic()
        else:
            self.consoleOut.outputText("No cameras connected")

    def stop_playback(self):
        try:
            self.cvHandler2.stop_playback()
            self.consoleOut.outputText("Video has stopped")
        except:
            self.consoleOut.outputText("No camera connected at this time")


    def playBackMotion(self):
        self.graphHandler.playbackMotion()


    def connectToIP(self, ipAddress, test):
        self.newTab()
        test.connectToStream(self)


    def getWidget(self):
        #CaptureArea.newTab()
        #lastTab = len(self.tabs) - 1
        lastWidget = len(self.widgets) - 1
        return int(lastWidget)

    def getGraph(self):
        return self.graphHandler

    def openVideoFile(self, fileName):
        pass

    def openMaskingDebugWindow(self):
        self.debugWin = MaskingDebug()

    def onResize(self):
        self.window_width = self.widgets[0].frameSize().width()
        self.window_height = self.widgets[0].frameSize().height()
        self.openGLHandler.updateWindowSize(self.window_width, self.window_height)

    def getWindowHeight(self):
        return self.window_height
    def getWindowWidth(self):
        return self.window_width


    def updateWindowSize(self):
        #print("wht the fuck")
        self.window_width = self.captureArea.frameSize().width()
        self.window_height = self.captureArea.frameSize().height()

    #this is going to check if the camera is recording, because there are 6 cam, we need an int
    def isRunning(self, cam=0):
        #self.cvHandler2[0].isRunning()
        return self.cvHandler2.isRunning()

    def updatePoints(self):
        self.cvHandler2.setPoints()
        print("test")
    '''
    def rectify(self):
        cv2.stereoCalibrate()

        rvec1 = np.array(self.cvObjectLists[0].rvecs).transpose()
        tvec1 = np.array(self.cvObjectLists[0].tvecs).transpose()
        mtx1 = np.array(self.cvObjectLists[0].mtx)
        dist1 = np.array(self.cvObjectLists[0].dist)

        rvec2 = np.array(self.cvObjectLists[1].rvecs).transpose()
        tvec2 = np.array(self.cvObjectLists[1].tvecs)
        mtx2 = np.array(self.cvObjectLists[1].mtx)
        dist2 = np.array(self.cvObjectLists[1].dist)

        rvecout = np.matmul(np.linalg.inv(rvec2),rvec1)
        tvecout = np.matmul(np.linalg.inv(tvec2)*tvec1)
        #rvecout, tvecout =cv2.composeRT(rvec1,tvec1,rvec2,tvec2)

        r1, r2, p1, p2, Q = cv2.stereoRectify(mtx1, mtx2, dist1, dist2, (1280,720),rvecout,tvecout)
        print(r1)
        print(r2)
        print(p1)
        print(p2)
        print(Q)
    '''