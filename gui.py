# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gisHelperGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabContainer = QtGui.QTabWidget(self.centralwidget)
        self.tabContainer.setEnabled(True)
        self.tabContainer.setGeometry(QtCore.QRect(10, 6, 781, 569))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tabContainer.setFont(font)
        self.tabContainer.setAcceptDrops(False)
        self.tabContainer.setObjectName(_fromUtf8("tabContainer"))
        self.gisCalc = QtGui.QWidget()
        self.gisCalc.setObjectName(_fromUtf8("gisCalc"))
        self.centroidGroup = QtGui.QGroupBox(self.gisCalc)
        self.centroidGroup.setGeometry(QtCore.QRect(4, 20, 361, 529))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.centroidGroup.setFont(font)
        self.centroidGroup.setTitle(_fromUtf8(""))
        self.centroidGroup.setObjectName(_fromUtf8("centroidGroup"))
        self.centroidCalcLabel = QtGui.QLabel(self.centroidGroup)
        self.centroidCalcLabel.setGeometry(QtCore.QRect(20, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.centroidCalcLabel.setFont(font)
        self.centroidCalcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.centroidCalcLabel.setObjectName(_fromUtf8("centroidCalcLabel"))
        self.originClearButton = QtGui.QPushButton(self.centroidGroup)
        self.originClearButton.setEnabled(True)
        self.originClearButton.setGeometry(QtCore.QRect(10, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.originClearButton.setFont(font)
        self.originClearButton.setObjectName(_fromUtf8("originClearButton"))
        self.originCalculateButton = QtGui.QPushButton(self.centroidGroup)
        self.originCalculateButton.setEnabled(True)
        self.originCalculateButton.setGeometry(QtCore.QRect(240, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.originCalculateButton.setFont(font)
        self.originCalculateButton.setObjectName(_fromUtf8("originCalculateButton"))
        self.originResultsLabel = QtGui.QLabel(self.centroidGroup)
        self.originResultsLabel.setGeometry(QtCore.QRect(20, 350, 321, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.originResultsLabel.setFont(font)
        self.originResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.originResultsLabel.setObjectName(_fromUtf8("originResultsLabel"))
        self.ddButtonCalcOrigin_2 = QtGui.QRadioButton(self.centroidGroup)
        self.ddButtonCalcOrigin_2.setGeometry(QtCore.QRect(20, 250, 131, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.ddButtonCalcOrigin_2.setFont(font)
        self.ddButtonCalcOrigin_2.setChecked(True)
        self.ddButtonCalcOrigin_2.setObjectName(_fromUtf8("ddButtonCalcOrigin_2"))
        self.llButtonCalcOrigin_4 = QtGui.QRadioButton(self.centroidGroup)
        self.llButtonCalcOrigin_4.setGeometry(QtCore.QRect(20, 280, 131, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.llButtonCalcOrigin_4.setFont(font)
        self.llButtonCalcOrigin_4.setObjectName(_fromUtf8("llButtonCalcOrigin_4"))
        self.label = QtGui.QLabel(self.centroidGroup)
        self.label.setGeometry(QtCore.QRect(20, 220, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.westXEntry = QtGui.QLineEdit(self.centroidGroup)
        self.westXEntry.setGeometry(QtCore.QRect(15, 108, 103, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.westXEntry.setFont(font)
        self.westXEntry.setInputMask(_fromUtf8(""))
        self.westXEntry.setText(_fromUtf8(""))
        self.westXEntry.setMaxLength(32767)
        # self.westXEntry.setClearButtonEnabled(False)
        self.westXEntry.setObjectName(_fromUtf8("westXEntry"))
        self.eastXEntry = QtGui.QLineEdit(self.centroidGroup)
        self.eastXEntry.setGeometry(QtCore.QRect(240, 108, 103, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.eastXEntry.setFont(font)
        self.eastXEntry.setInputMask(_fromUtf8(""))
        self.eastXEntry.setMaxLength(32767)
        #self.eastXEntry.setClearButtonEnabled(False)
        self.eastXEntry.setObjectName(_fromUtf8("eastXEntry"))
        self.northYEntry = QtGui.QLineEdit(self.centroidGroup)
        self.northYEntry.setGeometry(QtCore.QRect(128, 60, 103, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.northYEntry.setFont(font)
        self.northYEntry.setAccessibleName(_fromUtf8(""))
        self.northYEntry.setAutoFillBackground(False)
        self.northYEntry.setInputMask(_fromUtf8(""))
        self.northYEntry.setText(_fromUtf8(""))
        self.northYEntry.setMaxLength(32767)
        self.northYEntry.setCursorPosition(0)
        #self.northYEntry.setClearButtonEnabled(False)
        self.northYEntry.setObjectName(_fromUtf8("northYEntry"))
        self.southYEntry = QtGui.QLineEdit(self.centroidGroup)
        self.southYEntry.setGeometry(QtCore.QRect(128, 160, 103, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.southYEntry.setFont(font)
        self.southYEntry.setInputMask(_fromUtf8(""))
        self.southYEntry.setMaxLength(32767)
        #self.southYEntry.setClearButtonEnabled(False)
        self.southYEntry.setObjectName(_fromUtf8("southYEntry"))
        self.label_3 = QtGui.QLabel(self.centroidGroup)
        self.label_3.setGeometry(QtCore.QRect(20, 88, 59, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centroidGroup)
        self.label_4.setGeometry(QtCore.QRect(240, 88, 59, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centroidGroup)
        self.label_5.setGeometry(QtCore.QRect(128, 40, 59, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centroidGroup)
        self.label_6.setGeometry(QtCore.QRect(128, 140, 59, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.originOutputBox = QtGui.QLineEdit(self.centroidGroup)
        self.originOutputBox.setGeometry(QtCore.QRect(20, 376, 321, 29))
        self.originOutputBox.setReadOnly(True)
        self.originOutputBox.setObjectName(_fromUtf8("originOutputBox"))
        self.originGroup = QtGui.QGroupBox(self.gisCalc)
        self.originGroup.setGeometry(QtCore.QRect(410, 20, 361, 529))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.originGroup.setFont(font)
        self.originGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.originGroup.setTitle(_fromUtf8(""))
        self.originGroup.setObjectName(_fromUtf8("originGroup"))
        self.centroidCalcLabel_2 = QtGui.QLabel(self.originGroup)
        self.centroidCalcLabel_2.setGeometry(QtCore.QRect(20, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.centroidCalcLabel_2.setFont(font)
        self.centroidCalcLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.centroidCalcLabel_2.setObjectName(_fromUtf8("centroidCalcLabel_2"))
        self.convCoordClear = QtGui.QPushButton(self.originGroup)
        self.convCoordClear.setEnabled(True)
        self.convCoordClear.setGeometry(QtCore.QRect(10, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.convCoordClear.setFont(font)
        self.convCoordClear.setObjectName(_fromUtf8("convCoordClear"))
        self.convCoordCalc = QtGui.QPushButton(self.originGroup)
        self.convCoordCalc.setEnabled(True)
        self.convCoordCalc.setGeometry(QtCore.QRect(240, 470, 113, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.convCoordCalc.setFont(font)
        self.convCoordCalc.setObjectName(_fromUtf8("convCoordCalc"))
        self.convCombo = QtGui.QComboBox(self.originGroup)
        self.convCombo.setGeometry(QtCore.QRect(40, 48, 291, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.convCombo.setFont(font)
        self.convCombo.setObjectName(_fromUtf8("convCombo"))
        self.convCombo.addItem(_fromUtf8(""))
        self.convCombo.addItem(_fromUtf8(""))
        self.converterOutput = QtGui.QLineEdit(self.originGroup)
        self.converterOutput.setGeometry(QtCore.QRect(22, 376, 321, 29))
        self.converterOutput.setReadOnly(True)
        self.converterOutput.setObjectName(_fromUtf8("converterOutput"))
        self.converCoordsEntry = QtGui.QLineEdit(self.originGroup)
        self.converCoordsEntry.setGeometry(QtCore.QRect(120, 108, 126, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.converCoordsEntry.setFont(font)
        self.converCoordsEntry.setInputMask(_fromUtf8(""))
        self.converCoordsEntry.setMaxLength(32767)
        #self.converCoordsEntry.setClearButtonEnabled(False)
        self.converCoordsEntry.setObjectName(_fromUtf8("converCoordsEntry"))
        self.coordinatesResultsLabel = QtGui.QLabel(self.gisCalc)
        self.coordinatesResultsLabel.setGeometry(QtCore.QRect(430, 368, 321, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.coordinatesResultsLabel.setFont(font)
        self.coordinatesResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coordinatesResultsLabel.setObjectName(_fromUtf8("coordinatesResultsLabel"))
        self.originGroup.raise_()
        self.centroidGroup.raise_()
        self.coordinatesResultsLabel.raise_()
        self.tabContainer.addTab(self.gisCalc, _fromUtf8(""))
        self.catalogTiff = QtGui.QWidget()
        self.catalogTiff.setObjectName(_fromUtf8("catalogTiff"))
        self.label_2 = QtGui.QLabel(self.catalogTiff)
        self.label_2.setGeometry(QtCore.QRect(12, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.catalogTiffBrowseButton = QtGui.QPushButton(self.catalogTiff)
        self.catalogTiffBrowseButton.setGeometry(QtCore.QRect(652, 26, 113, 32))
        self.catalogTiffBrowseButton.setObjectName(_fromUtf8("catalogTiffBrowseButton"))
        self.tiffCatalogOutputLabel = QtGui.QLabel(self.catalogTiff)
        self.tiffCatalogOutputLabel.setGeometry(QtCore.QRect(12, 78, 105, 16))
        self.tiffCatalogOutputLabel.setObjectName(_fromUtf8("tiffCatalogOutputLabel"))
        self.catalogTiffBrowseButton_2 = QtGui.QPushButton(self.catalogTiff)
        self.catalogTiffBrowseButton_2.setGeometry(QtCore.QRect(652, 72, 113, 32))
        self.catalogTiffBrowseButton_2.setObjectName(_fromUtf8("catalogTiffBrowseButton_2"))
        self.catalogTiffOutputWindow = QtGui.QTextEdit(self.catalogTiff)
        self.catalogTiffOutputWindow.setGeometry(QtCore.QRect(10, 192, 755, 325))
        self.catalogTiffOutputWindow.setReadOnly(True)
        self.catalogTiffOutputWindow.setObjectName(_fromUtf8("catalogTiffOutputWindow"))
        self.checkBox = QtGui.QCheckBox(self.catalogTiff)
        self.checkBox.setGeometry(QtCore.QRect(12, 124, 153, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.progressBar_2 = QtGui.QProgressBar(self.catalogTiff)
        self.progressBar_2.setGeometry(QtCore.QRect(16, 158, 745, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.lineEdit_4 = QtGui.QLineEdit(self.catalogTiff)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 28, 481, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.catalogTiff)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 76, 481, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.tabContainer.addTab(self.catalogTiff, _fromUtf8(""))
        self.copyTiffs = QtGui.QWidget()
        self.copyTiffs.setObjectName(_fromUtf8("copyTiffs"))
        self.label_9 = QtGui.QLabel(self.copyTiffs)
        self.label_9.setGeometry(QtCore.QRect(12, 32, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.copyTiffs)
        self.label_10.setGeometry(QtCore.QRect(12, 64, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.copyTiffs)
        self.label_11.setGeometry(QtCore.QRect(12, 96, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit = QtGui.QLineEdit(self.copyTiffs)
        self.lineEdit.setGeometry(QtCore.QRect(188, 32, 433, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.copyTiffs)
        self.lineEdit_2.setGeometry(QtCore.QRect(188, 64, 433, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.copyTiffs)
        self.lineEdit_3.setGeometry(QtCore.QRect(188, 96, 433, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(self.copyTiffs)
        self.pushButton.setGeometry(QtCore.QRect(642, 28, 113, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.copyTiffs)
        self.pushButton_2.setGeometry(QtCore.QRect(642, 60, 113, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.copyTiffs)
        self.pushButton_3.setGeometry(QtCore.QRect(642, 92, 113, 32))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.copyTiffs)
        self.checkBox_2.setGeometry(QtCore.QRect(12, 124, 153, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.catalogTiffOutputWindow_2 = QtGui.QTextEdit(self.copyTiffs)
        self.catalogTiffOutputWindow_2.setGeometry(QtCore.QRect(10, 192, 755, 325))
        self.catalogTiffOutputWindow_2.setReadOnly(True)
        self.catalogTiffOutputWindow_2.setObjectName(_fromUtf8("catalogTiffOutputWindow_2"))
        self.progressBar = QtGui.QProgressBar(self.copyTiffs)
        self.progressBar.setGeometry(QtCore.QRect(16, 158, 745, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.tabContainer.addTab(self.copyTiffs, _fromUtf8(""))
        self.qkShp = QtGui.QWidget()
        self.qkShp.setObjectName(_fromUtf8("qkShp"))
        self.shapeViewWindow = QtGui.QGraphicsView(self.qkShp)
        self.shapeViewWindow.setGeometry(QtCore.QRect(6, 54, 763, 433))
        self.shapeViewWindow.setObjectName(_fromUtf8("shapeViewWindow"))
        self.label_13 = QtGui.QLabel(self.qkShp)
        self.label_13.setGeometry(QtCore.QRect(22, 20, 73, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.shapefileViewPath = QtGui.QLineEdit(self.qkShp)
        self.shapefileViewPath.setGeometry(QtCore.QRect(188, 18, 433, 21))
        self.shapefileViewPath.setObjectName(_fromUtf8("shapefileViewPath"))
        self.shapefileViewBrowseButton = QtGui.QPushButton(self.qkShp)
        self.shapefileViewBrowseButton.setGeometry(QtCore.QRect(642, 14, 113, 32))
        self.shapefileViewBrowseButton.setObjectName(_fromUtf8("shapefileViewBrowseButton"))
        self.shapefileViewClear = QtGui.QPushButton(self.qkShp)
        self.shapefileViewClear.setGeometry(QtCore.QRect(20, 490, 113, 32))
        self.shapefileViewClear.setObjectName(_fromUtf8("shapefileViewClear"))
        self.shapefileViewGo = QtGui.QPushButton(self.qkShp)
        self.shapefileViewGo.setGeometry(QtCore.QRect(640, 490, 113, 32))
        self.shapefileViewGo.setObjectName(_fromUtf8("shapefileViewGo"))
        self.tabContainer.addTab(self.qkShp, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GIS Helper", None))
        self.centroidCalcLabel.setText(_translate("MainWindow", "Calculate Origin", None))
        self.originClearButton.setText(_translate("MainWindow", "Clear", None))
        self.originCalculateButton.setText(_translate("MainWindow", "Calculate", None))
        self.originResultsLabel.setText(_translate("MainWindow", "Origin", None))
        self.ddButtonCalcOrigin_2.setText(_translate("MainWindow", "Decimal Degrees", None))
        self.llButtonCalcOrigin_4.setText(_translate("MainWindow", "Lat/Lon", None))
        self.label.setText(_translate("MainWindow", "Coordinate System", None))
        self.westXEntry.setPlaceholderText(_translate("MainWindow", "East X", None))
        self.eastXEntry.setPlaceholderText(_translate("MainWindow", "West X", None))
        self.northYEntry.setPlaceholderText(_translate("MainWindow", "North Y", None))
        self.southYEntry.setPlaceholderText(_translate("MainWindow", "South Y", None))
        self.label_3.setText(_translate("MainWindow", "West X", None))
        self.label_4.setText(_translate("MainWindow", "East X", None))
        self.label_5.setText(_translate("MainWindow", "North Y", None))
        self.label_6.setText(_translate("MainWindow", "South Y", None))
        self.centroidCalcLabel_2.setText(_translate("MainWindow", "Convert Coordinates", None))
        self.convCoordClear.setText(_translate("MainWindow", "Clear", None))
        self.convCoordCalc.setText(_translate("MainWindow", "Calculate", None))
        self.convCombo.setItemText(0, _translate("MainWindow", "Lat/Lon to Decimal Degrees", None))
        self.convCombo.setItemText(1, _translate("MainWindow", "Decimal Degrees to Lat/Lon", None))
        self.converCoordsEntry.setPlaceholderText(_translate("MainWindow", "Input Coordinates", None))
        self.coordinatesResultsLabel.setText(_translate("MainWindow", "Converted Coordinates", None))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.gisCalc),
                                     _translate("MainWindow", "GIS Calculator", None))
        self.label_2.setText(_translate("MainWindow", "Geotiff Directory: ", None))
        self.catalogTiffBrowseButton.setText(_translate("MainWindow", "Browse", None))
        self.tiffCatalogOutputLabel.setText(_translate("MainWindow", "Output Directory: ", None))
        self.catalogTiffBrowseButton_2.setText(_translate("MainWindow", "Browse", None))
        self.checkBox.setText(_translate("MainWindow", "Fan out by resolution", None))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.catalogTiff),
                                     _translate("MainWindow", "Catalog Tiffs", None))
        self.label_9.setText(_translate("MainWindow", "Geotiff Catalog Directory:", None))
        self.label_10.setText(_translate("MainWindow", "Intersecting Shapepfile: ", None))
        self.label_11.setText(_translate("MainWindow", "Geotiff Output Directory: ", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_2.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_3.setText(_translate("MainWindow", "Browse", None))
        self.checkBox_2.setText(_translate("MainWindow", "Fan out by resolution", None))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.copyTiffs),
                                     _translate("MainWindow", "Copy Tiffs", None))
        self.label_13.setText(_translate("MainWindow", "Shapefile: ", None))
        self.shapefileViewBrowseButton.setText(_translate("MainWindow", "Browse", None))
        self.shapefileViewClear.setText(_translate("MainWindow", "Clear", None))
        self.shapefileViewGo.setText(_translate("MainWindow", "Open Shape", None))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.qkShp),
                                     _translate("MainWindow", "Shapefile QuickView", None))
