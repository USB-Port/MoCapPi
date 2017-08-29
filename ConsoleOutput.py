from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class ConsoleOutput(QtGui.QWidget):

    def __init__(self, QWidget):
        super(ConsoleOutput, self).__init__()
        self.dockWidgetConsoleOutput = QtGui.QDockWidget(QWidget)
        self.dockWidgetConsoleOutput.setMinimumSize(QtCore.QSize(89, 40))
        self.dockWidgetConsoleOutput.setObjectName(_fromUtf8("dockWidgetConsoleOutput"))
        self.dockWidgetContents_9 = QtGui.QWidget()
        self.dockWidgetContents_9.setObjectName(_fromUtf8("dockWidgetContents_9"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_9)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.outputConsoleText = QtGui.QTextBrowser(self.dockWidgetContents_9)
        self.outputConsoleText.setObjectName(_fromUtf8("outputConsoleText"))
        self.horizontalLayout.addWidget(self.outputConsoleText)
        self.dockWidgetConsoleOutput.setWidget(self.dockWidgetContents_9)
        QWidget.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetConsoleOutput)