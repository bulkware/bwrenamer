# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Feb 23 21:36:48 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tblFileList = QtGui.QTableWidget(self.centralwidget)
        self.tblFileList.setAcceptDrops(True)
        self.tblFileList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblFileList.setAlternatingRowColors(True)
        self.tblFileList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tblFileList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblFileList.setObjectName(_fromUtf8("tblFileList"))
        self.tblFileList.setColumnCount(0)
        self.tblFileList.setRowCount(0)
        self.tblFileList.horizontalHeader().setCascadingSectionResizes(False)
        self.tblFileList.horizontalHeader().setStretchLastSection(True)
        self.tblFileList.verticalHeader().setVisible(True)
        self.tblFileList.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tblFileList)
        self.tabMain = QtGui.QTabWidget(self.centralwidget)
        self.tabMain.setEnabled(True)
        self.tabMain.setMaximumSize(QtCore.QSize(16777215, 220))
        self.tabMain.setTabsClosable(False)
        self.tabMain.setMovable(False)
        self.tabMain.setObjectName(_fromUtf8("tabMain"))
        self.tabCounter = QtGui.QWidget()
        self.tabCounter.setObjectName(_fromUtf8("tabCounter"))
        self.lblCounter = QtGui.QLabel(self.tabCounter)
        self.lblCounter.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCounter.setFont(font)
        self.lblCounter.setObjectName(_fromUtf8("lblCounter"))
        self.btnCounter = QtGui.QPushButton(self.tabCounter)
        self.btnCounter.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnCounter.setObjectName(_fromUtf8("btnCounter"))
        self.lblCounterSide = QtGui.QLabel(self.tabCounter)
        self.lblCounterSide.setGeometry(QtCore.QRect(90, 60, 71, 16))
        self.lblCounterSide.setObjectName(_fromUtf8("lblCounterSide"))
        self.sboCounterZeros = QtGui.QSpinBox(self.tabCounter)
        self.sboCounterZeros.setGeometry(QtCore.QRect(170, 80, 71, 22))
        self.sboCounterZeros.setObjectName(_fromUtf8("sboCounterZeros"))
        self.cboCounterSide = QtGui.QComboBox(self.tabCounter)
        self.cboCounterSide.setGeometry(QtCore.QRect(90, 80, 71, 22))
        self.cboCounterSide.setObjectName(_fromUtf8("cboCounterSide"))
        self.cboCounterSide.addItem(_fromUtf8(""))
        self.cboCounterSide.addItem(_fromUtf8(""))
        self.sboCounterPos = QtGui.QSpinBox(self.tabCounter)
        self.sboCounterPos.setGeometry(QtCore.QRect(10, 80, 71, 22))
        self.sboCounterPos.setObjectName(_fromUtf8("sboCounterPos"))
        self.chkCounterReplace = QtGui.QCheckBox(self.tabCounter)
        self.chkCounterReplace.setGeometry(QtCore.QRect(10, 120, 231, 17))
        self.chkCounterReplace.setObjectName(_fromUtf8("chkCounterReplace"))
        self.lblCounterZeros = QtGui.QLabel(self.tabCounter)
        self.lblCounterZeros.setGeometry(QtCore.QRect(170, 60, 71, 16))
        self.lblCounterZeros.setObjectName(_fromUtf8("lblCounterZeros"))
        self.lblCounterPos = QtGui.QLabel(self.tabCounter)
        self.lblCounterPos.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.lblCounterPos.setObjectName(_fromUtf8("lblCounterPos"))
        self.tabMain.addTab(self.tabCounter, _fromUtf8(""))
        self.tabCrop = QtGui.QWidget()
        self.tabCrop.setObjectName(_fromUtf8("tabCrop"))
        self.lblCrop = QtGui.QLabel(self.tabCrop)
        self.lblCrop.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCrop.setFont(font)
        self.lblCrop.setObjectName(_fromUtf8("lblCrop"))
        self.btnCrop = QtGui.QPushButton(self.tabCrop)
        self.btnCrop.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnCrop.setObjectName(_fromUtf8("btnCrop"))
        self.lblCropStart = QtGui.QLabel(self.tabCrop)
        self.lblCropStart.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.lblCropStart.setObjectName(_fromUtf8("lblCropStart"))
        self.sboCropStart = QtGui.QSpinBox(self.tabCrop)
        self.sboCropStart.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.sboCropStart.setProperty("value", 1)
        self.sboCropStart.setObjectName(_fromUtf8("sboCropStart"))
        self.lblCropEnd = QtGui.QLabel(self.tabCrop)
        self.lblCropEnd.setGeometry(QtCore.QRect(130, 60, 71, 16))
        self.lblCropEnd.setObjectName(_fromUtf8("lblCropEnd"))
        self.sboCropEnd = QtGui.QSpinBox(self.tabCrop)
        self.sboCropEnd.setGeometry(QtCore.QRect(130, 80, 111, 22))
        self.sboCropEnd.setProperty("value", 99)
        self.sboCropEnd.setObjectName(_fromUtf8("sboCropEnd"))
        self.chkCropInvert = QtGui.QCheckBox(self.tabCrop)
        self.chkCropInvert.setGeometry(QtCore.QRect(10, 120, 231, 17))
        self.chkCropInvert.setObjectName(_fromUtf8("chkCropInvert"))
        self.tabMain.addTab(self.tabCrop, _fromUtf8(""))
        self.tabExt = QtGui.QWidget()
        self.tabExt.setObjectName(_fromUtf8("tabExt"))
        self.lblExt = QtGui.QLabel(self.tabExt)
        self.lblExt.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblExt.setFont(font)
        self.lblExt.setObjectName(_fromUtf8("lblExt"))
        self.txtExt = QtGui.QLineEdit(self.tabExt)
        self.txtExt.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.txtExt.setText(_fromUtf8(""))
        self.txtExt.setObjectName(_fromUtf8("txtExt"))
        self.lblExtNew = QtGui.QLabel(self.tabExt)
        self.lblExtNew.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.lblExtNew.setObjectName(_fromUtf8("lblExtNew"))
        self.btnExt = QtGui.QPushButton(self.tabExt)
        self.btnExt.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnExt.setObjectName(_fromUtf8("btnExt"))
        self.tabMain.addTab(self.tabExt, _fromUtf8(""))
        self.tabInsert = QtGui.QWidget()
        self.tabInsert.setObjectName(_fromUtf8("tabInsert"))
        self.btnInsert = QtGui.QPushButton(self.tabInsert)
        self.btnInsert.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnInsert.setObjectName(_fromUtf8("btnInsert"))
        self.txtInsertText = QtGui.QLineEdit(self.tabInsert)
        self.txtInsertText.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.txtInsertText.setObjectName(_fromUtf8("txtInsertText"))
        self.lblInsert = QtGui.QLabel(self.tabInsert)
        self.lblInsert.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblInsert.setFont(font)
        self.lblInsert.setObjectName(_fromUtf8("lblInsert"))
        self.cboInsertSide = QtGui.QComboBox(self.tabInsert)
        self.cboInsertSide.setGeometry(QtCore.QRect(130, 130, 111, 22))
        self.cboInsertSide.setObjectName(_fromUtf8("cboInsertSide"))
        self.cboInsertSide.addItem(_fromUtf8(""))
        self.cboInsertSide.addItem(_fromUtf8(""))
        self.lblInsertPos = QtGui.QLabel(self.tabInsert)
        self.lblInsertPos.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.lblInsertPos.setObjectName(_fromUtf8("lblInsertPos"))
        self.sboInsertPos = QtGui.QSpinBox(self.tabInsert)
        self.sboInsertPos.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.sboInsertPos.setObjectName(_fromUtf8("sboInsertPos"))
        self.lblInsertSide = QtGui.QLabel(self.tabInsert)
        self.lblInsertSide.setGeometry(QtCore.QRect(130, 110, 111, 20))
        self.lblInsertSide.setObjectName(_fromUtf8("lblInsertSide"))
        self.label_2 = QtGui.QLabel(self.tabInsert)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabMain.addTab(self.tabInsert, _fromUtf8(""))
        self.tabRegEx = QtGui.QWidget()
        self.tabRegEx.setObjectName(_fromUtf8("tabRegEx"))
        self.btnRegEx = QtGui.QPushButton(self.tabRegEx)
        self.btnRegEx.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnRegEx.setObjectName(_fromUtf8("btnRegEx"))
        self.txtRegExReplace = QtGui.QLineEdit(self.tabRegEx)
        self.txtRegExReplace.setGeometry(QtCore.QRect(10, 130, 231, 20))
        self.txtRegExReplace.setObjectName(_fromUtf8("txtRegExReplace"))
        self.lblRegEx = QtGui.QLabel(self.tabRegEx)
        self.lblRegEx.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblRegEx.setFont(font)
        self.lblRegEx.setObjectName(_fromUtf8("lblRegEx"))
        self.lblRegExSearch = QtGui.QLabel(self.tabRegEx)
        self.lblRegExSearch.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.lblRegExSearch.setObjectName(_fromUtf8("lblRegExSearch"))
        self.txtRegExSearch = QtGui.QLineEdit(self.tabRegEx)
        self.txtRegExSearch.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.txtRegExSearch.setObjectName(_fromUtf8("txtRegExSearch"))
        self.lblRegExReplace = QtGui.QLabel(self.tabRegEx)
        self.lblRegExReplace.setGeometry(QtCore.QRect(10, 110, 231, 16))
        self.lblRegExReplace.setObjectName(_fromUtf8("lblRegExReplace"))
        self.label = QtGui.QLabel(self.tabRegEx)
        self.label.setGeometry(QtCore.QRect(400, 10, 361, 171))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabMain.addTab(self.tabRegEx, _fromUtf8(""))
        self.tabReplace = QtGui.QWidget()
        self.tabReplace.setObjectName(_fromUtf8("tabReplace"))
        self.btnReplace = QtGui.QPushButton(self.tabReplace)
        self.btnReplace.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnReplace.setObjectName(_fromUtf8("btnReplace"))
        self.lblReplaceSearch = QtGui.QLabel(self.tabReplace)
        self.lblReplaceSearch.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.lblReplaceSearch.setObjectName(_fromUtf8("lblReplaceSearch"))
        self.lblReplace = QtGui.QLabel(self.tabReplace)
        self.lblReplace.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblReplace.setFont(font)
        self.lblReplace.setObjectName(_fromUtf8("lblReplace"))
        self.txtReplaceWith = QtGui.QLineEdit(self.tabReplace)
        self.txtReplaceWith.setGeometry(QtCore.QRect(10, 130, 231, 20))
        self.txtReplaceWith.setObjectName(_fromUtf8("txtReplaceWith"))
        self.txtReplaceSearch = QtGui.QLineEdit(self.tabReplace)
        self.txtReplaceSearch.setGeometry(QtCore.QRect(10, 80, 231, 20))
        self.txtReplaceSearch.setObjectName(_fromUtf8("txtReplaceSearch"))
        self.lblReplaceWith = QtGui.QLabel(self.tabReplace)
        self.lblReplaceWith.setGeometry(QtCore.QRect(10, 110, 231, 16))
        self.lblReplaceWith.setObjectName(_fromUtf8("lblReplaceWith"))
        self.tabMain.addTab(self.tabReplace, _fromUtf8(""))
        self.tabTextCase = QtGui.QWidget()
        self.tabTextCase.setObjectName(_fromUtf8("tabTextCase"))
        self.btnTextCase = QtGui.QPushButton(self.tabTextCase)
        self.btnTextCase.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnTextCase.setObjectName(_fromUtf8("btnTextCase"))
        self.lblTextCase = QtGui.QLabel(self.tabTextCase)
        self.lblTextCase.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTextCase.setFont(font)
        self.lblTextCase.setObjectName(_fromUtf8("lblTextCase"))
        self.grpTextCaseMode = QtGui.QGroupBox(self.tabTextCase)
        self.grpTextCaseMode.setGeometry(QtCore.QRect(10, 50, 231, 101))
        self.grpTextCaseMode.setObjectName(_fromUtf8("grpTextCaseMode"))
        self.optTextCase1 = QtGui.QRadioButton(self.grpTextCaseMode)
        self.optTextCase1.setGeometry(QtCore.QRect(0, 20, 231, 17))
        self.optTextCase1.setChecked(True)
        self.optTextCase1.setObjectName(_fromUtf8("optTextCase1"))
        self.optTextCase2 = QtGui.QRadioButton(self.grpTextCaseMode)
        self.optTextCase2.setGeometry(QtCore.QRect(0, 40, 231, 17))
        self.optTextCase2.setObjectName(_fromUtf8("optTextCase2"))
        self.optTextCase3 = QtGui.QRadioButton(self.grpTextCaseMode)
        self.optTextCase3.setGeometry(QtCore.QRect(0, 60, 231, 17))
        self.optTextCase3.setObjectName(_fromUtf8("optTextCase3"))
        self.optTextCase4 = QtGui.QRadioButton(self.grpTextCaseMode)
        self.optTextCase4.setGeometry(QtCore.QRect(0, 80, 231, 17))
        self.optTextCase4.setObjectName(_fromUtf8("optTextCase4"))
        self.tabMain.addTab(self.tabTextCase, _fromUtf8(""))
        self.tabTrim = QtGui.QWidget()
        self.tabTrim.setObjectName(_fromUtf8("tabTrim"))
        self.btnTrim = QtGui.QPushButton(self.tabTrim)
        self.btnTrim.setGeometry(QtCore.QRect(170, 160, 71, 23))
        self.btnTrim.setObjectName(_fromUtf8("btnTrim"))
        self.lblTrimLength = QtGui.QLabel(self.tabTrim)
        self.lblTrimLength.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.lblTrimLength.setObjectName(_fromUtf8("lblTrimLength"))
        self.sboTrimLength = QtGui.QSpinBox(self.tabTrim)
        self.sboTrimLength.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.sboTrimLength.setMinimum(1)
        self.sboTrimLength.setProperty("value", 1)
        self.sboTrimLength.setObjectName(_fromUtf8("sboTrimLength"))
        self.lblTrimSide = QtGui.QLabel(self.tabTrim)
        self.lblTrimSide.setGeometry(QtCore.QRect(130, 60, 111, 20))
        self.lblTrimSide.setObjectName(_fromUtf8("lblTrimSide"))
        self.lblTrim = QtGui.QLabel(self.tabTrim)
        self.lblTrim.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTrim.setFont(font)
        self.lblTrim.setObjectName(_fromUtf8("lblTrim"))
        self.cboTrimSide = QtGui.QComboBox(self.tabTrim)
        self.cboTrimSide.setGeometry(QtCore.QRect(128, 80, 111, 22))
        self.cboTrimSide.setObjectName(_fromUtf8("cboTrimSide"))
        self.cboTrimSide.addItem(_fromUtf8(""))
        self.cboTrimSide.addItem(_fromUtf8(""))
        self.tabMain.addTab(self.tabTrim, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabMain)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAddFiles = QtGui.QAction(MainWindow)
        self.actionAddFiles.setObjectName(_fromUtf8("actionAddFiles"))
        self.actionAddFolder = QtGui.QAction(MainWindow)
        self.actionAddFolder.setObjectName(_fromUtf8("actionAddFolder"))
        self.actionClearList = QtGui.QAction(MainWindow)
        self.actionClearList.setEnabled(False)
        self.actionClearList.setObjectName(_fromUtf8("actionClearList"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExt = QtGui.QAction(MainWindow)
        self.actionExt.setObjectName(_fromUtf8("actionExt"))
        self.actionReplace = QtGui.QAction(MainWindow)
        self.actionReplace.setObjectName(_fromUtf8("actionReplace"))
        self.actionInsert = QtGui.QAction(MainWindow)
        self.actionInsert.setObjectName(_fromUtf8("actionInsert"))
        self.actionTrim = QtGui.QAction(MainWindow)
        self.actionTrim.setObjectName(_fromUtf8("actionTrim"))
        self.actionRegEx = QtGui.QAction(MainWindow)
        self.actionRegEx.setObjectName(_fromUtf8("actionRegEx"))
        self.actionCounter = QtGui.QAction(MainWindow)
        self.actionCounter.setObjectName(_fromUtf8("actionCounter"))
        self.actionTextCase = QtGui.QAction(MainWindow)
        self.actionTextCase.setObjectName(_fromUtf8("actionTextCase"))
        self.actionCrop = QtGui.QAction(MainWindow)
        self.actionCrop.setObjectName(_fromUtf8("actionCrop"))
        self.actionRename = QtGui.QAction(MainWindow)
        self.actionRename.setEnabled(False)
        self.actionRename.setObjectName(_fromUtf8("actionRename"))
        self.actionRemoveFiles = QtGui.QAction(MainWindow)
        self.actionRemoveFiles.setEnabled(False)
        self.actionRemoveFiles.setObjectName(_fromUtf8("actionRemoveFiles"))
        self.menuFile.addAction(self.actionAddFiles)
        self.menuFile.addAction(self.actionAddFolder)
        self.menuFile.addAction(self.actionRemoveFiles)
        self.menuFile.addAction(self.actionRename)
        self.menuFile.addAction(self.actionClearList)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAddFiles)
        self.toolBar.addAction(self.actionAddFolder)
        self.toolBar.addAction(self.actionRemoveFiles)
        self.toolBar.addAction(self.actionClearList)
        self.toolBar.addAction(self.actionRename)

        self.retranslateUi(MainWindow)
        self.tabMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tblFileList, self.tabMain)
        MainWindow.setTabOrder(self.tabMain, self.sboCounterPos)
        MainWindow.setTabOrder(self.sboCounterPos, self.cboCounterSide)
        MainWindow.setTabOrder(self.cboCounterSide, self.sboCounterZeros)
        MainWindow.setTabOrder(self.sboCounterZeros, self.chkCounterReplace)
        MainWindow.setTabOrder(self.chkCounterReplace, self.btnCounter)
        MainWindow.setTabOrder(self.btnCounter, self.sboCropStart)
        MainWindow.setTabOrder(self.sboCropStart, self.sboCropEnd)
        MainWindow.setTabOrder(self.sboCropEnd, self.chkCropInvert)
        MainWindow.setTabOrder(self.chkCropInvert, self.btnCrop)
        MainWindow.setTabOrder(self.btnCrop, self.txtExt)
        MainWindow.setTabOrder(self.txtExt, self.btnExt)
        MainWindow.setTabOrder(self.btnExt, self.txtInsertText)
        MainWindow.setTabOrder(self.txtInsertText, self.sboInsertPos)
        MainWindow.setTabOrder(self.sboInsertPos, self.cboInsertSide)
        MainWindow.setTabOrder(self.cboInsertSide, self.btnInsert)
        MainWindow.setTabOrder(self.btnInsert, self.txtRegExSearch)
        MainWindow.setTabOrder(self.txtRegExSearch, self.txtRegExReplace)
        MainWindow.setTabOrder(self.txtRegExReplace, self.btnRegEx)
        MainWindow.setTabOrder(self.btnRegEx, self.txtReplaceSearch)
        MainWindow.setTabOrder(self.txtReplaceSearch, self.txtReplaceWith)
        MainWindow.setTabOrder(self.txtReplaceWith, self.btnReplace)
        MainWindow.setTabOrder(self.btnReplace, self.optTextCase1)
        MainWindow.setTabOrder(self.optTextCase1, self.optTextCase2)
        MainWindow.setTabOrder(self.optTextCase2, self.optTextCase3)
        MainWindow.setTabOrder(self.optTextCase3, self.optTextCase4)
        MainWindow.setTabOrder(self.optTextCase4, self.btnTextCase)
        MainWindow.setTabOrder(self.btnTextCase, self.sboTrimLength)
        MainWindow.setTabOrder(self.sboTrimLength, self.cboTrimSide)
        MainWindow.setTabOrder(self.cboTrimSide, self.btnTrim)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "bwRenamer", None))
        self.lblCounter.setText(_translate("MainWindow", "Counter", None))
        self.btnCounter.setText(_translate("MainWindow", "Set", None))
        self.lblCounterSide.setText(_translate("MainWindow", "Side", None))
        self.cboCounterSide.setItemText(0, _translate("MainWindow", "Left", None))
        self.cboCounterSide.setItemText(1, _translate("MainWindow", "Right", None))
        self.chkCounterReplace.setText(_translate("MainWindow", "Replace filename", None))
        self.lblCounterZeros.setText(_translate("MainWindow", "Zeros", None))
        self.lblCounterPos.setText(_translate("MainWindow", "Position", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabCounter), _translate("MainWindow", "Counter", None))
        self.lblCrop.setText(_translate("MainWindow", "Crop", None))
        self.btnCrop.setText(_translate("MainWindow", "Set", None))
        self.lblCropStart.setText(_translate("MainWindow", "Start", None))
        self.lblCropEnd.setText(_translate("MainWindow", "End", None))
        self.chkCropInvert.setText(_translate("MainWindow", "Invert", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabCrop), _translate("MainWindow", "Crop", None))
        self.lblExt.setText(_translate("MainWindow", "Extension", None))
        self.lblExtNew.setText(_translate("MainWindow", "New extension:", None))
        self.btnExt.setText(_translate("MainWindow", "Set", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabExt), _translate("MainWindow", "Extension", None))
        self.btnInsert.setText(_translate("MainWindow", "Set", None))
        self.lblInsert.setText(_translate("MainWindow", "Insert", None))
        self.cboInsertSide.setItemText(0, _translate("MainWindow", "Left", None))
        self.cboInsertSide.setItemText(1, _translate("MainWindow", "Right", None))
        self.lblInsertPos.setText(_translate("MainWindow", "Position", None))
        self.lblInsertSide.setText(_translate("MainWindow", "Side", None))
        self.label_2.setText(_translate("MainWindow", "String", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabInsert), _translate("MainWindow", "Insert", None))
        self.btnRegEx.setText(_translate("MainWindow", "Set", None))
        self.lblRegEx.setText(_translate("MainWindow", "RegEx", None))
        self.lblRegExSearch.setText(_translate("MainWindow", "Search", None))
        self.lblRegExReplace.setText(_translate("MainWindow", "Replace with", None))
        self.label.setText(_translate("MainWindow", "\"In computing, a regular expression (abbreviated regex or regexp) is a sequence of characters that forms a search pattern, mainly for use in pattern matching with strings, or string matching, i.e. \"find and replace\"-like operations.\" - <a href=\"http://en.wikipedia.org/wiki/Regular_expression\">Wikipedia</a><br /><br /> Examples:<br />\\d = match digits<br />\\w = match all word characters<br />\\s = match all whitespace characters<br /><br />For more information, visit <a href=\"http://www.regular-expressions.info/\">this site</a>.", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabRegEx), _translate("MainWindow", "RegEx", None))
        self.btnReplace.setText(_translate("MainWindow", "Set", None))
        self.lblReplaceSearch.setText(_translate("MainWindow", "Search", None))
        self.lblReplace.setText(_translate("MainWindow", "Replace", None))
        self.lblReplaceWith.setText(_translate("MainWindow", "Replace with", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabReplace), _translate("MainWindow", "Replace", None))
        self.btnTextCase.setText(_translate("MainWindow", "Set", None))
        self.lblTextCase.setText(_translate("MainWindow", "Text case", None))
        self.grpTextCaseMode.setTitle(_translate("MainWindow", "Mode", None))
        self.optTextCase1.setText(_translate("MainWindow", "Capitalize text", None))
        self.optTextCase2.setText(_translate("MainWindow", "Title Case", None))
        self.optTextCase3.setText(_translate("MainWindow", "lowercase", None))
        self.optTextCase4.setText(_translate("MainWindow", "UPPERCASE", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabTextCase), _translate("MainWindow", "Text case", None))
        self.btnTrim.setText(_translate("MainWindow", "Set", None))
        self.lblTrimLength.setText(_translate("MainWindow", "Length", None))
        self.lblTrimSide.setText(_translate("MainWindow", "Side", None))
        self.lblTrim.setText(_translate("MainWindow", "Trim", None))
        self.cboTrimSide.setItemText(0, _translate("MainWindow", "Left", None))
        self.cboTrimSide.setItemText(1, _translate("MainWindow", "Right", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabTrim), _translate("MainWindow", "Trim", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionAddFiles.setText(_translate("MainWindow", "Add files", None))
        self.actionAddFolder.setText(_translate("MainWindow", "Add folder", None))
        self.actionAddFolder.setToolTip(_translate("MainWindow", "Add folder", None))
        self.actionClearList.setText(_translate("MainWindow", "Clear list", None))
        self.actionClearList.setToolTip(_translate("MainWindow", "Clear list", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionExt.setText(_translate("MainWindow", "Extension", None))
        self.actionReplace.setText(_translate("MainWindow", "Replace", None))
        self.actionInsert.setText(_translate("MainWindow", "Insert", None))
        self.actionTrim.setText(_translate("MainWindow", "Trim", None))
        self.actionRegEx.setText(_translate("MainWindow", "RegEx", None))
        self.actionCounter.setText(_translate("MainWindow", "Counter", None))
        self.actionTextCase.setText(_translate("MainWindow", "Text case", None))
        self.actionCrop.setText(_translate("MainWindow", "Crop", None))
        self.actionRename.setText(_translate("MainWindow", "Rename files", None))
        self.actionRename.setToolTip(_translate("MainWindow", "Rename files", None))
        self.actionRemoveFiles.setText(_translate("MainWindow", "Remove files", None))
        self.actionRemoveFiles.setToolTip(_translate("MainWindow", "Remove files", None))

