# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gisHelperGui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
# flake8:  noqa

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabContainer = QtWidgets.QTabWidget(self.centralwidget)
        self.tabContainer.setEnabled(True)
        self.tabContainer.setGeometry(QtCore.QRect(10, 6, 781, 569))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.tabContainer.setFont(font)
        self.tabContainer.setAcceptDrops(False)
        self.tabContainer.setObjectName("tabContainer")
        self.gisCalc = QtWidgets.QWidget()
        self.gisCalc.setObjectName("gisCalc")
        self.centroidGroup = QtWidgets.QGroupBox(self.gisCalc)
        self.centroidGroup.setGeometry(QtCore.QRect(4, 20, 361, 529))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.centroidGroup.setFont(font)
        self.centroidGroup.setTitle("")
        self.centroidGroup.setObjectName("centroidGroup")
        self.centroidCalcLabel = QtWidgets.QLabel(self.centroidGroup)
        self.centroidCalcLabel.setGeometry(QtCore.QRect(20, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.centroidCalcLabel.setFont(font)
        self.centroidCalcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.centroidCalcLabel.setObjectName("centroidCalcLabel")
        self.originClearButton = QtWidgets.QPushButton(self.centroidGroup)
        self.originClearButton.setEnabled(True)
        self.originClearButton.setGeometry(QtCore.QRect(10, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.originClearButton.setFont(font)
        self.originClearButton.setObjectName("originClearButton")
        self.originCalculateButton = QtWidgets.QPushButton(self.centroidGroup)
        self.originCalculateButton.setEnabled(True)
        self.originCalculateButton.setGeometry(QtCore.QRect(240, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.originCalculateButton.setFont(font)
        self.originCalculateButton.setObjectName("originCalculateButton")
        self.originResultsLabel = QtWidgets.QLabel(self.centroidGroup)
        self.originResultsLabel.setGeometry(QtCore.QRect(20, 350, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.originResultsLabel.setFont(font)
        self.originResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.originResultsLabel.setObjectName("originResultsLabel")
        self.ddButtonCalcOrigin_2 = QtWidgets.QRadioButton(self.centroidGroup)
        self.ddButtonCalcOrigin_2.setGeometry(QtCore.QRect(20, 250, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ddButtonCalcOrigin_2.setFont(font)
        self.ddButtonCalcOrigin_2.setChecked(True)
        self.ddButtonCalcOrigin_2.setObjectName("ddButtonCalcOrigin_2")
        self.llButtonCalcOrigin_4 = QtWidgets.QRadioButton(self.centroidGroup)
        self.llButtonCalcOrigin_4.setGeometry(QtCore.QRect(20, 280, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.llButtonCalcOrigin_4.setFont(font)
        self.llButtonCalcOrigin_4.setObjectName("llButtonCalcOrigin_4")
        self.label = QtWidgets.QLabel(self.centroidGroup)
        self.label.setGeometry(QtCore.QRect(20, 220, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.westXEntry = QtWidgets.QLineEdit(self.centroidGroup)
        self.westXEntry.setGeometry(QtCore.QRect(15, 108, 103, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.westXEntry.setFont(font)
        self.westXEntry.setInputMask("")
        self.westXEntry.setText("")
        self.westXEntry.setMaxLength(32767)
        self.westXEntry.setObjectName("westXEntry")
        self.eastXEntry = QtWidgets.QLineEdit(self.centroidGroup)
        self.eastXEntry.setGeometry(QtCore.QRect(240, 108, 103, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.eastXEntry.setFont(font)
        self.eastXEntry.setInputMask("")
        self.eastXEntry.setMaxLength(32767)
        self.eastXEntry.setObjectName("eastXEntry")
        self.northYEntry = QtWidgets.QLineEdit(self.centroidGroup)
        self.northYEntry.setGeometry(QtCore.QRect(128, 60, 103, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.northYEntry.setFont(font)
        self.northYEntry.setAccessibleName("")
        self.northYEntry.setAutoFillBackground(False)
        self.northYEntry.setInputMask("")
        self.northYEntry.setText("")
        self.northYEntry.setMaxLength(32767)
        self.northYEntry.setCursorPosition(0)
        self.northYEntry.setObjectName("northYEntry")
        self.southYEntry = QtWidgets.QLineEdit(self.centroidGroup)
        self.southYEntry.setGeometry(QtCore.QRect(128, 160, 103, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.southYEntry.setFont(font)
        self.southYEntry.setInputMask("")
        self.southYEntry.setMaxLength(32767)
        self.southYEntry.setObjectName("southYEntry")
        self.label_3 = QtWidgets.QLabel(self.centroidGroup)
        self.label_3.setGeometry(QtCore.QRect(20, 88, 59, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centroidGroup)
        self.label_4.setGeometry(QtCore.QRect(240, 88, 59, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centroidGroup)
        self.label_5.setGeometry(QtCore.QRect(128, 40, 59, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centroidGroup)
        self.label_6.setGeometry(QtCore.QRect(128, 140, 59, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.originOutputBox = QtWidgets.QLineEdit(self.centroidGroup)
        self.originOutputBox.setGeometry(QtCore.QRect(20, 376, 321, 29))
        self.originOutputBox.setReadOnly(True)
        self.originOutputBox.setObjectName("originOutputBox")
        self.originGroup = QtWidgets.QGroupBox(self.gisCalc)
        self.originGroup.setGeometry(QtCore.QRect(410, 20, 361, 529))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.originGroup.setFont(font)
        self.originGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.originGroup.setTitle("")
        self.originGroup.setObjectName("originGroup")
        self.centroidCalcLabel_2 = QtWidgets.QLabel(self.originGroup)
        self.centroidCalcLabel_2.setGeometry(QtCore.QRect(20, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.centroidCalcLabel_2.setFont(font)
        self.centroidCalcLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.centroidCalcLabel_2.setObjectName("centroidCalcLabel_2")
        self.convCoordClear = QtWidgets.QPushButton(self.originGroup)
        self.convCoordClear.setEnabled(True)
        self.convCoordClear.setGeometry(QtCore.QRect(10, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.convCoordClear.setFont(font)
        self.convCoordClear.setObjectName("convCoordClear")
        self.convCoordCalc = QtWidgets.QPushButton(self.originGroup)
        self.convCoordCalc.setEnabled(True)
        self.convCoordCalc.setGeometry(QtCore.QRect(240, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.convCoordCalc.setFont(font)
        self.convCoordCalc.setObjectName("convCoordCalc")
        self.converterOutput = QtWidgets.QLineEdit(self.originGroup)
        self.converterOutput.setGeometry(QtCore.QRect(22, 376, 321, 29))
        self.converterOutput.setReadOnly(True)
        self.converterOutput.setObjectName("converterOutput")
        self.converCoordsEntry = QtWidgets.QLineEdit(self.originGroup)
        self.converCoordsEntry.setGeometry(QtCore.QRect(120, 108, 126, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.converCoordsEntry.setFont(font)
        self.converCoordsEntry.setInputMask("")
        self.converCoordsEntry.setMaxLength(32767)
        self.converCoordsEntry.setObjectName("converCoordsEntry")
        self.dmsToDD = QtWidgets.QRadioButton(self.originGroup)
        self.dmsToDD.setGeometry(QtCore.QRect(76, 56, 100, 20))
        self.dmsToDD.setObjectName("dmsToDD")
        self.DDToDMS = QtWidgets.QRadioButton(self.originGroup)
        self.DDToDMS.setGeometry(QtCore.QRect(192, 56, 100, 20))
        self.DDToDMS.setObjectName("DDToDMS")
        self.coordinatesResultsLabel = QtWidgets.QLabel(self.gisCalc)
        self.coordinatesResultsLabel.setGeometry(QtCore.QRect(430, 368, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.coordinatesResultsLabel.setFont(font)
        self.coordinatesResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coordinatesResultsLabel.setObjectName("coordinatesResultsLabel")
        self.originGroup.raise_()
        self.centroidGroup.raise_()
        self.coordinatesResultsLabel.raise_()
        self.tabContainer.addTab(self.gisCalc, "")
        self.catalogTiff = QtWidgets.QWidget()
        self.catalogTiff.setObjectName("catalogTiff")
        self.label_2 = QtWidgets.QLabel(self.catalogTiff)
        self.label_2.setGeometry(QtCore.QRect(12, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.catalogTiffBrowseButton = QtWidgets.QPushButton(self.catalogTiff)
        self.catalogTiffBrowseButton.setGeometry(QtCore.QRect(652, 26, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.catalogTiffBrowseButton.setFont(font)
        self.catalogTiffBrowseButton.setObjectName("catalogTiffBrowseButton")
        self.tiffCatalogOutputLabel = QtWidgets.QLabel(self.catalogTiff)
        self.tiffCatalogOutputLabel.setGeometry(QtCore.QRect(12, 78, 105, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.tiffCatalogOutputLabel.setFont(font)
        self.tiffCatalogOutputLabel.setObjectName("tiffCatalogOutputLabel")
        self.catalogTiffBrowseButton_2 = QtWidgets.QPushButton(self.catalogTiff)
        self.catalogTiffBrowseButton_2.setGeometry(QtCore.QRect(652, 72, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.catalogTiffBrowseButton_2.setFont(font)
        self.catalogTiffBrowseButton_2.setObjectName("catalogTiffBrowseButton_2")
        self.catalogTiffOutputWindow = QtWidgets.QTextEdit(self.catalogTiff)
        self.catalogTiffOutputWindow.setGeometry(QtCore.QRect(10, 192, 755, 325))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.catalogTiffOutputWindow.setFont(font)
        self.catalogTiffOutputWindow.setReadOnly(True)
        self.catalogTiffOutputWindow.setObjectName("catalogTiffOutputWindow")
        self.checkBox = QtWidgets.QCheckBox(self.catalogTiff)
        self.checkBox.setGeometry(QtCore.QRect(12, 124, 153, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.progressBar_2 = QtWidgets.QProgressBar(self.catalogTiff)
        self.progressBar_2.setGeometry(QtCore.QRect(16, 158, 745, 23))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.geoTiffDir1 = QtWidgets.QLineEdit(self.catalogTiff)
        self.geoTiffDir1.setGeometry(QtCore.QRect(140, 28, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.geoTiffDir1.setFont(font)
        self.geoTiffDir1.setObjectName("geoTiffDir1")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.catalogTiff)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 76, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.catalogTiffProcess = QtWidgets.QPushButton(self.catalogTiff)
        self.catalogTiffProcess.setGeometry(QtCore.QRect(652, 118, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.catalogTiffProcess.setFont(font)
        self.catalogTiffProcess.setObjectName("catalogTiffProcess")
        self.tabContainer.addTab(self.catalogTiff, "")
        self.copyTiffs = QtWidgets.QWidget()
        self.copyTiffs.setObjectName("copyTiffs")
        self.label_9 = QtWidgets.QLabel(self.copyTiffs)
        self.label_9.setGeometry(QtCore.QRect(12, 32, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.copyTiffs)
        self.label_10.setGeometry(QtCore.QRect(12, 64, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.copyTiffs)
        self.label_11.setGeometry(QtCore.QRect(12, 96, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.TiffDirectory = QtWidgets.QLineEdit(self.copyTiffs)
        self.TiffDirectory.setGeometry(QtCore.QRect(188, 32, 433, 21))
        self.TiffDirectory.setObjectName("TiffDirectory")
        self.intersectingShapefileEdit = QtWidgets.QLineEdit(self.copyTiffs)
        self.intersectingShapefileEdit.setGeometry(QtCore.QRect(188, 64, 433, 21))
        self.intersectingShapefileEdit.setObjectName("intersectingShapefileEdit")
        self.geoTiffOutputDirEdit = QtWidgets.QLineEdit(self.copyTiffs)
        self.geoTiffOutputDirEdit.setGeometry(QtCore.QRect(188, 96, 433, 21))
        self.geoTiffOutputDirEdit.setObjectName("geoTiffOutputDirEdit")
        self.BrowseForTifDir = QtWidgets.QPushButton(self.copyTiffs)
        self.BrowseForTifDir.setGeometry(QtCore.QRect(642, 28, 113, 32))
        self.BrowseForTifDir.setObjectName("BrowseForTifDir")
        self.BrowseForIntShape = QtWidgets.QPushButton(self.copyTiffs)
        self.BrowseForIntShape.setGeometry(QtCore.QRect(642, 60, 113, 32))
        self.BrowseForIntShape.setObjectName("BrowseForIntShape")
        self.BrowseForGeoTiffOutputDir = QtWidgets.QPushButton(self.copyTiffs)
        self.BrowseForGeoTiffOutputDir.setGeometry(QtCore.QRect(642, 92, 113, 32))
        self.BrowseForGeoTiffOutputDir.setObjectName("BrowseForGeoTiffOutputDir")
        self.checkBox_2 = QtWidgets.QCheckBox(self.copyTiffs)
        self.checkBox_2.setGeometry(QtCore.QRect(12, 124, 153, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.catalogTiffOutputWindow_2 = QtWidgets.QTextEdit(self.copyTiffs)
        self.catalogTiffOutputWindow_2.setGeometry(QtCore.QRect(10, 192, 755, 325))
        self.catalogTiffOutputWindow_2.setReadOnly(True)
        self.catalogTiffOutputWindow_2.setObjectName("catalogTiffOutputWindow_2")
        self.progressBar = QtWidgets.QProgressBar(self.copyTiffs)
        self.progressBar.setGeometry(QtCore.QRect(16, 158, 745, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.CopyTiffProcess = QtWidgets.QPushButton(self.copyTiffs)
        self.CopyTiffProcess.setGeometry(QtCore.QRect(642, 124, 113, 32))
        self.CopyTiffProcess.setObjectName("CopyTiffProcess")
        self.tabContainer.addTab(self.copyTiffs, "")
        self.qkShp = QtWidgets.QWidget()
        self.qkShp.setObjectName("qkShp")
        self.shapeViewWindow = QtWidgets.QGraphicsView(self.qkShp)
        self.shapeViewWindow.setGeometry(QtCore.QRect(6, 54, 763, 433))
        self.shapeViewWindow.setObjectName("shapeViewWindow")
        self.label_13 = QtWidgets.QLabel(self.qkShp)
        self.label_13.setGeometry(QtCore.QRect(22, 20, 73, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.shapefileViewPath = QtWidgets.QLineEdit(self.qkShp)
        self.shapefileViewPath.setGeometry(QtCore.QRect(188, 18, 433, 21))
        self.shapefileViewPath.setObjectName("shapefileViewPath")
        self.shapefileViewBrowseButton = QtWidgets.QPushButton(self.qkShp)
        self.shapefileViewBrowseButton.setGeometry(QtCore.QRect(642, 14, 113, 32))
        self.shapefileViewBrowseButton.setObjectName("shapefileViewBrowseButton")
        self.shapefileViewClear = QtWidgets.QPushButton(self.qkShp)
        self.shapefileViewClear.setGeometry(QtCore.QRect(20, 490, 113, 32))
        self.shapefileViewClear.setObjectName("shapefileViewClear")
        self.shapefileViewGo = QtWidgets.QPushButton(self.qkShp)
        self.shapefileViewGo.setGeometry(QtCore.QRect(640, 490, 113, 32))
        self.shapefileViewGo.setObjectName("shapefileViewGo")
        self.tabContainer.addTab(self.qkShp, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GIS Helper"))
        self.centroidCalcLabel.setText(_translate("MainWindow", "Calculate Origin"))
        self.originClearButton.setText(_translate("MainWindow", "Clear"))
        self.originCalculateButton.setText(_translate("MainWindow", "Calculate"))
        self.originResultsLabel.setText(_translate("MainWindow", "Origin"))
        self.ddButtonCalcOrigin_2.setText(_translate("MainWindow", "Decimal Degrees"))
        self.llButtonCalcOrigin_4.setText(_translate("MainWindow", "Lat/Lon"))
        self.label.setText(_translate("MainWindow", "Coordinate System"))
        self.westXEntry.setPlaceholderText(_translate("MainWindow", "East X"))
        self.eastXEntry.setPlaceholderText(_translate("MainWindow", "West X"))
        self.northYEntry.setPlaceholderText(_translate("MainWindow", "North Y"))
        self.southYEntry.setPlaceholderText(_translate("MainWindow", "South Y"))
        self.label_3.setText(_translate("MainWindow", "West X"))
        self.label_4.setText(_translate("MainWindow", "East X"))
        self.label_5.setText(_translate("MainWindow", "North Y"))
        self.label_6.setText(_translate("MainWindow", "South Y"))
        self.centroidCalcLabel_2.setText(_translate("MainWindow", "Convert Coordinates"))
        self.convCoordClear.setText(_translate("MainWindow", "Clear"))
        self.convCoordCalc.setText(_translate("MainWindow", "Calculate"))
        self.converCoordsEntry.setPlaceholderText(_translate("MainWindow", "Input Coordinates"))
        self.dmsToDD.setText(_translate("MainWindow", "DMS to DD"))
        self.DDToDMS.setText(_translate("MainWindow", "DD to DMS"))
        self.coordinatesResultsLabel.setText(_translate("MainWindow", "Converted Coordinates"))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.gisCalc), _translate("MainWindow", "GIS Calculator"))
        self.label_2.setText(_translate("MainWindow", "Geotiff Directory: "))
        self.catalogTiffBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.tiffCatalogOutputLabel.setText(_translate("MainWindow", "Output Directory: "))
        self.catalogTiffBrowseButton_2.setText(_translate("MainWindow", "Browse"))
        self.checkBox.setText(_translate("MainWindow", "Fan out by resolution"))
        self.catalogTiffProcess.setText(_translate("MainWindow", "Process"))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.catalogTiff), _translate("MainWindow", "Catalog Tiffs"))
        self.label_9.setText(_translate("MainWindow", "Tif Directory"))
        self.label_10.setText(_translate("MainWindow", "Intersecting Shapefile: "))
        self.label_11.setText(_translate("MainWindow", "Geotiff Output Directory: "))
        self.BrowseForTifDir.setText(_translate("MainWindow", "Browse"))
        self.BrowseForIntShape.setText(_translate("MainWindow", "Browse"))
        self.BrowseForGeoTiffOutputDir.setText(_translate("MainWindow", "Browse"))
        self.checkBox_2.setText(_translate("MainWindow", "Fan out by resolution"))
        self.CopyTiffProcess.setText(_translate("MainWindow", "Process"))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.copyTiffs), _translate("MainWindow", "Copy Tiffs"))
        self.label_13.setText(_translate("MainWindow", "Shapefile: "))
        self.shapefileViewBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.shapefileViewClear.setText(_translate("MainWindow", "Clear"))
        self.shapefileViewGo.setText(_translate("MainWindow", "Open Shape"))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.qkShp), _translate("MainWindow", "Shapefile QuickView"))
