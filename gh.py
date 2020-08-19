"""
Tools to help with various GIS tasks
Robert Ross Wardrup
"""

# TODO: database SHP scanner - scan subdirectories and catalog all shapedata.

import sys
from math import modf
import os
from matplotlib import pyplot as plt

from gui import *
from vector import meta
from raster import measurements

# These must be declared for Python to find the gdal and proj libraries
#os.environ['GDAL_DATA'] = 'C:\\Users\\rwardrup\\miniconda3\\envs\\GIS-Helper\\Library\\share\\gdal'
#os.environ['PROJ_LIB'] = 'C:\\Users\\rwardrup\\miniconda3\\envs\\GIS-Helper\\Library\\share\\proj'


class GisHelper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.shape_functions = meta.PolygonFunctions()

        self.originCalculateButton.clicked.connect(get_origin)
        self.originClearButton.clicked.connect(self.clear_origin_fields)

        self.convCoordCalc.clicked.connect(self.get_dd_dms)
        self.convCoordClear.clicked.connect(self.clear_convert_fields)

        self.shapefileViewBrowseButton.clicked.connect(self.browse_for_shp)
        self.shapefileViewGo.clicked.connect(self.display_shapefile)

        self.catalogTiffBrowseButton.clicked.connect(self.browse_for_raster)
        self.catalogTiffProcess.clicked.connect(self.GetRasterBounds)

        # Copy Tiffs page
        self.BrowseForTifDir.clicked.connect(self.browse_for_tiff_directory)
        self.BrowseForIntShape.clicked.connect(self.browse_for_intersecting_shp)
        self.BrowseForGeoTiffOutputDir.clicked.connect(self.browse_for_output_directory)
        self.CopyTiffProcess.clicked.connect(self.handle_tiff_copy)

        plt.rcParams['toolbar'] = 'None'

    def browse_for_intersecting_shp(self):
        """
        Browse system for files
        :return:
        """

        openfile = QtWidgets.QFileDialog.getOpenFileName(self)
        self.intersectingShapefileEdit.setText(openfile)

    def browse_for_tiff_directory(self):
        """
        Browse for file
        :return:
        """

        openfile = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.TiffDirectory.setText(openfile)

    def browse_for_output_directory(self):
        """
        Browse for file
        :return:
        """

        openfile = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.geoTiffOutputDirEdit.setText(openfile)

    def browse_for_shp(self):
        """
        Browse file system for files
        :return:
        """

        openfile = QtWidgets.QFileDialog.getOpenFileName(self)[0]  # This now returns a tuple as of Qt5
        self.shapefileViewPath.setText(openfile)

    def browse_for_raster(self):
        """
        Browse file system for files
        :return:
        """

        openDir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Raster Directory")
        self.geoTiffDir1.setText(openDir)

    def error_popup(self, title, message, info):
        error_popup = QtWidgets.QMessageBox()
        error_popup.setIcon(error_popup.Critical)
        error_popup.setText(message)
        error_popup.setWindowTitle(title)
        error_popup.setInformativeText(info)
        error_popup.setStandardButtons(error_popup.Ok)

        error_popup.show()

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

        metadata['bounds'] = meta.PolygonFunctions.bounding_box(shp)

        print(metadata)

    def display_shapefile(self):
        self.shape_functions.display_shapefile(self.shapefileViewPath)

    def GetRasterBounds(self):
        """
        Gets bounding box of raster image using GDAL bindings
        :param path: path to raster
        :return: tuple of bounding coordinates
        """

        rasters = []
        raster_dictionary = {}
        raster_count = 0

        raster_measurements = measurements.RasterMeasurements()

        path = self.geoTiffDir1.text()

        raster_count, raster_dictionary = raster_measurements.CalculateRasterBounds(path)

        output_text = "Finished processing {0} rasters.\n\n".format(raster_count)
        output_text += 'Raster paths and bounds (ulX, ulY, lrX, lrY): \n'

        for filepath, bounds in raster_dictionary.items():
            output_text += '{0}: {1}\n\n'.format(filepath, bounds)

        self.catalogTiffOutputWindow.setText(output_text)

        return raster_count, raster_dictionary

    def handle_tiff_copy(self):
        """
        Handles code that copies tifs
        :return: IO
        """

        tiff_directory = self.TiffDirectory.text()
        shapefile_directory = self.intersectingShapefileEdit.text()
        output_directory = self.geoTiffOutputDirEdit.text()

        payload = (tiff_directory, shapefile_directory, output_directory)

        polygon_functions = meta.PolygonFunctions()
        polygon_functions.get_polygon_vertices(payload)


def get_origin(coords):
    """
    Button function to get origin calculation. Runs the origin_calc() function which runs the calculation.
    :return: Origin
    """

    blank_entry = False
    output_text = GisHelper.originOutputBox

    if coords:
        north_y = coords[0]
        south_y = coords[1]
        east_x = coords[2]
        west_x = coords[3]
    else:
        # Grab values from text entry boxes and convert to floats
        north_y = GisHelper.northYEntry.text()
        south_y = GisHelper.southYEntry.text()
        east_x = GisHelper.eastXEntry.text()
        west_x = GisHelper.westXEntry.text()

    coordinates = [north_y, south_y, east_x, west_x]

    # Print error message if entry is blank
    for i in coordinates:
        if len(i) == 0:
            blank_entry = True

    if blank_entry:
        title = "Error"
        text = "Missing coordinate(s) input."
        info = "Check that all coordinate fields contain valid values."
        GisHelper.error_popup(title, text, info)

    else:
        centroid = origin_calc(coordinates)  # Get origin from origin_calc
        if centroid:  # If a centroid is returned, print to text box.
            centroid = "{0}, {1}".format(centroid[0], centroid[1])
            output_text.setText(centroid)
        else:  # Calculate_origin returned false, indicating invalid input. Print error message.
            GisHelper.error_popup('Error', 'Error converting coordinates to decimal numbers.',
                                  'Check to ensure '
                                  'coordinate input '
                                  'contain only numbers.')


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
    #app = QtGui.QGuiApplication.QApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    window = GisHelper()
    window.show()
    sys.exit(app.exec_())
