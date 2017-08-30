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
        self.outputConsoleText = QtGui.QTextEdit(self.dockWidgetContents_9)
        self.outputConsoleText.setReadOnly(True)
        self.outputConsoleText.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.scrollBar = self.outputConsoleText.verticalScrollBar()
        self.font = self.outputConsoleText.font()
        self.font.setFamily("Courier")
        self.font.setPointSize(10)
        self.outputConsoleText.setObjectName(_fromUtf8("outputConsoleText"))
        self.horizontalLayout.addWidget(self.outputConsoleText)
        self.dockWidgetConsoleOutput.setWidget(self.dockWidgetContents_9)

        QWidget.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetConsoleOutput)

        x = 1
        for x in range(1, 100):
            self.outputText("test")


    def outputText(self, text):
        self.outputConsoleText.moveCursor(QtGui.QTextCursor.End)
        self.outputConsoleText.setCurrentFont(self.font)
        self.outputConsoleText.setTextColor(QtGui.QColor(255,0,0))

        self.outputConsoleText.insertPlainText(text)
        self.outputConsoleText.insertPlainText("\n")

        self.scrollBar.setValue(self.scrollBar.maximum())

    def open_docker(self):
        self.dockWidgetConsoleOutput.setVisible(True)