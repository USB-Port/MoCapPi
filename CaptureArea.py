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

        self.tabs = [0]
        self.gridLayouts = [0]
        self.widgets = [0]

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

