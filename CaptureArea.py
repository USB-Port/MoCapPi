###############################################################################
#Name:
#   CaptureArea.py

#What is this Class for:
#   This class handles the center Widget. The one with tabs. The ideal behind this tabs is to be able to open and view
#   several different motion captures at once in easy to use tabs. The first tab will always show a live view, while other
#   tabs can show recorded motions in either from a video or from a recorded motion file that can be played in OpenGL.
#   Since this class handles playback and one day recording of motion, this is a very import class for this project and
#   the one class that matters the most.
#
#What Can I do here:
#   Create tabs, Each tabs is made up of three parts that you should know. Tabs, gridLayouts and Widgets. Each tab is a
#   made up of a gridlayout and inside each gridlayout is a Widget. So a new tab is made by putting a widget inside a tab
#   then by putting the gridlayout inside that widget. This is done because most of everything needs to go into a widget
#   and those widgets should be in a layout (but doesn't have to be
#
#   Note: OpenGL Widget SHOULD NOT go in a Widget, this messes it up. But OpenGL Widget still goes into a Layout.
#
#What needs to be done in this class:
#   A lot, this is where the tracking Stick person will be, this is where tracking is be displayed. (displayed, not made)
#   -Improve the layouts - OpenGL widget seems to be "going out of the layout" Not sure why. Might be a bug in OpenGL class
#   -Delete Tabs - cant delete tabs but not a big deal and should be a easy fix. but error check deleting tabs in use
#   -Improve rebustness - Still crashes sometimes
#   -Naming the tabs. - No names on the tabs. not a big deal
#   -You know that "+" sign at the end of the tab in Notepad++. Add that. and one more thing Good Luck LOL
#
#Bugs:
#   If the user is on the tab that is loading up a video, the video will never show at all.
#   Super frustrainting bug. This bug also mess up the connect to stream button. Not a clue on how to fix..........Yet.
#
#Things to know:
#   This class creates the instance of CVHandler and OpenGLHandler because it displays these things in the tabs. Since
#   the main class does NOT create the CVhandler or OpenGL, you sill find some methods in Main that indirectly calls
#   methods in those two classes from Main by going through this Capture Area Class.
#
#   To better understand this: Look at the "Start_Motion" method in the main.py file, that method calls a method in
#   this class, that calls the constructor in CVhandler classss. This is what I mean by indirectly calls a method.
#
#   Making some methods in CV handler class, STATIC might/could fix this work around.
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

        self.cvObjectLists = []

        #The graph handler object
        self.graphHandler = GraphHandler(self, consoleOutput)

        #This line can make it where you cannot close the tabs
        #self.captureArea.setTabsClosable(False)

        #this was how I was going to close tabs, Doesn't work idk why....yet
        #self.captureArea.tabCloseRequested(lambda: self.closeTab(self.captureArea.currentIndex()))

        #Each tabs has 3 parts, they are lists so the user can make unlimited tabs
        self.tabs = []
        self.gridLayouts = []
        self.widgets = []

        self.captureArea.insertTab(3, self.graphHandler, "plot")

        #Add a new QWidget to the tab list
        #self.tabs.append(QtGui.QWidget())
        #tabObjectName = "tab" + str(len(self.tabs) - 1)
        #self.tabs[(len(self.tabs) - 1)].setObjectName(_fromUtf8(tabObjectName))

        #Add a new Gridlayout to to the Tab Widgets and add that to the grid layout list
        #self.gridLayouts.append(QtGui.QGridLayout(self.tabs[len(self.tabs) - 1]))
        #gridLayoutObjectName = "gridLayout" + str(len(self.gridLayouts) - 1)
        #self.gridLayouts[len(self.gridLayouts) - 1].setObjectName(_fromUtf8(gridLayoutObjectName))

        #add the list of tabs widgets to the widgets list. You will pass these widgets to OpenCVHandler
        #self.widgets.append(QtGui.QWidget(self.tabs[len(self.tabs) - 1]))
        #widgetObjectName = "widget" + str(len(self.widgets) - 1)
        #self.widgets[len(self.widgets) - 1].setObjectName(_fromUtf8(widgetObjectName))

        #self.gridLayouts[len(self.gridLayouts) - 1].addWidget(self.widgets[len(self.widgets) - 1], 0, 0, 1, 1)

        #This line, adds a tab to the Capture area. I add the last index tab.
        #self.captureArea.addTab(self.tabs[len(self.tabs) - 1], _fromUtf8(""))

        #This just sets the last tab as the active tab.
        #self.captureArea.setCurrentWidget(self.tabs[(len(self.tabs) - 1)])


        #The follow commented out code is a relic from the pass. But I recall that a
        # Widget is not added to the first tab since it is a OpenGL widget in Tab[0]

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

        #after creating all the tabs for capture area, add it to the layout. This is the whole otter layout.
        self.gridLayout_2.addWidget(self.captureArea, 0, 0, 1, 1)


        #self.capture_thread = threading.Thread(target=self.grab, args=(1, q, 1920, 1080, 60))
        #self.capture_thread2 = threading.Thread(target=self.grab, args=(1, q, 1920, 1080, 60))

        #self.setupUi(self)

        #self.startButton.clicked.connect(self.start_clicked)

        #self.window_width = self.ImgWidget.frameSize().width()
        #self.window_width = self.widgets[0].frameSize().width()
        #self.window_height = self.widgets[0].frameSize().height()

        #self.ImgWidget = OwnImageWidget(self.widget)

        #self.cvHandler = CVHandler(self.widgets[0], 0)
        #self.gridLayouts[0].setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        #self.openGLHandler = OpenGLHandler(self)
        #self.graphHandler = GraphHandler(self)

        #self.graphHandler.opts['distance'] = 50

        #self.xgrid = gl.GLGridItem()
        #self.ygrid = gl.GLGridItem()
        #self.zgrid = gl.GLGridItem()

        #self.graphHandler.addItem(self.xgrid)
        #self.graphHandler.addItem(self.ygrid)
        #self.graphHandler.addItem(self.zgrid)


        #self.captureArea.addTab(self.tabs[len(self.tabs) - 1], _fromUtf8(""))


        #self.captureArea.addTab(self.tabs[1], _fromUtf8(""))

        #self.captureArea.insertTab(3, self.graphHandler, "plot")

        #self.captureArea.setCurrentWidget(self.tabs[(len(self.tabs) - 1)])





        #self.tabs[1].addWidget(self.graphHandler)




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
        pass
        # global running
        # self.cvHandler = CVHandler(self.widget)
        # self.cvHandler.start_clicked()

        # text = "http://"+ str(self.ip) +":9090/?action=stream?dummy=param.mjpg"
        lastWidget = self.getWidget()
        self.cvHandler3 = CVHandler(self.widgets[lastWidget], "tcp://192.168.2.6:9092", self.graphHandler)
        self.cvHandler3.start_clicked()


        # self.update()

        # running = True
        # self.capture_thread.start()

        # self.captureArea.setCurrentWidget(self.tabs[2])
        # self.capture_thread2.start()







    def connectToCameras(self):
        print("TEST")
        self.captureArea.setCurrentWidget(self.tabs[0])

        lastWidget = self.getWidget()

        try:
            cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.101:9092", self.graphHandler)
            self.cvObjectLists.append(cvHandler)
            self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.101")

        lastWidget = self.getWidget()

        try:
            cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.102:9092", self.graphHandler)
            self.cvObjectLists.append(cvHandler)
            self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.102")

        lastWidget = self.getWidget()

        try:
            cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.103:9092", self.graphHandler)
            self.cvObjectLists.append(cvHandler)
            self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.103")

        lastWidget = self.getWidget()

        try:
            cvHandler = CVHandler(self.widgets[lastWidget], "tcp://192.168.1.100:9092", self.graphHandler)
            self.cvObjectLists.append(cvHandler)
            self.newTab()
            # self.cvHandler2 = CVHandler(self.widgets[1], "tcp://192.168.2.201:9092", self.graphHandler)
            # self.cvHandler2.start_clicked()
            # self.consoleOut.outputText("Playing video from webcam")
        except:
            self.consoleOut.outputText("Error has occurred while connecting to 192.168.1.104")

        for cv in self.cvObjectLists:
            cv.start_clicked()



    def deleteThisLater(self):
        self.graphHandler.testtest()

    def recordMotion(self):
        self.cvHandler2.recordMotion()

    def stopRecording(self):
        if (len(self.cvObjectLists) > 0):
            for cv in self.cvObjectLists:
                cv.stopRecording()
        else:
            self.consoleOut.outputText("No cameras connected")

    def takeCalibrationPicture(self):
        if(len(self.cvObjectLists) > 0):
            for cv in self.cvObjectLists:
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
        #self.cvHandler2 = CVHandler(self.widgets[(len(self.tabs) - 1)], ipAddress)
        #self.cvHandler2.start_clicked()

    def getWidget(self):
        #CaptureArea.newTab()
        #lastTab = len(self.tabs) - 1
        lastWidget = len(self.widgets) - 1
        print(lastWidget)
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
        print("wht the fuck")
        self.window_width = self.captureArea.frameSize().width()
        self.window_height = self.captureArea.frameSize().height()

    #this is going to check if the camera is recording, because there are 6 cam, we need an int
    def isRunning(self, cam=0):
        #self.cvHandler2[0].isRunning()
        return self.cvHandler2.isRunning()

    def updatePoints(self):
        self.cvHandler2.setPoints()
        print("test")