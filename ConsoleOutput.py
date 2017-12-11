###############################################################################
#Name:
#   ConsoleOutput.py
#Author:
#   USB-Port
#What is this Class for:
#   This class handles the console output at the bottom of the application. This is used to notify the user what the
#   application is doing. The ideal here is the make the class output text just like terminal to keep the user informed.
################################################################################


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class ConsoleOutput(QtGui.QWidget):

    #A lot of this code in the constructor is self generated from the QT designer.
    #The QT designer is used to get the layout right so I don't have to hard code it myself.
    #Example, you see line 41. QSize(89,40), Those numbers were done by Designer. I wouldn't be able to guess that.
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

    #Call this method, pass it a string and it out puts it to the console box at the end.
    #This method needs to be a static method
    def outputText(self, text):
        self.outputConsoleText.moveCursor(QtGui.QTextCursor.End)
        self.outputConsoleText.setCurrentFont(self.font)
        self.outputConsoleText.setTextColor(QtGui.QColor(255,0,0))

        self.outputConsoleText.insertPlainText(text)
        self.outputConsoleText.insertPlainText("\n")

        self.scrollBar.setValue(self.scrollBar.maximum())

    #if the docker window is closed, open it back up.
    def open_docker(self):
        self.dockWidgetConsoleOutput.setVisible(True)