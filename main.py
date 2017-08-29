# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mocappi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ProjectViewer import *


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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1016, 818)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetProjectViewer = QtGui.QDockWidget(MainWindow)
        self.dockWidgetProjectViewer.setMinimumSize(QtCore.QSize(89, 111))
        self.dockWidgetProjectViewer.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetProjectViewer.setObjectName(_fromUtf8("dockWidgetProjectViewer"))



        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.projectViewer = ProjectViewer(self.dockWidgetContents_2)

        self.gridLayout.addWidget(self.projectViewer.get_widget(), 0, 0, 1, 1)


        #self.treeView = QtGui.QTreeView(self.dockWidgetContents_2)
        #self.treeView.setObjectName(_fromUtf8("treeView"))

        #self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.dockWidgetProjectViewer.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetProjectViewer)
        self.dockWidgetControls = QtGui.QDockWidget(MainWindow)
        self.dockWidgetControls.setObjectName(_fromUtf8("dockWidgetControls"))
        self.dockWidgetContents_8 = QtGui.QWidget()
        self.dockWidgetContents_8.setObjectName(_fromUtf8("dockWidgetContents_8"))
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents_8)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.dockWidgetControls.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetControls)
        self.dockWidgetConsoleOutput = QtGui.QDockWidget(MainWindow)
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
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetConsoleOutput)

        MainWindow.setCentralWidget(self.centralwidget)

        self.init_menu_bar(MainWindow)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        '''
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1055, 538)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 491))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))


        self.projectViewer = ProjectViewer(self.gridLayoutWidget)

        self.gridLayout.addWidget(self.projectViewer.get_widget(), 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)


        self.init_menu_bar(MainWindow)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    '''

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mo Cap pie - Team Ep0ch", None))

    def init_menu_bar(self, MainWindow):
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1055, 25))
        self.menuBar.setObjectName(_fromUtf8("menubar"))

        #Initialze the Menu Items
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuProject = QtGui.QMenu(self.menuBar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))

        #Open a project file Action
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setStatusTip("Open a file")
        self.actionOpen.triggered.connect(lambda: self.open_file(MainWindow))

        #Save the Project Action
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip("Save the Project")
        #self.actionSave.connect(self.FUNCTION NAME)

        #Save As Action
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))

        #Open project Directory Action
        self.actionOpenProjectDirectory = QtGui.QAction(MainWindow)
        self.actionOpenProjectDirectory.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpenProjectDirectory.setShortcut("Ctrl+N")
        self.actionOpenProjectDirectory.setStatusTip("Open a Project Folder")
        self.actionOpenProjectDirectory.triggered.connect(self.open_project_directory)

        #Quit the program Action
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setStatusTip("Quit the application")
        self.actionQuit.triggered.connect(lambda: self.close_application(MainWindow))

        #Add Action to the "File" submenu
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionQuit)

        #Add Action to the "Project" submenu
        self.menuProject.addAction(self.actionOpenProjectDirectory)

        #Add Menu Items to the Menu Bar
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

       
        #Name the Menu Items
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuProject.setTitle(_translate("MainWindow", "Project", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionOpenProjectDirectory.setText(_translate("MainWindow", "Open Project Directory", None))

        MainWindow.setMenuBar(self.menuBar)

    def open_project_directory(self):
      self.projectViewer.open_project_directory()
      #self.gridLayout.update()

    def open_file(self, MainWindow):
        self.dlg = QtGui.QFileDialog(MainWindow)
        self.dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        self.dlg.setFilter("Text files (*.txt)")
        #self.fileName = QtCore.QString()

        self.fileName = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open File', '/')

        print(str(self.fileName))

    def close_application(self, MainWindow):
        choice = QtGui.QMessageBox.question(MainWindow,'Extract!', "Quit the Application?",QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

