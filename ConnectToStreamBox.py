###############################################################################
#Name:
#   ConnectToStreamBox.py

#What is this Class for:
#   This is a simple class that just pops up box. the User can type in an IP address in this form, "tcp://192.168.2.9:9092"
#   The that IP address gets passed to OpenCV. BUT, keep in mind that OpenCVHandler NEEDS a widget to get passed in as well.
#   To Get the stream to play, we must get a widget from Capture Area, that is why this class takes in a Capture Area Object
#
#What Can I do here:
#   Change UI. Use this code as an example for "How to open a Stream"
#
#
#What needs to be done in this class:
#   Make it robust, sometimes it still crashes.
#   It only works if the user is not on the same tab as the tab that gets returned from the Capture Area "get Widget" method.
#
#
################################################################################


from PyQt4 import QtCore, QtGui
from CVHandler import *
from CaptureArea import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class ConnectToStreamBox(QtGui.QWidget):
    #This class takes a Capture Area Object so that it can pass a Widget to OpenCVHandler
    def __init__(self, CaptureArea):
        QtGui.QWidget.__init__(self)

        #A lot of this code is auto Generated
        self.captureArea = CaptureArea
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.connectStreamLabel = QtGui.QLabel(self)
        self.connectStreamLabel.setObjectName(_fromUtf8("connectStreamLabel"))
        self.gridLayout.addWidget(self.connectStreamLabel, 0, 0, 1, 2)
        self.StreamConnectInput = QtGui.QLineEdit(self)
        self.StreamConnectInput.setObjectName(_fromUtf8("StreamConnectInput"))
        self.gridLayout.addWidget(self.StreamConnectInput, 1, 0, 1, 1)
        self.connectButton = QtGui.QPushButton(self)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.gridLayout.addWidget(self.connectButton, 1, 1, 1, 1)
        self.cancelButton = QtGui.QPushButton(self)
        self.cancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 1, 2, 1, 1)

        #Recall this is how you link a button to a function.
        #Fun Fact, The python Version of QT Designer 4 Can Not link method. The C++ version Can
        #Therefore, You will always need to link you button in code, like below.
        self.connectButton.clicked.connect(self.connectToStream)
        self.cancelButton.clicked.connect(self.cancelBox)


        #QtCore.QMetaObject.connectSlotsByName(self)

        self.connectStreamLabel.setText(_translate("Form", "Connect to a Stream", None))
        self.connectButton.setText(_translate("Form", "Connect", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))

        self.show()

    #This method gets called when the user clicks the "Connect" Button
    def connectToStream(self):
        #This is how you get the String from the Input Text Box
        self.ipAddress = self.StreamConnectInput.text()

        #Checks to see if there is a stream. This should be checked with Regular Expression
        if(self.ipAddress):
            #return self.ipAddress
            #print(self.ipAddress)

            #print(str(self.ipAddress))
            tab = self.captureArea.getWidget()
            #self.captureArea.newTab()
            self.stream = CVHandler(tab, 0)
            self.stream.start_clicked()
            #self.deleteLater()
            #text = "http://" + str(self.ipAddress) +":8081/?action=stream?dummy=param.mjpg"
            #self.stream = CVHandler(self.tab, text)
            #self.stream.start_clicked()
        else:
            #if the user
            print("need a Ip to connect")

    #This method gets called when user clicks the "cancel" button
    def cancelBox(self):
        self.deleteLater()


