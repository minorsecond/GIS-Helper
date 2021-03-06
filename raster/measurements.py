from os.path import join, splitext
from os import mkdir
from os import walk
import gdal
import rasterio as rio
from shapely.geometry import Point, Polygon, mapping
import fiona

# These are needed for pyinstaller
from rasterio import _shim, control, crs, sample, vrt, _features  # noqa


def calculate_raster_bounds(rasters):
    """
    Gets bounding box of raster image using GDAL bindings
    :param rasters: list of raster paths
    :return: tuple of bounding coordinates
    """

    raster_dictionary = {}
    raster_count = 0

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


def create_catalog(path, output_dir, fanout=False):
    rasters_by_resolution = {}
    rasters = []
    polygons = []
    resolution = None

    output_path = join(output_dir, 'tif_catalog.shp')

    for dirpath, dirnames, filenames in walk(path):
        for file in filenames:
            if splitext(file)[1].lower() == '.tif':
                rasters.append(join(dirpath, file))

    # rasters is a dict - path: [ulx, uly, lrx, lry]
    count, rasters = calculate_raster_bounds(rasters)

    # Create the polygons
    for path, bounds in rasters.items():
        resolution = get_resolution(path)
        resolution = f"{resolution[0]}x{resolution[1]}"

        ulx = bounds[0]
        uly = bounds[1]
        lrx = bounds[2]
        lry = bounds[3]

        p1 = Point(ulx, lry)
        p2 = Point(ulx, uly)
        p3 = Point(lrx, uly)
        p4 = Point(lrx, lry)

        pointList = [p1, p2, p3, p4]

        poly = Polygon([[p.x, p.y] for p in pointList])
        poly.path = path
        poly.resolution = resolution

        if fanout:  # Build the resolution dictionary
            if resolution not in rasters_by_resolution:
                rasters_by_resolution[resolution] = [poly]
            else:
                rasters_by_resolution[resolution].append(poly)
        else:
            polygons.append(poly)

    # Write to shp
    schema = {
        'geometry': 'Polygon',
        'properties': {'id': 'int',
                       'path': 'str',
                       'resolution': 'str'}
    }

    row_number = 0
    if fanout:
        for resolution, polygons in rasters_by_resolution.items():
            output_basedir = join(output_dir, resolution)
            mkdir(output_basedir)
            output_filename = resolution + "_raster_catalog.shp"
            output_path = join(output_basedir, output_filename)
            with fiona.open(output_path, 'w', 'ESRI Shapefile', schema) as c:
                for polygon in polygons:
                    c.write({
                        'geometry': mapping(polygon),
                        'properties': {'id': row_number,
                                       'path': path,
                                       'resolution': resolution
                                       }
                    })

                    row_number += 1

    else:
        with fiona.open(output_path, 'w', 'ESRI Shapefile', schema) as c:
            for polygon in polygons:
                c.write({
                    'geometry': mapping(polygon),
                    'properties': {'id': row_number,
                                   'path': path,
                                   'resolution': resolution
                                   }
                })

                row_number += 1

    return count, rasters


def get_resolution(raster_path):
    """
    Gets resolution if input raster
    :param raster_path: Path to raster
    :return: list of integers denoting resolution of raster
    """

    with rio.open(raster_path) as raster:
        res = raster.res

    return res


class RasterMeasurements:
    """
    Contains methods for measuring raster bounds, pixel size, etc.
    """

    def getPixelValue(self, raster, in_x, in_y):
        """
        Gets raster pixel value at xy coordinate
        :return: an RGB tuple
        """

        pixel_val = None

        # Remove this - don't want to run this thing twice
        raster_count, raster_dictionary = calculate_raster_bounds(raster)

        for raster_path, bounds in raster_dictionary.items():
            with rio.open(raster_path) as raster_input:
                px, py = raster_input.index(in_x, in_y)

                # one-pixel window
                window = rio.windows.Window(py - 1//2, px - 1//2, 1, 1)
                clip = raster_input.read(window=window)
                pixel_val = clip[0][0][0], clip[1][0][0], clip[2][0][0]
        return pixel_val
