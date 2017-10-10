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

    def __init__(self, CaptureArea):
        QtGui.QWidget.__init__(self)
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


        self.connectButton.clicked.connect(self.connectToStream)
        self.cancelButton.clicked.connect(self.cancelBox)


        #QtCore.QMetaObject.connectSlotsByName(self)

        self.connectStreamLabel.setText(_translate("Form", "Connect to a Stream", None))
        self.connectButton.setText(_translate("Form", "Connect", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))

        self.show()

    def connectToStream(self):
        self.ipAddress = self.StreamConnectInput.text()
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

    def cancelBox(self):
        self.deleteLater()


