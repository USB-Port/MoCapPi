from PyQt4 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
import numpy as np
import pyqtgraph.opengl as gl
from numpy import *

from time import sleep

from OpenGL import GL
from Point import *
from time import sleep
import types
import re

#pg.GraphicsLayoutWidget
class GraphHandler(gl.GLViewWidget):
    #This class takes a Capture Area Object so that it can pass a Widget to OpenCVHandler
    def __init__(self, GraphHandler):
        gl.GLViewWidget.__init__(self)
        #pg.mkQApp()

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
            size[i] = 10.0
            color[i] = (1.0, 0.0, 0.0, 0.5)

        self.ppt = gl.GLScatterPlotItem(pos=PosArray, size=size, color=color, pxMode=False)
        self.addItem(self.ppt)


    def addPoints(self, Point):


        for item in self.items:
            if isinstance(item, gl.GLScatterPlotItem):
                self.removeItem(item)

        if len(Point) > 0:
            limit = 0
            pts = []
            i = 0
            for point in Point:
                pos = np.empty((53, 3))
                size = np.empty((53))
                color = np.empty((53, 4))
                pos[0] = (point.getX(), point.getY(), point.getZ())
                size[0] = 10.0
                color[0] = (1.0, 0.0, 0.0, 0.5)
                pts.append(gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False))
                self.addItem(pts[i])
                limit = limit +1
                i = i+1

    def playbackMotion(self, fileName = "motion.txt"):


        #file = open(fileName, "r")
        lastCommand = None
        with open(fileName) as file:
            for line in file:
                self.pos = []
                if line == "addpoint":
                    lastCommand = "addpoint"

                elif line == "transpoint":
                    lastCommand = "transpoint"

                else:
                    data = re.findall(r"[0-9]+", line)
                    print(str(data))
                    if len(data) != 0:
                    #line = line.strip("[")  # or some other preprocessing
                        self.pos.append([int(i) for i in data])  # storing everything in memory!

                    #innerList = line.split(',')
                    #del innerList[-1]
                    #print("innerList is " +str(innerList))
                    #self.pos.append(innerList)
                    print("pos is "+ str(self.pos))
                   # print("pos sssss "+ str(self.pos[0][0]))
