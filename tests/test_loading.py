# Test loading of shapefiles and rasters
from vector import meta
import shapefile


def test_load_shapefile():
    input_payload = ["", "tests\\test_data\\texas.shp", ""]
    shapefile_functions = meta.PolygonFunctions()
    shp = shapefile_functions.load_polygons(input_payload)

    assert type(shp) == shapefile.Shapes


def test_load_raster():
    input_payload = "tests\\test_data\\i30dem.tif"

    # TODO: Write the raster load code
