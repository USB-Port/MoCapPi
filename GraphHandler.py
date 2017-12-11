from PyQt4 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
import numpy as np
import pyqtgraph.opengl as gl
from numpy import *
import threading
from ConsoleOutput import *
from PyQt4 import QtCore, QtGui, QtOpenGL

from time import sleep

from OpenGL import GL
from Point import *
from time import sleep
import types
import re
from time import sleep

#pg.GraphicsLayoutWidget
class GraphHandler(gl.GLViewWidget):
    #This class takes a Capture Area Object so that it can pass a Widget to OpenCVHandler
    def __init__(self, GraphHandler, consoleOutput):
        gl.GLViewWidget.__init__(self)
        #pg.mkQApp()
        self.consoleOut = consoleOutput
        ## make a widget for displaying 3D objects

        self.pts = []
        self.opts['distance'] = 1000
        self.setBackgroundColor((1.0, 0.0, 0.0, 0.5))

        self.increment = 100
        self.ppt = None

        #self.setBackgroundColor(pg.mkColor(150,150,0))

        ## create three grids, add each to the view
        self.xgrid = gl.GLGridItem(color=(1.0,0.0,0.0,0.5))
        self.ygrid = gl.GLGridItem()
        self.zgrid = gl.GLGridItem()

        #self.points = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)
        #self.point.translate(5.0, 5.0, 5.0)


        self.axis = gl.GLAxisItem()
        #self.addItem(self.points)
        self.addItem(self.xgrid)
        self.addItem(self.ygrid)
        self.addItem(self.zgrid)
        #self.addItem(self.axis)


        pos = np.empty((1, 3))
        size = np.empty((1))
        color = np.empty((1, 4))
        pos[0] = (0, 0, 0)
        size[0] = 10.0
        color[0] = (1.0, 0.0, 0.0, 0.5)

        #self.p = gl.GLScatterPlotItem(pos=pos, size=size, color=color)
        #self.addItem(self.p)

        pos = np.empty((1, 3))
        size = np.empty((1))
        color = np.empty((1, 4))
        pos[0] = (100, 100, 100)
        size[0] = 10.0
        color[0] = (0.0, 1.0, 0.0, 0.5)


        self.zgrid.rotate(90, 0, 1, 0)
        self.ygrid.rotate(90, 1, 0, 0)
        self.ygrid.translate(0, -1000, 1000)
        self.zgrid.translate(-1000, 0, 1000)
        ## scale each grid differently
        self.xgrid.scale(100, 100, 100)
        self.ygrid.scale(100, 100, 100)
        self.zgrid.scale(100, 100, 100)
        #self.update()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.play)
        self.lineNumber = 0
        self.lastCommand = None
        self.playbackSpeed = 10
        self.pointSize = 80.0

    def testtest(self):
        self.increment = self.increment + 100
        pos = np.empty((1, 3))
        size = np.empty((1))
        color = np.empty((1, 4))
        pos[0] = (100, 100, self.increment)
        size[0] = 10.0
        color[0] = (0.0, 1.0, 0.0, 0.5)
        self.p.setData(pos=pos, size=size, color=color)

    def translatePoints(self, PosArray):

        #print(str(self.items))
        for item in self.items:
            if isinstance(item, gl.GLScatterPlotItem):
                item.setData(pos=PosArray)


    def setPoints(self, PosArray):

        for item in self.items:
            if isinstance(item, gl.GLScatterPlotItem):
                self.removeItem(item)

        size = np.empty((len(PosArray)))
        color = np.empty((len(PosArray), 4))

        for i in range(0, len(PosArray)):
            size[i] = self.pointSize
            color[i] = (1.0, 0.0, 0.0, 0.5)

        self.ppt = gl.GLScatterPlotItem(pos=PosArray, size=size, color=color, pxMode=False)
        self.addItem(self.ppt)


    def deletePoints(self):
        for item in self.items:
            if isinstance(item, gl.GLScatterPlotItem):
                self.removeItem(item)

        #def playbackMotion(self, fileName = "motion.txt"):
        #    t = threading.Thread(target=self.playbackMotionThread)
        #    t.start()

    def play(self):
        f = open("motion.txt", "r")
        lines = f.readlines()

        lines[self.lineNumber] = lines[self.lineNumber].strip("\n\r")
        # print("line is "+ line)
        self.pos = []
        if lines[self.lineNumber] == "addpoint":

            self.lastCommand = "addpoint"

        elif lines[self.lineNumber] == "transpoint":

            self.lastCommand = "transpoint"

        else:
            data = re.findall(r"[0-9]+", lines[self.lineNumber])
            # print(str(data))
            if len(data) != 0:
                # line = line.strip("[")  # or some other preprocessing
                self.pos.append([int(i) for i in data])  # storing everything in memory!

                self.ppp = []

                for num in self.pos:
                    i = 0
                    while i < len(num) - 3:
                        self.ppp.append([num[i], num[i + 1], num[i + 2]])
                        i = i + 3
            if self.lastCommand == "addpoint":
                self.posToPlot = np.asarray(self.ppp)
                self.setPoints(self.posToPlot)
            elif self.lastCommand == "transpoint":
                self.posToPlot = np.asarray(self.ppp)
                self.translatePoints(self.posToPlot)

        self.lineNumber = self.lineNumber + 1

        if self.lineNumber >= len(lines):
            self.deletePoints()
            self.timer.stop()
            self.lineNumber = 0
            self.consoleOut.outputText("Playing back Ended")


    def playbackMotion(self):
        #Play back needs to be in a separate thread, QT does threads in Timer

        self.consoleOut.outputText("Playing back motion")
        self.timer.start(self.playbackSpeed)
