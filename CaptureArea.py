from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



class CaptureArea(QtGui.QWidget):

    def __init__(self, QWidget):
        super(CaptureArea, self).__init__()
        self.gridLayout_2 = QtGui.QGridLayout(QWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.captureArea = QtGui.QTabWidget(QWidget)
        self.captureArea.setObjectName(_fromUtf8("captureArea"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.captureArea.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.widget_2 = QtGui.QWidget(self.tab_2)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 1)
        self.captureArea.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.captureArea, 0, 0, 1, 1)