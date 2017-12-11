###############################################################################
#Name:
#   ProjectViewer.py
#Author:
#   USB-Port
#What is this Class for:
#   This class handles all things related to the left side of the application, The Project Viewer. This class was implemented
#   So that the user can open and manage several different motion recordings at one time. Once the files are recorded,
#   The user will be able to play back this motion recorcing in OpenGL. (Not in OpenCV becuase we are not recording the
#   6 videos, but We could record the videos if we should). So this class will ack like any other Project viewer you have
#   used in any IDE.
#########################################################################
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class ProjectViewer(QtGui.QWidget):

    def __init__(self, QWidget):
        super(ProjectViewer, self).__init__()

        self.dockWidgetProjectViewer = QtGui.QDockWidget(QWidget)
        self.dockWidgetProjectViewer.setMinimumSize(QtCore.QSize(89, 111))
        self.dockWidgetProjectViewer.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetProjectViewer.setObjectName(_fromUtf8("dockWidgetProjectViewer"))

        self.projectViewerDocker = QtGui.QWidget()
        self.projectViewerDocker.setObjectName(_fromUtf8("projectViewerDocker"))
        self.gridLayout = QtGui.QGridLayout(self.projectViewerDocker)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.pathRoot = QtCore.QDir.currentPath()

        self.model = QtGui.QFileSystemModel(self)
        self.model.setRootPath(self.pathRoot)


        self.indexRoot = self.model.index(self.model.rootPath())

        #Fun Fact: PyQt have a QtreeView and a QTreeModel. At first glance, the model sounds like the one you want
        #but I ended up wasting like 5 hours using the QTreeModel and it did not work. QTreeView is the one you want.
        self.treeView = QtGui.QTreeView(QWidget)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.clicked.connect(self.on_treeView_clicked)
        self.treeView.doubleClicked.connect(self.on_treeView_double_clicked)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)

        self.gridLayout.addWidget(self.get_widget(), 0, 0, 1, 1)
        self.dockWidgetProjectViewer.setWidget(self.projectViewerDocker)

        QWidget.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetProjectViewer)

    #I'm not sure what these QTCore.pyqtSlots do, but I think it does something with events
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def open_project_directory(self):
        self.directory  = QtGui.QFileDialog.getExistingDirectory(self, 'Select a Folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        print(str(self.directory))
        print(str(self.pathRoot))
        print(str(self.indexRoot))
        self.treeView.setRootIndex(self.model.index(self.directory))


    #this is a overloaded virtual method. This expands the tree
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        #fileName = self.model.fileName(indexItem)
        #filePath = self.model.filePath(indexItem)

    #This is how you open a file
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_double_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        try:
            fileToOpen = open(fileName, 'r')
            for line in fileToOpen:
                print(line)
            fileToOpen.close()
        except:
            print("could not open the file")

    #this just re opens the project viewer if you close it
    def open_docker(self):
        self.dockWidgetProjectViewer.setVisible(True)

    #This returns the tree Open, I forgot what I was doing with this, could maybe remove
    def get_widget(self):
        return self.treeView
