###############################################################################
#Name:
#   SetUpWizard.py
#Author:
#   USB-Port
#What is this Class for:
#   This class is planned to handle the setting up the cameras. This is going to be a wizard that walks the user through
#   the set up precess of the cameras. This include, connecting to each camera, setting up distortion metrixes, inputing
#   the distance between each camera, inputting the angle, picking a project folder, calibrating the cameras and saving
#   The setting to a file that is auto loaded when the program opens up.
################################################################################



from PyQt4 import QtCore, QtGui

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

class SetUpWizard(QtGui.QWidget):


    def __init__(self):
        QtGui.QWidget.__init__(self)

        #Below is the self generated code from the Designer.

        print("test")
        #self.setGeometry(QtCore.QRect(800, 400, 500, 500))
        #self.setWindowTitle("When you ask someone to do work")
        #Form = QtGui.QWidget()
        #Form.resize(776, 559)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("./imgs/pic.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.cancelButton = QtGui.QPushButton(self)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 2, 1, 1, 1)
        self.nextButton = QtGui.QPushButton(self)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))

        self.nextButton.clicked.connect(self.connectCamera)
        self.cancelButton.clicked.connect(self.cancelBox)

        self.gridLayout.addWidget(self.nextButton, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3)

        self.setWindowTitle(_translate("Form", "When you ask someone to do work", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))
        self.nextButton.setText(_translate("Form", "Next", None))
        self.label_2.setText(_translate("Form", "Welcome, I am the Set up wizard, I will walk you through setting up the cameras.", None))
        self.label_3.setText(_translate("Form", "So You Want to Set up the Cameras?", None))

        #self.myPic  = QtGui.QPixmap(_fromUtf8("./imgs/pic.jpg"))

        #hbox = QtGui.QHBoxLayout(self)
        #lbl = QtGui.QLabel(self)
        #lbl.setPixmap(self.myPic)

        #hbox.addWidget(lbl)
        #self.setLayout(hbox)

        self.show()

    #This method is self generated code except that I need to delete stuff. I think it is the delete Later methods.
    #There are still some bugs, think of this method as Frame 2. After the user clicks the first next button
    def connectCamera(self):

        #self.deleteLater()
        #self.gridLayout.deleteLater()


        self.label.deleteLater()
        self.label_2.deleteLater()
        self.label_3.deleteLater()
        self.cancelButton.deleteLater()
        self.nextButton.deleteLater()


        #self.gridLayout2 = QtGui.QGridLayout(self)
        #self.gridLayout2.setObjectName(_fromUtf8("gridLayout2"))

        self.widget = QtGui.QWidget(self)
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QtCore.QSize(0, 500))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()

        self.pushButton.setText(_translate("Form", "Cancel", None))

        self.pushButton_2.setText(_translate("Form", "Connect", None))

        self.pushButton_3.setText(_translate("Form", "Next", None))

        self.label_2.setText(
            _translate("Form", "Welcome to the Set up wizard, I will walk you through setting up the cameras.", None))
        self.label_3.setText(_translate("Form", "So You Want to Set up the Cameras?", None))

        self.show()

    #Not sure why this is here, might not be needed TBH
    def paintEvent(self, e):
        dc = QtGui.QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)

    #If the user clicks cancel, Delete the whole Widget
    def cancelBox(self):
        self.deleteLater()