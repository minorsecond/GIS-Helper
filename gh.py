"""
Tools to help with various GIS tasks
Robert Ross Wardrup
"""

# TODO: database SHP scanner - scan subdirectories and catalog all shapedata.

import sys
from math import modf
import os
from os import walk
from os.path import join

import fiona
from fiona import _shim, schema
import matplotlib.pyplot as plt
import shapefile
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
from osgeo import gdal
from shapely.geometry import MultiPolygon, shape

from gui import *

# These must be declared for Python to find the gdal and proj libraries
os.environ['GDAL_DATA'] = 'C:\\Users\\rwardrup\\miniconda3\\envs\\GIS-Helper\\Library\\share\\gdal'
os.environ['PROJ_LIB'] = 'C:\\Users\\rwardrup\\miniconda3\\envs\\GIS-Helper\\Library\\share\\proj'

class GisHelper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

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
        color_map = plt.get_cmap('RdBu')
        num_colors = 1000

        if len(shp_path) > 0:
            # try:

            # Open shape data
            shp = MultiPolygon(
                [shape(pol['geometry']) for pol in fiona.open(shp_path)]
            )

            print("Finished loading shape data")

            fig = plt.figure()

            # try:
            ax = fig.add_subplot(111)
            minx, miny, maxx, maxy = shp.bounds
            w, h = maxx - minx, maxy - miny
            ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
            ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
            ax.set_aspect(1)

            patches = []
            for idx, p in enumerate(shp):
                colour = color_map(1. * idx / num_colors)
                patches.append(PolygonPatch(p, fc=colour, ec='#555555', alpha=1., zorder=1))
                print("Adding {0} to plot.".format(idx))

            ax.add_collection(PatchCollection(patches, match_original=True))
            plt.show()


    def GetRasterBounds(self):
        """
        Gets bounding box of raster image using GDAL bindings
        :param path: path to raster
        :return: tuple of bounding coordinates
        """

        rasters = []
        raster_dictionary = {}
        raster_count = 0

        path = self.geoTiffDir1.text()

        raster_count, raster_dictionary = CalculateRasterBounds(path)

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

        polygon_functions = PolygonFunctions()
        polygon_functions.get_polygon_vertices(payload)


class PolygonFunctions:
    """
    Contains the IO functions
    """

    def load_polygons(self, payload):
        """
        Loads polygons into memory
        :return:
        """

        self.input_file = payload[0]
        self.shapefile_directory = payload[1]
        self.output_directory = payload[2]

        shp = shapefile.Reader(self.shapefile_directory)
        self.shapes = shp.shapes()

    def get_polygon_vertices(self, payload):
        """
        Gets vertex locations for polygons
        :return:
        """

        self.vertices = []

        self.load_polygons(payload)

        for polygon in self.shapes:
            self.vertices.append(polygon.points)

        print(self.vertices)


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


def getPixelValue(raster):
    """
    Gets raster pixel value at xy coordinate
    :return: an RGB tuple
    """

    rgb2i = None
    i2rgb = None

    _, raster_dictionary = CalculateRasterBounds(
        raster)  # Remove this - don't want to run this thing twice

    for raster_path, bounds in raster_dictionary.items():
        raster = gdal.Open(raster_path)
        geoTransform = raster.GetGeoTransform()
        rasterBand = geoTransform.GetRasterBand(1)
        gdal.UseExceptions()



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


def CalculateRasterBounds(path):
    """
    Gets bounding box of raster image using GDAL bindings
    :param path: path to raster
    :return: tuple of bounding coordinates
    """

    rasters = []
    raster_dictionary = {}
    raster_count = 0

    for dirpath, dirnames, filenames in walk(path):
        for file in filenames:
            if file.endswith('.tif'):
                rasters.append(join(dirpath, file))

    for raster in rasters:
        raster_count += 1
        image = gdal.Open(raster)  # Open the file using gdal
        ulx, xres, xskew, uly, yskew, yres = image.GetGeoTransform()
        lrx = ulx + (image.RasterXSize * xres)
        lry = uly + (image.RasterYSize * yres)

        ulx = round(ulx, 3)
        uly = round(uly, 3)
        lrx = round(lrx, 3)
        lry = round(lry, 3)

        bounds = [ulx, uly, lrx, lry]
        raster_dictionary[raster] = bounds

    return raster_count, raster_dictionary


if __name__ == "__main__":
    #app = QtGui.QGuiApplication.QApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    window = GisHelper()
    window.show()
    sys.exit(app.exec_())
