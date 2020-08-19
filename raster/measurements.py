from os.path import join
from os import walk
import gdal
import rasterio as rio

# These are needed for pyinstaller
from rasterio import _shim, control, crs, sample, vrt, _features


class RasterMeasurements:
    """
    Contains methods for measuring raster bounds, pixel size, etc.
    """

    def CalculateRasterBounds(self, path):
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

    def getPixelValue(self, raster, in_x, in_y):
        """
        Gets raster pixel value at xy coordinate
        :return: an RGB tuple
        """

        pixel_val = None

        # Remove this - don't want to run this thing twice
        raster_count, raster_dictionary = self.CalculateRasterBounds(raster)

        for raster_path, bounds in raster_dictionary.items():
            with rio.open(raster_path) as raster_input:
                px, py = raster_input.index(in_x, in_y)

                # one-pixel window
                window = rio.windows.Window(py - 1//2, px - 1//2, 1, 1)
                clip = raster_input.read(window=window)
                pixel_val = clip[0][0][0], clip[1][0][0], clip[2][0][0]
        return pixel_val
