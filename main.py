###############################################################################
#Name:
#   main.py

#What is this Class for:
#   This file is for the over all application of the program.
#   This class stores the UI layout of the different parts of the app, This also stores the
#   QMainWindow class which handles OS events. The class also manages the tool bar and the menu bar.
#   Most of the classes are instatiated in this class. This is the base of the app.
#
#What Can I do here:
#   Add Menu Items, Add Tool Bar Items, Backend Design of classes, App Event handling,
#   Modify Over all UI design, change Dockable widgets, change Window Title, Create a software DRM activation key.
#   make a trial version of the software, anything that deals with the whole application
#
#What needs to be done in this class:
#   -Improved Class architecture - Fixing bad design starts here with the instatiation of the classes
#   -Improve UI
#   -anything that you want to see in the over all application window.
#   Yea, not much as most bugs are in the other classes
#
################################################################################





import sys
from PyQt4 import QtCore, QtGui
from ProjectViewer import *
from CaptureArea import *
from ConsoleOutput import *
from SetUpWizard import *
from ConnectToStreamBox import *

#This two try except is used to support multiple languages. still need it to support English
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


#This is the UI for the main Window. this is the class that links everything together. This class is long because
#it links everything together. This class is mainly made up of the over all UI design and the Tool Bar
#A lot of this code is self generated from QT designer, Don't really have to mess with a lot of it.
class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, MainWindow, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1016, 818)

        #Central Widget is the main area to put Widgets on the program
        #Itis not a container.
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.init_tool_bar(MainWindow)

        #initialize the Capture Area
        self.captureArea = CaptureArea(self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        #Initialize the ProjectViewer
        self.projectViewer = ProjectViewer(MainWindow)


        #This may be the buttons but might remove in an update
        self.dockWidgetControls = QtGui.QDockWidget(MainWindow)
        self.dockWidgetControls.setObjectName(_fromUtf8("dockWidgetControls"))
        self.dockWidgetContents_8 = QtGui.QWidget()
        self.dockWidgetContents_8.setObjectName(_fromUtf8("dockWidgetContents_8"))
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents_8)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.dockWidgetControls.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetControls)

        #initialize the Console Output
        self.consoleOutput = ConsoleOutput(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        #Set up the Menu Bar
        self.init_menu_bar(MainWindow)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #This is a virtual method that is used to set the text, this makes it easy to support multiple languages
    def retranslateUi(self, MainWindow):
        #This will be used to support multiple languages

        MainWindow.setWindowTitle(_translate("MainWindow", "Mo Cap pie - Team Ep0ch", None))
        MainWindow.setWindowIcon(QtGui.QIcon("./imgs/icon.ico"))
        #self.captureArea.setTabText(self.captureArea.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        #self.captureArea.setTabText(self.captureArea.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))

    #Method I wrote to set up the docakable tool bar
    def init_tool_bar(self, MainWindow):

        #This line assigns this veriable to a QAction. then set the ICON and text
        self.playMotionAction = QtGui.QAction(QtGui.QIcon("./imgs/PlayGreenButton.ico"), "Play Motion", MainWindow)
        #This is how you link a QAction to a function. The function here is Play_motion
        self.playMotionAction.triggered.connect(self.play_motion)

        #If you would like a new button, you can just copy these 2 lines like how I did for the next 3. This simpley makes
        #the veriable, once created, you have to add these "actions" to a menu or tool bar.

        self.pauseMotionAction = QtGui.QAction(QtGui.QIcon("./imgs/Pause.ico"), "Pause Motion Capture", MainWindow)
        self.pauseMotionAction.triggered.connect(self.pause_motion)

        self.stopMotionAction = QtGui.QAction(QtGui.QIcon("./imgs/StopRedButton.ico"), "Stop Motion Capture", MainWindow)
        self.stopMotionAction.triggered.connect(self.stop_motion)

        self.recordMotionAction = QtGui.QAction(QtGui.QIcon("./imgs/RecordButton.ico"), "Record New Motion Capture", MainWindow)
        self.recordMotionAction.triggered.connect(self.record_Motion)

        self.testMotionAction = QtGui.QAction(QtGui.QIcon("./imgs/RecordButton.ico"), "Record New Motion Capture",MainWindow)
        self.testMotionAction.triggered.connect(self.test_Motion)

        # Let me tell you all a story about a mouse named glory
        #Here I create a tool bar and add it to the MainWindow.
        self.toolBar = MainWindow.addToolBar("Test test")
        #Once the toolbar is made, you can add the actions, AKA buttons, to the tool bar like so.
        self.toolBar.addAction(self.playMotionAction)
        self.toolBar.addAction(self.pauseMotionAction)
        self.toolBar.addAction(self.stopMotionAction)
        self.toolBar.addAction(self.recordMotionAction)
        self.toolBar.addAction(self.testMotionAction)


    def test_Motion(self):
        self.captureArea.playBackMotion()

    #Yoy need to link a button action to a method, so this method is called when the user clicks, "record motion" button
    def record_Motion(self):
        #this line just prints the string to the output console in the program

        print(str(self.captureArea.isRunning()))
        if self.captureArea.isRunning() == True:
            self.consoleOutput.outputText("Captured points..")
            self.captureArea.recordMotion()
        # you could just do "print("test stuff")" to print to IDE consoles

    #same as above, this method is called wehn you click play motion button
    def play_motion(self):
        self.consoleOutput.outputText("playing motion...")
        self.captureArea.start_clicked()

    #Same, this button does not work. To pause, need access to CVHandlerCLass which is not made in this class.
    def pause_motion(self):
        self.consoleOutput.outputText("Motion Capture paused")
        self.captureArea.stopRecording()


        #self.captureArea.openMaskingDebugWindow()
        #self.playMotionAction.setEnabled(False)

        #self.setUpWizard.setGeometry(QtCore.QRect(1000,500,100,30))
        #self.setUpWizard.show()

    #same as above
    def stop_motion(self):
        self.consoleOutput.outputText("Motion Captured stopped")
        self.captureArea.stop_playback()

    #This method is called when clicked set up cameras button
    def setUpWizardAction(self):
        #This creates a new instance of SetUpWizard class
        self.setUpWizard = SetUpWizard()

    #This is just like the tool bar except this is a menu bar. "File, Edit, Help, ect"
    def init_menu_bar(self, MainWindow):
        #Create a new QMenuBar, Takes in a QMainWindow
        self.menuBar = QtGui.QMenuBar(MainWindow)
        #This line is false to improve functionality for Linux.
        self.menuBar.setNativeMenuBar(False)
        #This changes the size. NOTE: I did not set these numbers, they are auto generated in QT Designer 4
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1055, 25))
        #Every single QSomthing, need a UNIQUE object name, no 2 can be alike
        self.menuBar.setObjectName(_fromUtf8("menubar"))

        #Initialze the Menu Items
        #This is how you make menu items, like "File"
        self.menuFile = QtGui.QMenu(self.menuBar)
        # again needs a unique object name
        self.menuFile.setObjectName(_fromUtf8("menuFile"))

        #made a "Edit" menu item here
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))

        #made a "Project" menu item
        self.menuProject = QtGui.QMenu(self.menuBar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))

        #made a "View" menu item here
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))

        #made a "Tools" menu item
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))

        #Help menu item
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))

        #Note: The above lines makes the Main Menus, these are not the sub menus


        #blow is how to make actions for the menu bar.

        #These 5 lines is how to create a sub menu item
        #Open a project file Action
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        #This is how to set a shortcut.
        self.actionOpen.setShortcut("Ctrl+O")
        #this is a tool tip, just a tip that pops up if the user hovers over the button
        self.actionOpen.setStatusTip("Open a file")

        #this is how you link the button to a function
        #You might have notcie the "lambda". I don't truly understand it but let me explain why and what it is for.
        # in Python, to create an Anonamous function, you use the keyword lambda. Anonamous methods are like regular methods
        #except they do not have a method name. This is used here to pass in "MainWindow" to the Open_File method when the
        #user clicks
        #This is how you pass in veriables to a method that is connected to a button.
        self.actionOpen.triggered.connect(lambda: self.open_file(MainWindow))

        # New File Action
        self.actionNewFile = QtGui.QAction(MainWindow)
        self.actionNewFile.setObjectName(_fromUtf8("actionOpen"))
        self.actionNewFile.setShortcut("Ctrl+N")
        self.actionNewFile.setStatusTip("New File")
        self.actionNewFile.triggered.connect(self.new_file)

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

        self.actionOpenProjectViewerWindow = QtGui.QAction(MainWindow)
        self.actionOpenProjectViewerWindow.setObjectName(_fromUtf8("actionOpenProjectViewerWindow"))
        self.actionOpenProjectViewerWindow.setShortcut("Ctrl+P")
        self.actionOpenProjectViewerWindow.setStatusTip("Open Project Viewer Window")
        self.actionOpenProjectViewerWindow.triggered.connect(self.openProjectViewerWindow)

        self.setUpWizardActionButton = QtGui.QAction(MainWindow)
        self.setUpWizardActionButton.setObjectName(_fromUtf8("setUpWizardAction"))
        self.setUpWizardActionButton.setShortcut("Ctrl+K")
        self.setUpWizardActionButton.setStatusTip("Set up the Cameras")
        self.setUpWizardActionButton.triggered.connect(self.setUpWizardAction)

        self.actionOpenConsoleOutputWindow = QtGui.QAction(MainWindow)
        self.actionOpenConsoleOutputWindow.setObjectName(_fromUtf8("actionOpenConsoleOutputWindow"))
        self.actionOpenConsoleOutputWindow.setShortcut("Ctrl+L")
        self.actionOpenConsoleOutputWindow.setStatusTip("Open Console Window")
        self.actionOpenConsoleOutputWindow.triggered.connect(self.openConsoleOutputWindow)

        self.actionConnectToStream = QtGui.QAction(MainWindow)
        self.actionConnectToStream.setObjectName(_fromUtf8("actionConnectToStream"))
        self.actionConnectToStream.setShortcut("Ctrl+M")
        self.actionConnectToStream.setStatusTip("Connect to  a stream")
        self.actionConnectToStream.triggered.connect(self.connectToStream)

        #Add Action to the "File" submenu
        #here we add all the items to the "File" Menu
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionQuit)

        #Add Action to the "Project" submenu
        #Here we add actions to the "Project" menu
        self.menuProject.addAction(self.actionOpenProjectDirectory)
        self.menuProject.addAction(self.actionConnectToStream)

        #Add Actions to the "View" Submenu
        self.menuView.addAction(self.actionOpenProjectViewerWindow)
        self.menuView.addAction(self.actionOpenConsoleOutputWindow)

        #Add Menu Items to the Menu Bar
        #Here we add all the main menus to the menu Bar
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())


        #Add Menu Items to the Menu Bar
        self.menuTools.addAction(self.setUpWizardActionButton)

       
        #Name the Menu Items
        #used to set the text, can be used to translate to different languges
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuProject.setTitle(_translate("MainWindow", "Project", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNewFile.setText(_translate("MainWindow", "New File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionOpenProjectDirectory.setText(_translate("MainWindow", "Open Project Directory", None))
        self.actionOpenProjectViewerWindow.setText(_translate("MainWindow", "Open Project Viewer Window", None))
        self.actionConnectToStream.setText(_translate("MainWindow", "Connect to a Stream", None))
        self.actionOpenConsoleOutputWindow.setText(_translate("MainWindow", "Open Console Output Window", None))
        self.setUpWizardActionButton.setText(_translate("MainWindow", "Set up Cameras Wizard", None))

        #Set the Menu mar to the main menu.
        #You can put a menu bar on any Qwidget
        MainWindow.setMenuBar(self.menuBar)

    #A lot of the following methods are just used to link the menu buttons to.

    def open_project_directory(self):
      self.projectViewer.open_project_directory()
      #self.gridLayout.update()

    def new_file(self):
        self.captureArea.newTab()

    #This code is used to open up a file
    def open_file(self, MainWindow):
        self.dlg = QtGui.QFileDialog(MainWindow)
        self.dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        self.dlg.setFilter("Text files (*.mp4)")
        #self.fileName = QtCore.QString()

        #once you open a file, the file Name is set here
        #You can use this file name to do a "open(self.fileName, 'r')" This will be used when we open up files
        self.fileName = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open File', '/')

        #siple output the text to console
        self.consoleOutput.outputText("Opening file")

        #Here we need to check if it is a valid file. we can set filters in the project viewer class
        #once we have the motion file we want, pass it to Capture Area to open it in a tab.
        self.captureArea.openVideoFile(self.fileName)

        print(str(self.fileName))

    #This is used by the Quit button in the menu bar
    def close_application(self, MainWindow):
        choice = QtGui.QMessageBox.question(MainWindow,'Extract!', "Quit the Application?",QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    #This is used by the connect to a stream
    def connectToStream(self):
        #This makes a pop up box asking for an IP to connect to
        self.connectToStreamBox = ConnectToStreamBox(self.captureArea)
        #ipAddress = self.connectToStreamBox.getIpAddress()
        #self.captureArea.connectToIP(self.connectToStreamBox)


    #The following function will deal with opening Docked Windows
    #If you close out a dock widget, you can get them back with these lines.
    def openProjectViewerWindow(self):
        self.projectViewer.open_docker()

    def openConsoleOutputWindow(self):
        self.consoleOutput.open_docker()

    #Doesn't work here, Maybe Fix, maybe now. WOrks in MyWIndow CLass
    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            self.captureArea.stop_playback()
            event.accept()


#This class represents the whole window frame. This class is for handling OS Events. (X-out, keyboard, ect)
#This is a PyQT subclass. This class inherents from QtGUI.QMainWindow.
#NOTE: There can only be ONE QMainWindow class per program. SO do make pop up windows a MainWindow.
#also, this class creates a main thread, and like all GUI shit, some some connect be done in the main thread.
class MyWindow(QtGui.QMainWindow):
    #this is a virtual method that I have overridden from the super class.
    #this method is called when the user presses the red X at the top right.
    def closeEvent(self,event):
        #A simple pop up message with a yes or no option
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()

        #if the use clicks yes.
        if result == QtGui.QMessageBox.Yes:
            #I'm not sure what this does but it quits the program as I should.
            cam = cv2.VideoCapture(0)
            cam.release
            event.accept()
            print("Camera turned off")

    def resizeEvent(self, evt=None):
        pass
        #print("does this work")


#This is the entry point into the program
if __name__ == "__main__":


    #app is used to pass in system arguments to the application, not used for us
    app = QtGui.QApplication(sys.argv)

    #The main Window and the UI is best designed as 2 seperate things. This keeps design better
    MainWindow = MyWindow()



    #The ui is for the user interface, The main window is where all the UI needs to be placed, so we pass in the main window
    ui = Ui_MainWindow(MainWindow)

    #after we built the UI, we must show it.
    MainWindow.show()

    #exit
    sys.exit(app.exec_())

