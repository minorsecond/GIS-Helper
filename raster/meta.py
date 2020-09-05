class RasterIO:
    """
    Contains io functions
    """

import vector.meta as vector_functions
from shapely.geometry import Polygon
from raster import measurements as raster_measurements
import os


def intersect_by_shape(tiff_directory, shapefile_path, output_directory):
    """
    Find rasters that intersect polygons in a shapefile.
    :param tiff_directory: String denoting path of a directory
    containing rasters.
    :param shapefile_directory: String denoting path to a shapefile
    :param output_directory: Path denoting output path.
    :return:
    """
    polygons = []
    raster_paths = []
    intersecting_rasters = []

    payload = (tiff_directory, shapefile_path, output_directory)

    polygon_functions = vector_functions.PolygonFunctions()
    shp_vertices = polygon_functions.get_polygon_vertices(payload)
    for polygon in shp_vertices:
        shp_poly = Polygon(polygon)
        polygons.append(shp_poly)

    for root, dirname, filenames in os.walk(tiff_directory):
        for file in filenames:
            if os.path.splitext(file)[1].lower() == ".tif":
                raster_path = os.path.join(root, file)
                raster_paths.append(raster_path)

    raster_bounds = raster_measurements. \
        calculate_raster_bounds(raster_paths)[1]

    for path, bounds in raster_bounds.items():
        raster_ulx = bounds[0]
        raster_uly = bounds[1]
        raster_lrx = bounds[2]
        raster_lry = bounds[3]
        raster_llx = raster_ulx
        raster_lly = raster_lry
        raster_urx = raster_lrx
        raster_ury = raster_uly
        raster_poly = Polygon([(raster_llx, raster_lly),
                               (raster_ulx, raster_uly),
                               (raster_urx, raster_ury),
                               (raster_lrx, raster_lry)])

        for polygon in polygons:
            if polygon.intersects(raster_poly):
                intersecting_rasters.append(path)

    return intersecting_rasters
