# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" An application to rename files. """

# Python imports
import os # Miscellaneous operating system interfaces
import sys # System-specific parameters and functions

# PyQt imports
from PyQt4 import QtCore, QtGui

# Application classes
from filelisthandler import FileListHandler # A class to handle file lists

# Import mainwindow
from mainwindow import *

# Create a class for our mainwindow
class Main(QtGui.QMainWindow):

    # Initialize mainwindow
    def __init__(self):

        # Declare class variables
        self.path = "" # String for path

        # Create class instances
        self.filelist = FileListHandler()

        # Initialize top level window widget
        QtGui.QMainWindow.__init__(self)

        # This is always the same
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals, menu and toolbar
        self.ui.actionAddFiles.triggered.connect(self.addFiles)
        self.ui.actionAddFolder.triggered.connect(self.addFolder)
        self.ui.actionRemoveFiles.triggered.connect(self.removeFiles)
        self.ui.actionClearList.triggered.connect(self.clearList)
        self.ui.actionRename.triggered.connect(self.renameFiles)
        self.ui.actionQuit.triggered.connect(self.quitApplication)
        self.ui.actionAbout.triggered.connect(self.aboutMessage)

        # Connect signals, tab widget
        self.ui.tabMain.currentChanged.connect(self.changeTab)

        # Connect signals, counter
        self.ui.sboCounterPos.valueChanged.connect(self.addCounter)
        self.ui.cboCounterSide.activated.connect(self.addCounter)
        self.ui.sboCounterZeros.valueChanged.connect(self.addCounter)
        self.ui.chkCounterReplace.stateChanged.connect(self.addCounter)
        self.ui.btnCounter.clicked.connect(self.addCounter)

        # Connect signals, crop
        self.ui.sboCropStart.valueChanged.connect(self.addCrop)
        self.ui.sboCropEnd.valueChanged.connect(self.addCrop)
        self.ui.chkCropInvert.stateChanged.connect(self.addCrop)
        self.ui.btnCrop.clicked.connect(self.addCrop)

        # Connect signals, extension
        self.ui.txtExt.textEdited.connect(self.addExt)
        self.ui.btnExt.clicked.connect(self.addExt)

        # Connect signals, insert
        self.ui.txtInsertText.textEdited.connect(self.addInsert)
        self.ui.sboInsertPos.valueChanged.connect(self.addInsert)
        self.ui.cboInsertSide.activated.connect(self.addInsert)
        self.ui.btnInsert.clicked.connect(self.addInsert)

        # Connect signals, regex
        self.ui.txtRegExSearch.textEdited.connect(self.addRegEx)
        self.ui.txtRegExReplace.textEdited.connect(self.addRegEx)
        self.ui.btnRegEx.clicked.connect(self.addRegEx)

        # Connect signals, replace
        self.ui.txtReplaceSearch.textEdited.connect(self.addReplace)
        self.ui.txtReplaceWith.textEdited.connect(self.addReplace)
        self.ui.btnReplace.clicked.connect(self.addReplace)

        # Connect signals, text case
        self.ui.optTextCase1.clicked.connect(self.addTextCase)
        self.ui.optTextCase2.clicked.connect(self.addTextCase)
        self.ui.optTextCase3.clicked.connect(self.addTextCase)
        self.ui.optTextCase4.clicked.connect(self.addTextCase)
        self.ui.btnTextCase.clicked.connect(self.addTextCase)

        # Connect signals, trim
        self.ui.sboTrimLength.valueChanged.connect(self.addTrim)
        self.ui.cboTrimSide.activated.connect(self.addTrim)
        self.ui.btnTrim.clicked.connect(self.addTrim)

        # Icons
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.ui.actionAddFiles.setIcon(QtGui.QIcon("add_files.png"))
        self.ui.actionAddFolder.setIcon(QtGui.QIcon("add_folder.png"))
        self.ui.actionRemoveFiles.setIcon(QtGui.QIcon("remove.png"))
        self.ui.actionClearList.setIcon(QtGui.QIcon("clear.png"))
        self.ui.actionRename.setIcon(QtGui.QIcon("rename.png"))
        self.ui.actionQuit.setIcon(QtGui.QIcon("quit.png"))
        self.ui.actionAbout.setIcon(QtGui.QIcon("about.png"))
        self.ui.tabMain.setTabIcon(0, QtGui.QIcon("counter.png"))
        self.ui.tabMain.setTabIcon(1, QtGui.QIcon("crop.png"))
        self.ui.tabMain.setTabIcon(2, QtGui.QIcon("extension.png"))
        self.ui.tabMain.setTabIcon(3, QtGui.QIcon("insert.png"))
        self.ui.tabMain.setTabIcon(4, QtGui.QIcon("regex.png"))
        self.ui.tabMain.setTabIcon(5, QtGui.QIcon("replace.png"))
        self.ui.tabMain.setTabIcon(6, QtGui.QIcon("text_case.png"))
        self.ui.tabMain.setTabIcon(7, QtGui.QIcon("trim.png"))

        # Drag-and-drop events for file list
        self.ui.tblFileList.dragEnterEvent = self.dragEnterEvent
        self.ui.tblFileList.dragMoveEvent = self.dragEnterEvent
        self.ui.tblFileList.dropEvent = self.dropEvent

        # Select the first tab from the tab widget
        self.ui.tabMain.setCurrentIndex(0)

        # Load settings
        self.loadSettings()

        # Check if command line arguments has files in it
        if sys.argv[1:]:
            self.loopItems(sys.argv[1:])

        # Refresh table
        self.refreshTable()


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Actions
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # Add files
    def addFiles(self):

        # Get file list using a dialog
        items = QtGui.QFileDialog.getOpenFileNames(self, "Add files",
            self.path)

        # Check list for items
        if len(items) < 1:
            return

        # Loop items to main file list
        self.loopItems(items)


    # Add folder
    def addFolder(self):

        # Get folder using a dialog
        path = QtGui.QFileDialog.getExistingDirectory(self, "Add folder",
            self.path)

        # Check path
        if path == "":
            return

        # Check dir
        if not os.path.isdir(path):
            return

        # Create a list with full paths
        items = []
        for item in os.listdir(path):
            items.append(os.path.join(path, item))

        # Loop items to main file list
        self.loopItems(items)


    # Loop items to main file list
    def loopItems(self, items):

        nonexist = 0
        duplicates = 0
        folders = 0
        for item in items:

            # Check if item does not exist
            if not os.path.exists(item):
                nonexist += 1
                continue

            # Check for duplicates
            if self.filelist.exists(item):
                duplicates += 1
                continue

            # Check for folders
            if os.path.isdir(item):
                folders += 1
                continue

            # Check if file path is an existing regular file
            if not os.path.isfile(item):
                continue

            # Set the path from first file
            if item == items[0]:
                self.path = os.path.split(item)[0]

            # Add file
            self.filelist.addfile(item)

        # Check for files, sort them, enable widgets and refresh table
        if self.filelist.count > 0:
            self.filelist.sort()
            self.enableWidgets()
            self.refreshTable()

        # Count total adds and message user, if necessary
        total = nonexist
        total += duplicates
        total += folders
        if total > 0:
            msg = "%s items were skipped:\n" % (total)
            msg += "\n"
            msg += "%s doesn't exist\n" % (nonexist)
            msg += "%s duplicates\n" % (duplicates)
            msg += "%s folders\n" % (folders)
            QtGui.QMessageBox.information(self, "Info", msg)


    # Clear list
    def clearList(self):
        self.filelist.clear()
        self.disableWidgets()
        self.refreshTable()


    # Remove files
    def removeFiles(self):

        # Check if file list is empty
        if self.filelist.count < 1:
            msg = "No files in list."
            QtGui.QMessageBox.critical(self, "Error", msg)
            return

        # Check table's selected items
        if not self.ui.tblFileList.selectedIndexes():
            msg = "Please select file."
            QtGui.QMessageBox.critical(self, "Error", msg)
            return

        # Get indexes from table
        rows = []
        for item in self.ui.tblFileList.selectedIndexes():
            index = int(item.row())
            if index not in rows:
                rows.append(index)

        # Remove items in reverse order (so the indexes won't change)
        for index in sorted(rows, reverse=True):
            self.filelist.remove(index)

        # Check file list for files
        if self.filelist.count < 1:
            self.disableWidgets()

        # Refresh table
        self.refreshTable()


    # Rename files
    def renameFiles(self):
        ok = self.filelist.rename()
        self.filelist.reset()
        self.refreshTable()
        if ok:
            message = "Files renamed successfully."
            QtGui.QMessageBox.information(self, "Info", message)
        else:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)


    # Quit
    def quitApplication(self):
        QtGui.QApplication.quit()


    # Help > about...
    def aboutMessage(self):
        msg = """<strong>bwRenamer</strong><br />
        Version 1.0.0<br />
        <br />
        This is free software.<br />
        Released under the General Public License.<br />
        <br />
        <a href="http://sourceforge.net/projects/bwrenamer">SourceForge</a>"""
        QtGui.QMessageBox.about(self, "About", msg)


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Events
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # Drag
    def dragEnterEvent(self, event):
        if (event.type() == QtCore.QEvent.DragEnter):
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()

    # Drop
    def dropEvent(self, event):
        if (event.type() == QtCore.QEvent.Drop):
            if event.mimeData().hasUrls():

                # Make a list of items from drag-and-drop
                items = []
                for i in event.mimeData().urls():
                    items.append(i.toLocalFile())

                # Loop items to main file list
                self.loopItems(items)


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Settings
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def loadSettings(self):
        try:
            settings = QtCore.QSettings("bulkware", "bwRenamer")
            if settings.contains("geometry"): # Window geometry
                self.restoreGeometry(settings.value("geometry"))
            if settings.contains("state"): # Window state
                self.restoreState(settings.value("state"))
            if settings.contains("path"):
                self.path = settings.value("path", type=str)
            if settings.contains("tabindex"):
                tabindex = settings.value("tabindex", type=int)
                self.ui.tabMain.setCurrentIndex(tabindex)
        except:
            self.path = ""
            self.ui.tabMain.setCurrentIndex(0)
            return False
        else:
            return True


    # Save settings when closing the application
    def closeEvent(self, event):
        settings = QtCore.QSettings("bulkware", "bwRenamer")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("state", self.saveState())
        settings.setValue("path", self.path)
        settings.setValue("tabindex", self.ui.tabMain.currentIndex())


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Widgets
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # Tab widget
    def changeTab(self, index):
        if self.filelist.count < 1: return
        tabname = str(self.ui.tabMain.tabText(index))
        if tabname == "Counter": self.addCounter()
        elif tabname == "Crop": self.addCrop()
        elif tabname == "Extension": self.addExt()
        elif tabname == "Insert": self.addInsert()
        elif tabname == "RegEx": self.addRegEx()
        elif tabname == "Replace": self.addReplace()
        elif tabname == "Text case": self.addTextCase()
        elif tabname == "Trim": self.addTrim()


    # Counter
    def addCounter(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnCounter":
            preview = False
        pos = int(self.ui.sboCounterPos.text())
        side = int(self.ui.cboCounterSide.currentIndex())
        zeros = int(self.ui.sboCounterZeros.text()) + 1
        if self.ui.chkCounterReplace.isChecked():
            replace = True
        else:
            replace = False
        ok = self.filelist.counter(pos, side, zeros, replace, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # Crop
    def addCrop(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnCrop":
            preview = False
        start = int(self.ui.sboCropStart.text())
        end = int(self.ui.sboCropEnd.text())
        if self.ui.chkCropInvert.isChecked():
            invert = True
        else:
            invert = False
        ok = self.filelist.crop(start, end, invert, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # Extension
    def addExt(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnExt":
            preview = False
        ext = self.ui.txtExt.text()
        ok = self.filelist.extension(ext, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # Insert
    def addInsert(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnInsert":
            preview = False
        text = self.ui.txtInsertText.text()
        pos = int(self.ui.sboInsertPos.text())
        side = int(self.ui.cboInsertSide.currentIndex())
        ok = self.filelist.insert(text, pos, side, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # RegEx
    def addRegEx(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnRegEx":
            preview = False
        old = self.ui.txtRegExSearch.text()
        new = self.ui.txtRegExReplace.text()
        ok = self.filelist.regex(old, new, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # Replace
    def addReplace(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnReplace":
            preview = False
        old = self.ui.txtReplaceSearch.text()
        new = self.ui.txtReplaceWith.text()
        ok = self.filelist.replace(old, new, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # Text case
    def addTextCase(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnTextCase":
            preview = False
        if self.ui.optTextCase1.isChecked():
            mode = 0
        elif self.ui.optTextCase2.isChecked():
            mode = 1
        elif self.ui.optTextCase3.isChecked():
            mode = 2
        elif self.ui.optTextCase4.isChecked():
            mode = 3
        ok = self.filelist.textcase(mode, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # Trim
    def addTrim(self):
        preview = True
        if self.sender() and str(self.sender().objectName()) == "btnTrim":
            preview = False
        length = int(self.ui.sboTrimLength.text())
        side = int(self.ui.cboTrimSide.currentIndex())
        ok = self.filelist.trim(length, side, preview)
        if not ok and not preview:
            QtGui.QMessageBox.critical(self, "Error", self.filelist.error)
        self.refreshTable()


    # Refresh table
    def refreshTable(self):

        # Clear widgets
        self.ui.tblFileList.setColumnCount(0)
        self.ui.tblFileList.setRowCount(0)
        self.ui.tblFileList.clear()

        # Check if file list is empty
        if self.filelist.count < 1:
            return

        # Set columns and rows
        self.ui.tblFileList.setColumnCount(4)
        self.ui.tblFileList.setRowCount(self.filelist.count)

        # Set header labels
        self.ui.tblFileList.setHorizontalHeaderLabels(["Original", "Modified", \
            "Preview", ""])

        # Populate table
        for i, file in enumerate(self.filelist.filelist):
            item = QtGui.QTableWidgetItem(file[2])
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
            self.ui.tblFileList.setItem(i, 0, item)

            item = QtGui.QTableWidgetItem(file[3])
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
            self.ui.tblFileList.setItem(i, 1, item)

            item = QtGui.QTableWidgetItem(file[4])
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
            self.ui.tblFileList.setItem(i, 2, item)

            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.ui.tblFileList.setItem(i, 3, item)

        # Resize columns to contents
        # setVisible lines are because of QTBUG-9352!
        self.ui.tblFileList.setVisible(False)
        self.ui.tblFileList.resizeColumnsToContents()
        self.ui.tblFileList.setVisible(True)


    # Disable widgets
    def disableWidgets(self):
        self.ui.actionRemoveFiles.setEnabled(False)
        self.ui.actionClearList.setEnabled(False)
        self.ui.actionRename.setEnabled(False)
        self.ui.tabMain.setEnabled(False)


    # Enable widgets
    def enableWidgets(self):
        self.ui.actionRemoveFiles.setEnabled(True)
        self.ui.actionClearList.setEnabled(True)
        self.ui.actionRename.setEnabled(True)
        self.ui.tabMain.setEnabled(True)


# Creates an application object and begins the event handling loop
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    ret = app.exec_()
    sys.exit(ret)
