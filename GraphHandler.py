from PyQt4 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
import numpy as np
import pyqtgraph.opengl as gl

#pg.GraphicsLayoutWidget
class GraphHandler(gl.GLViewWidget):
    #This class takes a Capture Area Object so that it can pass a Widget to OpenCVHandler
    def __init__(self, GraphHandler):
        gl.GLViewWidget.__init__(self)
        #pg.mkQApp()

        ## make a widget for displaying 3D objects


        self.opts['distance'] = 50
        #self.view.show()

        ## create three grids, add each to the view
        self.xgrid = gl.GLGridItem()
        self.ygrid = gl.GLGridItem()
        self.zgrid = gl.GLGridItem()

        self.addItem(self.xgrid)
        self.addItem(self.ygrid)
        self.addItem(self.zgrid)

        # pos = np.empty((53, 3))
        # size = np.empty((53))
        # color = np.empty((53, 4))
        # pos[0] = (1,0,0); size[0] = 0.1;   color[0] = (1.0, 0.0, 0.0, 0.5)
        # pos[1] = (0,1,0); size[1] = 0.1;   color[1] = (0.0, 0.0, 1.0, 0.5)
        # pos[2] = (0,0,1); size[2] = 0.1; color[2] = (0.0, 1.0, 0.0, 0.5)

        # point = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)
        # point.translate(5,5,0)
        # point.pos(1,1,1)
        # point.size(10.0)
        # point.color(.5,.5,.5,.5)

        # view.addItem(point)

        ## rotate x and y grids to face the correct direction
        self.zgrid.rotate(90, 0, 1, 0)
        self.ygrid.rotate(90, 1, 0, 0)
        self.ygrid.translate(0, -10, 10)
        self.zgrid.translate(-10, 0, 10)
        ## scale each grid differently
        self.xgrid.scale(1, 1, 1)
        self.ygrid.scale(1, 1, 1)
        self.zgrid.scale(1, 1, 1)
        #self.update()