###############################################################################
#Name:
#   ConsoleOutput.py

#What is this Class for:
#   This class handles the console output at the bottom of the application. This is used to notify the user what the
#   application is doing. The ideal here is the make the class output text just like terminal to keep the user informed.
#
#What Can I do here:
#   Output texts to the console window, change the color and size of the text, use custom fonts, and ummm. output text
#
#
#What needs to be done in this class:
#   -The output Text methods NEEDS to be a static method. I'm not sure how python handles static methods but this really
#   needs to be static. AKA, "Class method". This is not a high priority but will make the application a lot better.
#   You can make it static with "@staticmethod" but needs to be tested.
#   -Improve the output text to support different colors and different sizes or even different fonts
#   -Give the Console Output class some tabs, there can be tabs for updates, a tab for FPS, tabe for when tracking gets lost
#   You know, like a output, a debug, and a error tab or something. Not needed but feature creeping, but that static one
#   that one is a must.
#
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