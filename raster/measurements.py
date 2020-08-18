from os.path import join
from os import walk
import gdal


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

    def getPixelValue(self, raster):
        """
        Gets raster pixel value at xy coordinate
        :return: an RGB tuple
        """

        rgb2i = None
        i2rgb = None

        _, raster_dictionary = self.CalculateRasterBounds(
            raster)  # Remove this - don't want to run this thing twice

        for raster_path, bounds in raster_dictionary.items():
            raster = gdal.Open(raster_path)
            geoTransform = raster.GetGeoTransform()
            rasterBand = geoTransform.GetRasterBand(1)
            gdal.UseExceptions()