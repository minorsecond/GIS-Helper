from os.path import join
from os import walk
import gdal
import struct

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

        rgb2i = None
        i2rgb = None
        rasterBand = None

        # Remove this - don't want to run this thing twice
        raster_count, raster_dictionary = self.CalculateRasterBounds(raster)

        for raster_path, bounds in raster_dictionary.items():
            raster = gdal.Open(raster_path, 1)
            geoTransform = raster.GetGeoTransform()
            print("geotransform: {}".format(geoTransform))
            rasterBand = raster.GetRasterBand(1)

            px = int((in_x - geoTransform[0]) / geoTransform[1])  # x pixel
            py = int((in_y - geoTransform[3]) / geoTransform[5])  # y pixel

            print("px: {0} py: {1}".format(px, py))
            structval = rasterBand.ReadRaster(px, py, 1, 1, buf_type=gdal.GDT_UInt16)
            print("structval: {}".format(structval))
            intval = struct.unpack('h', structval)

            print("Result: {}".format(intval[0]))

            gdal.UseExceptions()

        return rasterBand
