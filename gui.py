# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gisHelperGui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 611)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabContainer = QtWidgets.QTabWidget(self.centralwidget)
        self.tabContainer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabContainer.sizePolicy().hasHeightForWidth())
        self.tabContainer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.tabContainer.setFont(font)
        self.tabContainer.setAcceptDrops(False)
        self.tabContainer.setObjectName("tabContainer")
        self.gisCalc = QtWidgets.QWidget()
        self.gisCalc.setObjectName("gisCalc")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gisCalc)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.centroidGroup = QtWidgets.QGroupBox(self.gisCalc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.centroidGroup.setFont(font)
        self.centroidGroup.setTitle("")
        self.centroidGroup.setObjectName("centroidGroup")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centroidGroup)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 8, 1, 1, 1)
        self.eastXEntry = QtWidgets.QLineEdit(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.eastXEntry.setFont(font)
        self.eastXEntry.setInputMask("")
        self.eastXEntry.setMaxLength(32767)
        self.eastXEntry.setObjectName("eastXEntry")
        self.gridLayout_7.addWidget(self.eastXEntry, 4, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.centroidGroup)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.llButtonCalcOrigin_4 = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.llButtonCalcOrigin_4.setFont(font)
        self.llButtonCalcOrigin_4.setObjectName("llButtonCalcOrigin_4")
        self.gridLayout_6.addWidget(self.llButtonCalcOrigin_4, 0, 0, 1, 1)
        self.ddButtonCalcOrigin_2 = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ddButtonCalcOrigin_2.setFont(font)
        self.ddButtonCalcOrigin_2.setChecked(True)
        self.ddButtonCalcOrigin_2.setObjectName("ddButtonCalcOrigin_2")
        self.gridLayout_6.addWidget(self.ddButtonCalcOrigin_2, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame, 13, 1, 1, 1)
        self.northYEntry = QtWidgets.QLineEdit(self.centroidGroup)
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
        self.gridLayout_7.addWidget(self.northYEntry, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 5, 1, 1, 1)
        self.centroidCalcLabel = QtWidgets.QLabel(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.centroidCalcLabel.setFont(font)
        self.centroidCalcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.centroidCalcLabel.setObjectName("centroidCalcLabel")
        self.gridLayout_7.addWidget(self.centroidCalcLabel, 0, 0, 1, 3)
        self.originClearButton = QtWidgets.QPushButton(self.centroidGroup)
        self.originClearButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.originClearButton.setFont(font)
        self.originClearButton.setObjectName("originClearButton")
        self.gridLayout_7.addWidget(self.originClearButton, 17, 0, 1, 1)
        self.southYEntry = QtWidgets.QLineEdit(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.southYEntry.setFont(font)
        self.southYEntry.setInputMask("")
        self.southYEntry.setMaxLength(32767)
        self.southYEntry.setObjectName("southYEntry")
        self.gridLayout_7.addWidget(self.southYEntry, 6, 1, 1, 1)
        self.originCalculateButton = QtWidgets.QPushButton(self.centroidGroup)
        self.originCalculateButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.originCalculateButton.setFont(font)
        self.originCalculateButton.setObjectName("originCalculateButton")
        self.gridLayout_7.addWidget(self.originCalculateButton, 17, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 1, 1, 1, 1)
        self.westXEntry = QtWidgets.QLineEdit(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.westXEntry.setFont(font)
        self.westXEntry.setInputMask("")
        self.westXEntry.setText("")
        self.westXEntry.setMaxLength(32767)
        self.westXEntry.setObjectName("westXEntry")
        self.gridLayout_7.addWidget(self.westXEntry, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centroidGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 3, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centroidGroup)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.originResultsLabel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.originResultsLabel.setFont(font)
        self.originResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.originResultsLabel.setObjectName("originResultsLabel")
        self.gridLayout_9.addWidget(self.originResultsLabel, 0, 0, 1, 1)
        self.originOutputBox = QtWidgets.QLineEdit(self.frame_3)
        self.originOutputBox.setReadOnly(True)
        self.originOutputBox.setObjectName("originOutputBox")
        self.gridLayout_9.addWidget(self.originOutputBox, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 14, 0, 1, 3)
        self.horizontalLayout.addWidget(self.centroidGroup)
        self.originGroup = QtWidgets.QGroupBox(self.gisCalc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.originGroup.sizePolicy().hasHeightForWidth())
        self.originGroup.setSizePolicy(sizePolicy)
        self.originGroup.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.originGroup.setFont(font)
        self.originGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.originGroup.setTitle("")
        self.originGroup.setObjectName("originGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.originGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.DDToDMS = QtWidgets.QRadioButton(self.originGroup)
        self.DDToDMS.setObjectName("DDToDMS")
        self.gridLayout_5.addWidget(self.DDToDMS, 1, 1, 1, 1)
        self.converCoordsEntry = QtWidgets.QLineEdit(self.originGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.converCoordsEntry.setFont(font)
        self.converCoordsEntry.setInputMask("")
        self.converCoordsEntry.setMaxLength(32767)
        self.converCoordsEntry.setObjectName("converCoordsEntry")
        self.gridLayout_5.addWidget(self.converCoordsEntry, 2, 0, 1, 2)
        self.centroidCalcLabel_2 = QtWidgets.QLabel(self.originGroup)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.centroidCalcLabel_2.setFont(font)
        self.centroidCalcLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.centroidCalcLabel_2.setObjectName("centroidCalcLabel_2")
        self.gridLayout_5.addWidget(self.centroidCalcLabel_2, 0, 0, 1, 2)
        self.convCoordClear = QtWidgets.QPushButton(self.originGroup)
        self.convCoordClear.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.convCoordClear.setFont(font)
        self.convCoordClear.setObjectName("convCoordClear")
        self.gridLayout_5.addWidget(self.convCoordClear, 6, 0, 1, 1)
        self.dmsToDD = QtWidgets.QRadioButton(self.originGroup)
        self.dmsToDD.setObjectName("dmsToDD")
        self.gridLayout_5.addWidget(self.dmsToDD, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.originGroup)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.converterOutput = QtWidgets.QLineEdit(self.frame_2)
        self.converterOutput.setReadOnly(True)
        self.converterOutput.setObjectName("converterOutput")
        self.gridLayout_8.addWidget(self.converterOutput, 2, 0, 1, 1)
        self.coordinatesResultsLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.coordinatesResultsLabel.setFont(font)
        self.coordinatesResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coordinatesResultsLabel.setObjectName("coordinatesResultsLabel")
        self.gridLayout_8.addWidget(self.coordinatesResultsLabel, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 3, 0, 1, 2)
        self.convCoordCalc = QtWidgets.QPushButton(self.originGroup)
        self.convCoordCalc.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.convCoordCalc.setFont(font)
        self.convCoordCalc.setObjectName("convCoordCalc")
        self.gridLayout_5.addWidget(self.convCoordCalc, 6, 1, 1, 1)
        self.horizontalLayout.addWidget(self.originGroup)
        self.tabContainer.addTab(self.gisCalc, "")
        self.catalogTiff = QtWidgets.QWidget()
        self.catalogTiff.setObjectName("catalogTiff")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.catalogTiff)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TiffCatalogOutputEdit = QtWidgets.QLineEdit(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.TiffCatalogOutputEdit.setFont(font)
        self.TiffCatalogOutputEdit.setObjectName("TiffCatalogOutputEdit")
        self.gridLayout_3.addWidget(self.TiffCatalogOutputEdit, 1, 2, 1, 1)
        self.catalogTiffOutputWindow = QtWidgets.QTableWidget(self.catalogTiff)
        self.catalogTiffOutputWindow.setObjectName("catalogTiffOutputWindow")
        self.catalogTiffOutputWindow.setColumnCount(0)
        self.catalogTiffOutputWindow.setRowCount(0)
        self.gridLayout_3.addWidget(self.catalogTiffOutputWindow, 8, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.catalogTiffBOutputrowseButton = QtWidgets.QPushButton(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.catalogTiffBOutputrowseButton.setFont(font)
        self.catalogTiffBOutputrowseButton.setObjectName("catalogTiffBOutputrowseButton")
        self.gridLayout_3.addWidget(self.catalogTiffBOutputrowseButton, 1, 3, 1, 1)
        self.catalogTiffProcess = QtWidgets.QPushButton(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.catalogTiffProcess.setFont(font)
        self.catalogTiffProcess.setObjectName("catalogTiffProcess")
        self.gridLayout_3.addWidget(self.catalogTiffProcess, 3, 3, 1, 1)
        self.geoTiffDir1 = QtWidgets.QLineEdit(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.geoTiffDir1.setFont(font)
        self.geoTiffDir1.setObjectName("geoTiffDir1")
        self.gridLayout_3.addWidget(self.geoTiffDir1, 0, 2, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_3.addWidget(self.progressBar_2, 7, 0, 1, 4)
        self.catalogTiffBrowseButton = QtWidgets.QPushButton(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.catalogTiffBrowseButton.setFont(font)
        self.catalogTiffBrowseButton.setObjectName("catalogTiffBrowseButton")
        self.gridLayout_3.addWidget(self.catalogTiffBrowseButton, 0, 3, 1, 1)
        self.tiffCatalogOutputLabel = QtWidgets.QLabel(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.tiffCatalogOutputLabel.setFont(font)
        self.tiffCatalogOutputLabel.setObjectName("tiffCatalogOutputLabel")
        self.gridLayout_3.addWidget(self.tiffCatalogOutputLabel, 1, 0, 1, 1)
        self.FanOutByRes = QtWidgets.QCheckBox(self.catalogTiff)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.FanOutByRes.setFont(font)
        self.FanOutByRes.setObjectName("FanOutByRes")
        self.gridLayout_3.addWidget(self.FanOutByRes, 3, 0, 1, 1)
        self.ignoreNullValuesCheckbox = QtWidgets.QCheckBox(self.catalogTiff)
        self.ignoreNullValuesCheckbox.setObjectName("ignoreNullValuesCheckbox")
        self.gridLayout_3.addWidget(self.ignoreNullValuesCheckbox, 3, 2, 1, 1)
        self.tabContainer.addTab(self.catalogTiff, "")
        self.copyTiffs = QtWidgets.QWidget()
        self.copyTiffs.setObjectName("copyTiffs")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.copyTiffs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TiffDirectory = QtWidgets.QLineEdit(self.copyTiffs)
        self.TiffDirectory.setObjectName("TiffDirectory")
        self.gridLayout_2.addWidget(self.TiffDirectory, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.copyTiffs)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.BrowseForGeoTiffOutputDir = QtWidgets.QPushButton(self.copyTiffs)
        self.BrowseForGeoTiffOutputDir.setObjectName("BrowseForGeoTiffOutputDir")
        self.gridLayout_2.addWidget(self.BrowseForGeoTiffOutputDir, 2, 2, 1, 1)
        self.BrowseForTifDir = QtWidgets.QPushButton(self.copyTiffs)
        self.BrowseForTifDir.setObjectName("BrowseForTifDir")
        self.gridLayout_2.addWidget(self.BrowseForTifDir, 0, 2, 1, 1)
        self.copyTiffOutputWindow = QtWidgets.QTableWidget(self.copyTiffs)
        self.copyTiffOutputWindow.setObjectName("copyTiffOutputWindow")
        self.copyTiffOutputWindow.setColumnCount(0)
        self.copyTiffOutputWindow.setRowCount(0)
        self.gridLayout_2.addWidget(self.copyTiffOutputWindow, 5, 0, 1, 3)
        self.CopyFanoutByResolution = QtWidgets.QCheckBox(self.copyTiffs)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.CopyFanoutByResolution.setFont(font)
        self.CopyFanoutByResolution.setObjectName("CopyFanoutByResolution")
        self.gridLayout_2.addWidget(self.CopyFanoutByResolution, 3, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.copyTiffs)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 4, 0, 1, 3)
        self.intersectingShapefileEdit = QtWidgets.QLineEdit(self.copyTiffs)
        self.intersectingShapefileEdit.setObjectName("intersectingShapefileEdit")
        self.gridLayout_2.addWidget(self.intersectingShapefileEdit, 1, 1, 1, 1)
        self.CopyTiffProcess = QtWidgets.QPushButton(self.copyTiffs)
        self.CopyTiffProcess.setObjectName("CopyTiffProcess")
        self.gridLayout_2.addWidget(self.CopyTiffProcess, 3, 2, 1, 1)
        self.BrowseForIntShape = QtWidgets.QPushButton(self.copyTiffs)
        self.BrowseForIntShape.setObjectName("BrowseForIntShape")
        self.gridLayout_2.addWidget(self.BrowseForIntShape, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.copyTiffs)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.copyTiffs)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.geoTiffOutputDirEdit = QtWidgets.QLineEdit(self.copyTiffs)
        self.geoTiffOutputDirEdit.setObjectName("geoTiffOutputDirEdit")
        self.gridLayout_2.addWidget(self.geoTiffOutputDirEdit, 2, 1, 1, 1)
        self.tabContainer.addTab(self.copyTiffs, "")
        self.qkShp = QtWidgets.QWidget()
        self.qkShp.setObjectName("qkShp")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.qkShp)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_13 = QtWidgets.QLabel(self.qkShp)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.shapefileViewPath = QtWidgets.QLineEdit(self.qkShp)
        self.shapefileViewPath.setObjectName("shapefileViewPath")
        self.gridLayout_4.addWidget(self.shapefileViewPath, 0, 1, 1, 1)
        self.shapefileViewBrowseButton = QtWidgets.QPushButton(self.qkShp)
        self.shapefileViewBrowseButton.setObjectName("shapefileViewBrowseButton")
        self.gridLayout_4.addWidget(self.shapefileViewBrowseButton, 0, 2, 1, 1)
        self.shapeViewWindow = QtWidgets.QGraphicsView(self.qkShp)
        self.shapeViewWindow.setObjectName("shapeViewWindow")
        self.gridLayout_4.addWidget(self.shapeViewWindow, 1, 0, 1, 3)
        self.shapefileViewClear = QtWidgets.QPushButton(self.qkShp)
        self.shapefileViewClear.setObjectName("shapefileViewClear")
        self.gridLayout_4.addWidget(self.shapefileViewClear, 2, 0, 1, 1)
        self.shapefileViewGo = QtWidgets.QPushButton(self.qkShp)
        self.shapefileViewGo.setObjectName("shapefileViewGo")
        self.gridLayout_4.addWidget(self.shapefileViewGo, 2, 2, 1, 1)
        self.tabContainer.addTab(self.qkShp, "")
        self.gridLayout.addWidget(self.tabContainer, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 22))
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
        self.label.setText(_translate("MainWindow", "Coordinate System"))
        self.eastXEntry.setPlaceholderText(_translate("MainWindow", "West X"))
        self.llButtonCalcOrigin_4.setText(_translate("MainWindow", "Lat/Lon"))
        self.ddButtonCalcOrigin_2.setText(_translate("MainWindow", "Decimal Degrees"))
        self.northYEntry.setPlaceholderText(_translate("MainWindow", "North Y"))
        self.label_6.setText(_translate("MainWindow", "South Y"))
        self.centroidCalcLabel.setText(_translate("MainWindow", "Calculate Origin"))
        self.originClearButton.setText(_translate("MainWindow", "Clear"))
        self.southYEntry.setPlaceholderText(_translate("MainWindow", "South Y"))
        self.originCalculateButton.setText(_translate("MainWindow", "Calculate"))
        self.label_5.setText(_translate("MainWindow", "North Y"))
        self.westXEntry.setPlaceholderText(_translate("MainWindow", "East X"))
        self.label_3.setText(_translate("MainWindow", "West X"))
        self.label_4.setText(_translate("MainWindow", "East X"))
        self.originResultsLabel.setText(_translate("MainWindow", "Origin"))
        self.DDToDMS.setText(_translate("MainWindow", "DD to DMS"))
        self.converCoordsEntry.setPlaceholderText(_translate("MainWindow", "Input Coordinates"))
        self.centroidCalcLabel_2.setText(_translate("MainWindow", "Convert Coordinates"))
        self.convCoordClear.setText(_translate("MainWindow", "Clear"))
        self.dmsToDD.setText(_translate("MainWindow", "DMS to DD"))
        self.coordinatesResultsLabel.setText(_translate("MainWindow", "Converted Coordinates"))
        self.convCoordCalc.setText(_translate("MainWindow", "Calculate"))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.gisCalc), _translate("MainWindow", "GIS Calculator"))
        self.label_2.setText(_translate("MainWindow", "Geotiff Directory: "))
        self.catalogTiffBOutputrowseButton.setText(_translate("MainWindow", "Browse"))
        self.catalogTiffProcess.setText(_translate("MainWindow", "Process"))
        self.catalogTiffBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.tiffCatalogOutputLabel.setText(_translate("MainWindow", "Output Directory: "))
        self.FanOutByRes.setText(_translate("MainWindow", "Fan out by resolution"))
        self.ignoreNullValuesCheckbox.setText(_translate("MainWindow", "Ignore Null Values"))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.catalogTiff), _translate("MainWindow", "Catalog Tiffs"))
        self.label_10.setText(_translate("MainWindow", "Intersecting Shapefile: "))
        self.BrowseForGeoTiffOutputDir.setText(_translate("MainWindow", "Browse"))
        self.BrowseForTifDir.setText(_translate("MainWindow", "Browse"))
        self.CopyFanoutByResolution.setText(_translate("MainWindow", "Fan out by resolution"))
        self.CopyTiffProcess.setText(_translate("MainWindow", "Process"))
        self.BrowseForIntShape.setText(_translate("MainWindow", "Browse"))
        self.label_9.setText(_translate("MainWindow", "Tif Directory"))
        self.label_11.setText(_translate("MainWindow", "Geotiff Output Directory: "))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.copyTiffs), _translate("MainWindow", "Copy Tiffs"))
        self.label_13.setText(_translate("MainWindow", "Shapefile: "))
        self.shapefileViewBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.shapefileViewClear.setText(_translate("MainWindow", "Clear"))
        self.shapefileViewGo.setText(_translate("MainWindow", "Open Shape"))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.qkShp), _translate("MainWindow", "Shapefile QuickView"))
