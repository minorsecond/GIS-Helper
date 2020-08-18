from os.path import join
from os import walk
from gdal import Open as gdal_open

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
            image = gdal_open(raster)  # Open the file using gdal
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