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


class GisHelper(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.originCalculateButton.clicked.connect(self.get_origin)
        self.originClearButton.clicked.connect(self.clear_origin_fields)

        self.convCoordCalc.clicked.connect(self.get_dd_dms)
        self.convCoordClear.clicked.connect(self.clear_convert_fields)

        self.shapefileViewBrowseButton.clicked.connect(self.browse_filesystem)
        self.shapefileViewGo.clicked.connect(self.display_shapefile)

        plt.rcParams['toolbar'] = 'None'

    def browse_filesystem(self):
        """
        Browse file system for files
        :return:
        """

        openfile = QtGui.QFileDialog.getOpenFileName(self)
        self.shapefileViewPath.setText(openfile[0])

    def error_popup(self, title, message, info):
        error_popup = QtGui.QMessageBox()
        error_popup.setIcon(error_popup.Critical)
        error_popup.setText(message)
        error_popup.setWindowTitle(title)
        error_popup.setInformativeText(info)
        error_popup.setStandardButtons(error_popup.Ok)

        error_popup.exec()

    def get_origin(self):
        """
        Button function to get origin calculation. Runs the origin_calc() function which runs the calculation.
        :return: Origin
        """

        blank_entry = False
        output_text = self.originOutputBox

        # Grab values from text entry boxes and convert to floats
        north_y = self.northYEntry.text()
        south_y = self.southYEntry.text()
        east_x = self.eastXEntry.text()
        west_x = self.westXEntry.text()

        coordinates = [north_y, south_y, east_x, west_x]

        # Print error message if entry is blank
        for i in coordinates:
            if len(i) == 0:
                blank_entry = True

        if blank_entry:
            title = "Error"
            text = "Missing coordinate(s) input."
            info = "Check that all coordinate fields contain valid values."
            self.error_popup(title, text, info)

        else:
            centroid = origin_calc(coordinates)  # Get origin from origin_calc
            if centroid:  # If a centroid is returned, print to text box.
                centroid = "{0}, {1}".format(centroid[0], centroid[1])
                output_text.setText(centroid)
            else:  # Calculate_origin returned false, indicating invalid input. Print error message.
                self.error_popup('Error', 'Error converting coordinates to decimal numbers.',
                                 'Check to ensure '
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

    def get_dd_dms(self):
        """
        Convert decimal degrees to lat/lon
        :return: lat/lon value
        """

        input_coord = self.converCoordsEntry.text()
        output_text = self.converterOutput

        if len(input_coord) == 0:
            title = "Error"
            text = "Missing coordinate input."
            info = "Check that coordinate field contains valid value."
            self.error_popup(title, text, info)

        else:
            try:
                degrees, minutes, seconds, valid = dd_to_dms(input_coord)
                if valid:
                    output = '{0}d, {1}m, {2}s'.format(degrees, minutes, seconds)
                    output_text.setText(output)
                else:
                    self.error_popup('Error', 'Check input and try again.', '')

            except ValueError:
                self.error_popup('Error', 'Error converting decimal degrees to lat/lon.',
                                 'Check to ensure coordinate input only contains numbers.')

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

    def bounding_box(self, shp):
        """
        Get bounding box of shapefile
        :return:
        """

        ll_lat = 9999999999.9
        ll_lon = 9999999999.9
        ur_lat = 0.0
        ur_lon = 0.0

        shp = shp.shapes()
        bounding_box = [ll_lon, ll_lat, ur_lon, ur_lat]

        for i in shp:
            bbox = i.bbox
            if bbox[0] < bounding_box[0]:
                bounding_box[0] = round(bbox[0], 5)

            if bbox[1] < bounding_box[1]:
                bounding_box[1] = round(bbox[1], 5)

            if bbox[2] > bounding_box[2]:
                bounding_box[2] = round(bbox[2], 5)

            if bbox[3] > bounding_box[3]:
                bounding_box[3] = round(bbox[3], 5)

        return bounding_box

    def get_shape_meta(self, shp):
        """
        Gets metadata from shapefile
        :return: shapefile metadata
        """
        metadata = {
            'proj': None,
            'origin': None,
            'bounds': None,
            'nRecords': None
        }

        metadata['bounds'] = self.bounding_box(shp)

        print(metadata)

    def display_shapefile(self):
        """
        Display shape data on screen
        :return:
        """

        shp_path = self.shapefileViewPath.text()

        if len(shp_path) > 0:
            try:
                shp = shapefile.Reader(shp_path)
                meta = self.get_shape_meta(shp)
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


def origin_calc(coords):
    """
    Calculates the origin of a bounding box
    :param coords: List of tuples containing coordinates in (x,y),(x,y) format
    :return: A list of xy coords denoting origin, false if coordinate entry is invalid
    """

    blank_entry = False

    for i in coords:
        if not coords:
            blank_entry = True

    if not blank_entry:
        try:
            coords[0] = float(coords[0])
            coords[1] = float(coords[1])
            coords[2] = float(coords[2])
            coords[3] = float(coords[3])

            x = [coords[2], coords[3]]
            y = [coords[0], coords[1]]

            centroid = (sum(x) / 2, sum(y) / 2)
            return centroid

        except ValueError:
            return False


def dd_to_dms(coords):
    """
    Calculates decimal degrees to degrees, minutes, seconds
    :param coords: a float (DD)
    :return: DMS coordinates
    """
    degrees = None
    minutes = None
    seconds = None
    valid = True

    try:
        input_coord = float(coords)
        if input_coord >= -180 and input_coord <= 180:
            number_list = modf(input_coord)
            integer = number_list[1]
            decimal = number_list[0]

            degrees = int(integer)
            minutes = int(60 * decimal)
            seconds = abs(round(((decimal - (minutes / 60)) * 3600), 3))
        else:
            valid = False

    except Exception as e:
        print(e)

    return degrees, minutes, seconds, valid


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = GisHelper()
    window.show()
    sys.exit(app.exec_())
