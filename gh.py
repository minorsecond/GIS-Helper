"""
Tools to help with various GIS tasks
Robert Ross Wardrup
"""
import sys
import os
from pathlib import Path
from matplotlib import pyplot as plt
from gui import QtWidgets, Ui_MainWindow
from vector import meta
from raster import measurements
from spatial_functions.calculations import origin_calc, \
    dd_to_dms, dms_to_dd

anaconda_dir = os.path.join(str(Path.home()), "anaconda3\\envs\\GIS-Helper")
print("Anaconda3 Dir: {}".format(anaconda_dir))
os.environ['GDAL_DATA'] = os.path.join(anaconda_dir, 'Library\\share\\gdal')
os.environ['PROJ_LIB'] = os.path.join(anaconda_dir, 'Library\\share\\proj')


class GisHelper(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Main user interface class.
    """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.shape_functions = meta.PolygonFunctions()

        self.originCalculateButton.clicked.connect(self.get_origin)
        self.originClearButton.clicked.connect(self.clear_origin_fields)

        self.convCoordCalc.clicked.connect(self.get_dd_dms)
        self.convCoordClear.clicked.connect(self.clear_convert_fields)

        self.shapefileViewBrowseButton.clicked.connect(self.browse_for_shp)
        self.shapefileViewGo.clicked.connect(self.display_shapefile)

        self.catalogTiffBrowseButton.clicked.connect(self.browse_for_raster)
        self.catalogTiffProcess.clicked.connect(self.get_raster_bounds)

        # Copy Tiffs page
        self.BrowseForTifDir.clicked.connect(self.browse_for_tiff_directory)
        self.BrowseForIntShape.\
            clicked.connect(self.browse_for_intersecting_shp)
        self.BrowseForGeoTiffOutputDir.\
            clicked.connect(self.browse_for_output_directory)
        self.CopyTiffProcess.clicked.connect(self.handle_tiff_copy)

        self.error_popup = QtWidgets.QMessageBox()

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
        # This now returns a tuple as of Qt5
        openfile = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        self.shapefileViewPath.setText(openfile)

    def browse_for_raster(self):
        """
        Browse file system for files
        :return:
        """

        open_dir = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                              "Select Raster "
                                                              "Directory")
        self.geoTiffDir1.setText(open_dir)

    def error_popup_show(self, title, message, info):
        """
        Display an error message when an exception occurs.
        :param title: A string for the window title, should be "Error"
        :param message: Quick message about the error.
        :param info: How to resolve the error.
        :return: Error text displayed in QMessageBox
        """

        self.error_popup.setIcon(self.error_popup.Critical)
        self.error_popup.setText(message)
        self.error_popup.setWindowTitle(title)
        self.error_popup.setInformativeText(info)
        self.error_popup.setStandardButtons(self.error_popup.Ok)

        self.error_popup.show()

    def clear_origin_fields(self):
        """
        Clear the orgin calculation fields
        :return: Blank fields
        """
        self.northYEntry.clear()
        self.southYEntry.clear()
        self.eastXEntry.clear()
        self.westXEntry.clear()
        self.originOutputBox.clear()

    def clear_convert_fields(self):
        """
        Clear the coordinate system conversion fields
        :return: Blank fields
        """
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
                    output = '{0}d, {1}m, {2}s'.format(degrees, minutes,
                                                       seconds)
                    output_text.setText(output)
                else:
                    self.error_popup('Error', 'Check input and try again.', '')

            except ValueError:
                self.error_popup('Error',
                                 'Error converting decimal degrees to '
                                 'lat/lon.',
                                 'Check to ensure coordinate input only'
                                 ' contains numbers.')

    def display_shapefile(self):
        """
        Linker to run the display_shapefile function iin shape_functions
        module. #TODO This is eligible for removal.
        :return:
        """
        print("calling display_shapefile")
        self.shape_functions.display_shapefile(self.shapefileViewPath)

    def get_raster_bounds(self):
        """
        Gets bounding box of raster image using GDAL bindings
        :param path: path to raster
        :return: tuple of bounding coordinates
        """

        raster_measurements = measurements.RasterMeasurements()

        path = self.geoTiffDir1.text()

        raster_count, raster_dictionary = raster_measurements.\
            CalculateRasterBounds(path)

        output_text = "Finished processing {0} rasters.\n\n".\
            format(raster_count)
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

    def get_origin(self):
        """
        Button function to get origin calculation. Runs the origin_calc()
        function which runs the calculation.
        :return: Origin
        """

        blank_entry = False
        output_text = self.originOutputBox

        # Grab values from text entry boxes and convert to floats
        north_y = self.northYEntry.text()
        south_y = self.southYEntry.text()
        east_x = self.eastXEntry.text()
        west_x = self.westXEntry.text()

        # Print error message if entry is blank
        for i in north_y, south_y, east_x, west_x:
            if len(i) == 0:
                blank_entry = True

        if blank_entry:
            title = "Error"
            text = "Missing coordinate(s) input."
            info = "Check that all coordinate fields contain valid values."
            self.error_popup_show(title, text, info)

        else:
            north_y = float(north_y)
            south_y = float(south_y)
            east_x = float(east_x)
            west_x = float(west_x)

            coordinates = [north_y, south_y, east_x, west_x]

            centroid = origin_calc(coordinates)  # Get origin from origin_calc
            if centroid:  # If a centroid is returned, print to text box.
                centroid = "{0}, {1}".format(centroid[0], centroid[1])
                output_text.setText(centroid)
            # Calculate_origin returned false, indicating invalid input.
            # Print error message.
            else:
                title = "Error"
                text = "Error converting coordinates to decimal numbers."
                info = "Check to insure coordinate input contains only " \
                       "numbers."
                self.error_popup_show(title, text, info)


if __name__ == "__main__":
    # app = QtGui.QGuiApplication.QApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    window = GisHelper()
    window.show()
    sys.exit(app.exec_())
