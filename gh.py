"""
Tools to help with various GIS tasks
Robert Ross Wardrup
"""

# TODO: database SHP scanner - scan subdirectories and catalog all shapedata.

import sys
from math import modf

import matplotlib.pyplot as plt
import shapefile

from gui import *


class gishelper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.originCalculateButton.clicked.connect(self.calculateOrigin)
        self.originClearButton.clicked.connect(self.clear_origin_fields)

        self.convCoordCalc.clicked.connect(self.dd_to_dms)
        self.convCoordClear.clicked.connect(self.clear_convert_fields)

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

                centroid = (sum(x) / 2, sum(y) / 2)
                centroid = "{0}, {1}".format(centroid[0], centroid[1])

                outputText.setText(centroid)

            except ValueError:
                self.error_popup('Error', 'Error converting coordinates to decimal numbers.', 'Check to ensure '
                                                                                              'coordinate input '
                                                                                              'contain only numbers.')

    def clear_origin_fields(self):
        self.northYEntry.clear()
        self.southYEntry.clear()
        self.eastXEntry.clear()
        self.westXEntry.clear()
        self.originOutputBox.clear()

    def clear_convert_fields(self):
        self.converCoordsEntry.clear()
        self.converterOutput.clear()

    def dd_to_dms(self):
        """
        Convert decimal degrees to lat/lon
        :return: lat/lon value
        """

        blank_entry = False
        input_coord = self.converCoordsEntry.text()
        outputText = self.converterOutput
        if len(input_coord) == 0:
            blank_entry = True
            title = "Error"
            text = "Missing coordinate input."
            info = "Check that coordinate field contains valid value."
            self.error_popup(title, text, info)
        else:
            try:
                input_coord = float(input_coord)
                number_list = modf(input_coord)
                print(number_list)
                integer = number_list[1]
                decimal = number_list[0]

                degrees = int(integer)
                minutes = int(60 * decimal)
                # seconds = int(60 * modf(minutes)[1])
                seconds = round(((decimal - (minutes / 60)) * 3600), 3)

                output = '{0}d, {1}m, {2}s'.format(degrees, minutes, seconds)
                outputText.setText(output)

            except ValueError:
                self.error_popup('Error', 'Error converting decimal degrees to lat/lon.', 'Check to ensure coordinate '
                                                                                          'input only contains numbers.')

    def dms_to_dd(self):
        """
        Convert dms to decimal degrees
        :return: dd
        """

        degrees = 0
        minutes = 0
        seconds = 0

        input_coord = self.converCoordsEntry.text()

        dd = degrees + (minutes / 60) + (seconds / 3600)

    def bounding_box(self, shapefile):
        """
        Get bounding box of shapefile
        :return:
        """

        ll_lat = 9999999999.9
        ll_lon = 9999999999.9
        ur_lat = 0.0
        ur_lon = 0.0

        shapefile = shapefile.shapes()
        bounding_box = [ll_lon, ll_lat, ur_lon, ur_lat]

        for i in shapefile:
            bbox = i.bbox
            if bbox[0] < bounding_box[0]:
                bounding_box[0] = bbox[0]

            if bbox[1] < bounding_box[1]:
                bounding_box[1] = bbox[1]

            if bbox[2] > bounding_box[2]:
                bounding_box[2] = bbox[2]

            if bbox[3] > bounding_box[3]:
                bounding_box[3] = bbox[3]

        return bounding_box


    def display_shapefile(self):
        """
        Display shape data on screen
        :return:
        """

        shpFilePath = self.shapefileViewPath.text()

        if len(shpFilePath) > 0:
            try:
                shp = shapefile.Reader(shpFilePath)
                plt.figure()
                try:
                    for shape in shp.shapeRecords():
                        xy = [i for i in shape.shape.points[:]]
                        x, y = zip(*[(j[0], j[1]) for j in xy])
                        plt.plot(x, y)
                    plt.show(1)
                except AssertionError:
                    self.error_popup('Error', 'Shapefile does not contain points.',
                                     'Check feature type and try again')


            except shapefile.ShapefileException:
                self.error_popup('Error', 'Shapefile not found.', 'Ensure that the path is correct and try again.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = gishelper()
    window.show()
    sys.exit(app.exec_())
