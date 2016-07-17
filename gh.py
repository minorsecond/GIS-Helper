"""
Tools to help with various GIS tasks
Robert Ross Wardrup
"""

# TODO: database SHP scanner - scan subdirectories and catalog all shapedata.

import sys

import matplotlib.pyplot as plt
import shapefile
from PyQt5 import uic, QtWidgets

qtCreatorFile = "gisHelperGui.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class gishelper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.originCalculateButton.clicked.connect(self.calculateOrigin)
        self.originClearButton.clicked.connect(self.clear_origin_fields)

        self.shapefileViewBrowseButton.clicked.connect(self.browseFileSystem)
        self.shapefileViewGo.clicked.connect(self.display_shapefile)

        plt.rcParams['toolbar'] = 'None'

    def browseFileSystem(self):
        """
        Browse file system for files
        :return:
        """

        openfile = QtWidgets.QFileDialog.getOpenFileName(self)
        self.shapefileViewPath.setText(openfile[0])

    def error_popup(self, title, message, info):
        error_popup = QtWidgets.QMessageBox()
        error_popup.setIcon(error_popup.Critical)
        error_popup.setText(message)
        error_popup.setWindowTitle(title)
        error_popup.setInformativeText(info)
        error_popup.setStandardButtons(error_popup.Ok)

        error_popup.exec()

    def calculateOrigin(self):
        """
        Calculates the origin, given bounding box coordinates
        :return: Origin
        """

        blank_entry = False
        outputText = self.originOutputBox

        # Grab values from text entry boxes and convert to floats
        # TODO: Data validation
        north_y = self.northYEntry.text()
        south_y = self.southYEntry.text()
        east_x = self.eastXEntry.text()
        west_x = self.westXEntry.text()

        coordinates = [north_y, south_y, east_x, west_x]

        for i in coordinates:
            if len(i) == 0:
                blank_entry = True

        if blank_entry:
            title = "Error"
            text = "Missing coordinate(s) input."
            info = "Check that all coordinate fields contain valid values."
            self.error_popup(title, text, info)

        else:
            try:
                coordinates[0] = float(coordinates[0])
                coordinates[1] = float(coordinates[1])
                coordinates[2] = float(coordinates[2])
                coordinates[3] = float(coordinates[3])

                x = [coordinates[2], coordinates[3]]
                y = [coordinates[0], coordinates[1]]

                centroid = (sum(x) / len(coordinates), sum(y) / len(coordinates))
                centroid = "{0}, {1}".format(centroid[0], centroid[1])

                outputText.setText(centroid)

            except ValueError:
                self.error_popup('Error', 'Error converting coordinates to decimal numbers.', 'Check to ensure '
                                                                                              'coordinate input boxes '
                                                                                              'contain only numbers.')

    def clear_origin_fields(self):
        self.northYEntry.clear()
        self.southYEntry.clear()
        self.eastXEntry.clear()
        self.westXEntry.clear()
        self.originOutputBox.clear()

    def dd_to_dms(self):
        """
        Convert decimal degrees to lat/lon
        :return: lat/lon value
        """

    def dms_to_dd(self):
        """
        Convert dms to decimal degrees
        :return: dd
        """

        degrees = 0
        minutes = 0
        seconds = 0

        dd = degrees + (minutes / 60) + (seconds / 3600)

    def display_shapefile(self):
        """
        Display shape data on screen
        :return:
        """

        shpFilePath = self.shapefileViewPath.text()

        if len(shpFilePath) > 0:
            try:
                shp = shapefile.Reader(shpFilePath)
                for shape in shp.shapeRecords():
                    x = [i[0] for i in shape.shape.points[:]]
                    y = [i[1] for i in shape.shape.points[:]]
                    plt.plot(x, y)

                plt.show()

            except shapefile.ShapefileException:
                self.error_popup('Error', 'Shapefile not found.', 'Ensure that the path is correct and try again.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = gishelper()
    window.show()
    sys.exit(app.exec_())
