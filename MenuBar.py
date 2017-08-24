import sys
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

class MenuBar(QtGui.QMainWindow):

  def __init__(self, QMainWindow):
    super(MenuBar, self).__init__()
    self.menuBar = QtGui.QMenuBar(self)
    self.menuBar.setNativeMenuBar(False)
    self.menuBar.setGeometry(QtCore.QRect(0, 0, 1055, 25))
    self.menuBar.setObjectName(_fromUtf8("menubar"))

    self.menuFile = QtGui.QMenu(self.menuBar)
    self.menuFile.setObjectName(_fromUtf8("menuFile"))

    self.menuEdit = QtGui.QMenu(self.menuBar)
    self.menuEdit.setObjectName(_fromUtf8("menuEdit"))

    self.menuView = QtGui.QMenu(self.menuBar)
    self.menuView.setObjectName(_fromUtf8("menuView"))

    self.menuTools = QtGui.QMenu(self.menuBar)
    self.menuTools.setObjectName(_fromUtf8("menuTools"))

    self.menuHelp = QtGui.QMenu(self.menuBar)
    self.menuHelp.setObjectName(_fromUtf8("menuHelp"))


    self.actionOpen = QtGui.QAction(self)
    self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
    self.actionOpen.setShortcut("Ctrl+O")
    self.actionOpen.setStatusTip("Open a file")
    self.actionOpen.triggered.connect(self.open_file)

    self.actionSave = QtGui.QAction(self)
    self.actionSave.setObjectName(_fromUtf8("actionSave"))

    self.actionSave_As = QtGui.QAction(self)
    self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))

    self.actionQuit = QtGui.QAction(self)
    self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
    self.actionQuit.setShortcut("Ctrl+Q")
    self.actionQuit.setStatusTip("Quit the application")
    self.actionQuit.triggered.connect(self.close_application)

    self.menuFile.addAction(self.actionOpen)
    self.menuFile.addAction(self.actionSave)
    self.menuFile.addAction(self.actionSave_As)
    self.menuFile.addAction(self.actionQuit)
    self.menuBar.addAction(self.menuFile.menuAction())
    self.menuBar.addAction(self.menuEdit.menuAction())
    self.menuBar.addAction(self.menuView.menuAction())
    self.menuBar.addAction(self.menuTools.menuAction())
    self.menuBar.addAction(self.menuHelp.menuAction())

    self.menuFile.setTitle(_translate("MainWindow", "File", None))
    self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
    self.menuView.setTitle(_translate("MainWindow", "View", None))
    self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
    self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
    self.actionOpen.setText(_translate("MainWindow", "Open", None))
    self.actionSave.setText(_translate("MainWindow", "Save", None))
    self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
    self.actionQuit.setText(_translate("MainWindow", "Quit", None))

  def get_widget(self):
    return self.menuBar

  def open_file(self):
      self.dlg = QtGui.QFileDialog()
      self.dlg.setFileMode(QtGui.QFileDialog.AnyFile)
      self.dlg.setFilter("Text files (*.txt)")
      self.fileName = QtCore.QString()

      self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/')

      print(str(self.fileName))

  def close_application(self):
    choice = QtGui.QMessageBox.question(self,'Extract!',
    "Quit the Application?",QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)

    if choice == QtGui.QMessageBox.Yes:
      sys.exit()
    else:
      pass