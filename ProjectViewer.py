import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class ProjectViewer(QtGui.QWidget):

    def __init__(self, QWidget):
        super(ProjectViewer, self).__init__()

        self.pathRoot = QtCore.QDir.currentPath()

        self.model = QtGui.QFileSystemModel(self)
        self.model.setRootPath(self.pathRoot)


        self.indexRoot = self.model.index(self.model.rootPath())

        self.treeView = QtGui.QTreeView(QWidget)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.clicked.connect(self.on_treeView_clicked)
        self.treeView.doubleClicked.connect(self.on_treeView_double_clicked)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def open_project_directory(self):
        self.directory  = QtGui.QFileDialog.getExistingDirectory(self, 'Select a Folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        print(str(self.directory))
        print(str(self.pathRoot))
        print(str(self.indexRoot))
        self.treeView.setRootIndex(self.model.index(self.directory))
        #view.setRootIndex(model.index("C:\Myfolder")
        #self.model.setRootPath(self.directory)
        #self.indexRoot = self.model.index(self.model.rootPath()) 

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        #fileName = self.model.fileName(indexItem)
        #filePath = self.model.filePath(indexItem)

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



    def get_widget(self):
        return self.treeView
