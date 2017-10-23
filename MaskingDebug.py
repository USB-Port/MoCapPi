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

class MaskingDebug(QtGui.QWidget):
    #This class takes a Capture Area Object so that it can pass a Widget to OpenCVHandler
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.setObjectName(_fromUtf8("Form"))
        self.resize(568, 184)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 2, 1, 2, 1)
        self.textEdit_3 = QtGui.QTextEdit(self)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout.addWidget(self.textEdit_3, 4, 1, 2, 1)
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(self)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.gridLayout.addWidget(self.horizontalSlider_2, 3, 0, 1, 1)
        self.horizontalSlider_3 = QtGui.QSlider(self)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.gridLayout.addWidget(self.horizontalSlider_3, 5, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Lower Bound", None))
        self.label_2.setText(_translate("Form", "Upper Bound", None))
        self.pushButton_2.setText(_translate("Form", "Quit", None))
        self.pushButton.setText(_translate("Form", "Set", None))
        self.label_3.setText(_translate("Form", "Radius", None))
