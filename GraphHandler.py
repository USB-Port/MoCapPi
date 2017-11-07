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

        #self.q = gl.GLScatterPlotItem(pos=pos, size=size, color=color)
        #self.addItem(self.q)



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

    def translatePoints(self, Point):

        #print(str(Point))

        #for item in self.items:
        #    if isinstance(item, gl.GLScatterPlotItem):
        #        item.setData(pos=Point)

        #if(self.ppt is not None):
        #    self.ppt.setData(pos=Point)
        print(str(self.items))
        for item in self.items:
            if isinstance(item, gl.GLScatterPlotItem):
                item.setData(pos=Point)


        #for pts in self.pts:
        #    pos = np.empty((1, 3))
        #    pos[0] = (Point[self.i].getX(), Point[self.i].getY(), Point[self.i].getZ())
        #    #pts.setData(pos=pos[0])
        #    self.i = self.i + 1

        #for point in Point:
            #print("x is " + str(point.getX()) + " y is " + str(point.getY()))


        #self.ii = 0
        #for self.ii in range(0, len(Point)):
        #    pos = np.empty((1, 3))
        #    pos[0] = (Point[self.ii].getX(), Point[self.ii].getY(), Point[self.ii].getZ())
        #    self.pts[self.ii].setData(pos=pos[0])



        #for pts, point in zip(self.pts, Point):
        #    pos = np.empty((1, 3))
        #    pos[0] = (point.getX(), point.getY(), point.getZ())
        #    #point.printPosition()
        #    pts.setData(pos=pos[0])



        '''
        i = 0
        pos = np.empty((53, 3))
        if len(Point) > 0:
            #print("list " + str(self.items))
            #print("count of item " + str(len(self.items)))
            for item in self.items:
                if isinstance(item, gl.GLScatterPlotItem):
                    #print("moving")
                    #Point[i].printPosition()
                    #print("i " + str(i))
                    pos[i] = (Point[i].getX(), Point[i].getY(), Point[i].getZ())
                    i = i + 1

                    item.setData(pos=pos)


                    # print("lost point")
                else:
                    pass
                    #print("NOT PLOT")

        '''

    def setPoints(self, Point):
        size = np.empty((len(Point)))
        color = np.empty((len(Point), 4))

        for i in range(0, len(Point)):
            size[i] = 10.0
            color[i] = (1.0, 0.0, 0.0, 0.5)
        print(str(size))
        print(str(color))

        self.ppt = gl.GLScatterPlotItem(pos=Point, size=size, color=color, pxMode=False)
        self.addItem(self.ppt)
        #####################################
        '''
        self.pts = []
        i=0
        for item in self.items:
            if isinstance(item, gl.GLScatterPlotItem):
                self.removeItem(item)

        pos = np.empty((1, 3))
        size = np.empty((1))
        color = np.empty((1, 4))

        for point in Point:
            pos = np.empty((1, 3))
            size = np.empty((1))
            color = np.empty((1, 4))


            pos[0] = (point.getX(), point.getY(), point.getZ())
            point.printPosition()
            size[0] = 5.0
            color[0] = (1.0, 0.0, 0.0, 0.5)
            self.pts.append(gl.GLScatterPlotItem(pos=pos[0], size=size[0], color=color[0]))

            #self.addItem(self.pts[i])

        for pts in self.pts:
            self.addItem(pts)
        '''
        ######################################################

        #pptt = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)
        #self.addItem(pptt)
        #self.updateGL()


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

        '''
            #self.hide()
            if len(Point) > 0:
                i=0
                for po in Point:
                    self.pos[i] = (po.getX()+10000, po.getY(), po.getZ())
                    self.size[i] = 10.0
                    self.color[i] = (1.0, 0.0, 0.0, 0.5)
                    i = i +1
                    #po.printPosition()


                self.points = gl.GLScatterPlotItem(pos=self.pos, size=self.size, color=self.color, pxMode=False)
                self.addItem(self.points)
                self.SHIT =False

            for (po, i) in (self.points, Point):
                 po.translate(i.getX()-10000, i.getY(), i.getZ())

        for (po, i) in (self.points, Point):
            po.translate(i.getX(), i.getY(), i.getZ())

        #sleep(0.1)
        #self.setVisible(True)
        #else:
        #   self.SHIT = self.SHIT + 1
        #    if self.SHIT == 100000:
        #        self.SHIT = 0

        #    if len(Point) > 0:
        #        for (po,i) in (self.points,Point):
        #            po.translate(i.getX(), i.getY(), i.getZ())

        '''