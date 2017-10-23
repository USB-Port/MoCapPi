###############################################################################
#Name:
#   OpenGLHandler.py

#What is this Class for:
#   This class is to handle all the point data and recreate the actor in 3D space. The point data will be record so that
#   it can be playbacked and exported as Motion files.
#
#What Can I do here:
#   Not much, still trying to wrap my head around it
#
#
#What needs to be done in this class:
#   Get the OpenGL working accurately. There is a ton of problems with this, but I did get the point to update based on
#   the data I got from OPenCV. I'm still working on this Garbo. I can't really comment this code as I'm not sure what it
#   all does, a lot of it is going to change once I start to understand it.
#
################################################################################

import sys
import math
import numpy as np
from PyQt4 import QtCore, QtGui, QtOpenGL
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *

try:
    from OpenGL import GL
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL hellogl",
            "PyOpenGL must be installed")
    sys.exit(1)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class OpenGLHandler(QtOpenGL.QGLWidget):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)
    xRotationChanged = QtCore.pyqtSignal(int)
    yRotationChanged = QtCore.pyqtSignal(int)
    zRotationChanged = QtCore.pyqtSignal(int)


    def __init__(self, windowWidth, windowHeight):
        super(OpenGLHandler, self).__init__()

        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        #self.object = 0
        self.singlePoint = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.pointX = 0.01
        self.pointY = 0.01

        self.lastPos = QtCore.QPoint()

        self.trolltechGreen = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1)

    def setPos(self, x, y):

        #self.pointX = (x/680) - 1
        #self.pointY = (y/440) -1

        print(str(self.pointY))


    def refresh(self):
        #print("het")
        self.updateGL()

    def minimumSizeHint(self):
        return QtCore.QSize(self.windowWidth, self.windowHeight)

    def sizeHint(self):
        return QtCore.QSize(self.windowWidth, self.windowHeight)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.updateGL()

    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.dark())
        #self.object = self.makeObject()
        #gluPerspective(90, (self.windowWidth / self.windowHeight), 0.1, 150.0)
        #gluPerspective(60, (self.windowWidth / self.windowHeight), 1.0, 150.0)
        self.singlePoint = self.makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        #glutInit(sys.argv)




    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(self.y1, self.y1, -10.0)
        #GL.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        #GL.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        #GL.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        #GL.glCallList(self.object)

        GL.glCallList(self.singlePoint)

    def resizeGL(self, width, height):

        # GL.glViewport(int((width - side) / 2), int((height - side) / 2), side, side)
        #
        # GL.glMatrixMode(GL.GL_PROJECTION)
        # GL.glLoadIdentity()
        # GL.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        # GL.glMatrixMode(GL.GL_MODELVIEW)
        #GL.glViewport(0,0,self.windowWidth,self.windowHeight)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        #GL.glOrtho(0,680,0,480,0,1)
        GL.glOrtho(0, self.windowWidth, self.windowHeight, 0, -1.0, 15.0)
        #GL.glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
        #gluPerspective(60, (self.windowWidth / self.windowHeight), 1.0, 150.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        #GL.glLoadIdentity()



    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def keyPressEvent(self, event):
        super(OpenGLHandler, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def onKeyEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.y1 = self.y1 + 1.0
        elif event.key() == QtCore.Qt.Key_S:
            self.y1 = self.y1 - 1.0
        elif event.key() == QtCore.Qt.Key_D:
            self.x1 = self.x1 + 1.0
        elif event.key() == QtCore.Qt.Key_A:
            self.x1 = self.x1 - 1.0
        elif event.key() == QtCore.Qt.Key_Enter:
            print("YO YO")
        elif event.key() == QtCore.Qt.Key_Return:
            print("YO NO")

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.y1 = self.y1 + 1.0
            print(str(self.y1))
            self.updateGL()
            #self.setXRotation(self.xRot + 8 * dy)
            #self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & QtCore.Qt.RightButton:
            self.y1 = self.y1 - 1.0
            print(str(self.y1))
            self.updateGL()


        elif QtCore.QEvent.KeyPress == QtCore.Qt.Key_0:
            self.pointX = self.pointX - 0.1
            print(str(self.pointX))

        elif event.buttons() & QtCore.Qt.MiddleButton:
            self.pointX = self.pointX + 0.1
            print(str(self.pointX))
            #self.setXRotation(self.xRot + 8 * dy)
            #self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = event.pos()

    def makeObject(self):
        genList = GL.glGenLists(1)
        GL.glNewList(genList, GL.GL_COMPILE)

        #GL.glBegin(GL.GL_QUADS)




        self.x1 = +0.06
        self.y1 = -0.14
        x2 = +0.14
        y2 = -0.06
        x3 = +0.08
        y3 = +0.00
        x4 = +0.30
        y4 = +0.22
        '''
        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)
        self.quad(x3, y3, x4, y4, y4, x4, y3, x3)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)
        self.extrude(x3, y3, x4, y4)
        self.extrude(x4, y4, y4, x4)
        self.extrude(y4, x4, y3, x3)

        NumSectors = 200

        for i in range(NumSectors):
            angle1 = (i * 2 * math.pi) / NumSectors
            x5 = 0.30 * math.sin(angle1)
            y5 = 0.30 * math.cos(angle1)
            x6 = 0.20 * math.sin(angle1)
            y6 = 0.20 * math.cos(angle1)

            angle2 = ((i + 1) * 2 * math.pi) / NumSectors
            x7 = 0.20 * math.sin(angle2)
            y7 = 0.20 * math.cos(angle2)
            x8 = 0.30 * math.sin(angle2)
            y8 = 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)
        '''

        GL.glBegin(GL.GL_POINTS)
        self.qglColor(self.trolltechGreen)
        #for i in range(0, 10):
        #print("x1 " + str(self.x1))

        #print("y1 " + str(self.y1))
        GL.glVertex2d(self.y1,self.y1)

        GL.glEnd()
        GL.glEndList()
        GL.glPointSize(8.0)
        return genList

    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.qglColor(self.trolltechGreen)

        GL.glVertex3d(x1, y1, -0.05)
        GL.glVertex3d(x2, y2, -0.05)
        GL.glVertex3d(x3, y3, -0.05)
        GL.glVertex3d(x4, y4, -0.05)

        GL.glVertex3d(x4, y4, +0.05)
        GL.glVertex3d(x3, y3, +0.05)
        GL.glVertex3d(x2, y2, +0.05)
        GL.glVertex3d(x1, y1, +0.05)

    def extrude(self, x1, y1, x2, y2):
        self.qglColor(self.trolltechGreen.dark(250 + int(100 * x1)))

        GL.glVertex3d(x1, y1, +0.05)
        GL.glVertex3d(x2, y2, +0.05)
        GL.glVertex3d(x2, y2, -0.05)
        GL.glVertex3d(x1, y1, -0.05)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
