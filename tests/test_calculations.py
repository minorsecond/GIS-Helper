from spatial_functions.calculations import origin_calc, dd_to_dms, dms_to_dd
from raster import measurements


def test_dd_to_dms():
    """
    Test conversion from decimal degrees to degrees, minutes, seconds
    """
    assert dd_to_dms(38.898556) == (38, 53, 54.802, True)
    assert dd_to_dms(-77.037852) == (-77, -2, 16.267, True)
    assert dd_to_dms(180.001) == (None, None, None, False)


def test_dms_to_dd():
    """
    Test conversion from degrees, minutes, seconds to decimal degrees
    """
    assert dms_to_dd("32 46 3.5") == 32.76764
    assert dms_to_dd("32d 46m 3.5s") == 32.76764
    assert dms_to_dd("032m 046d 003.5s") == 32.76764
    assert dms_to_dd("032046003.5") == 32.76764


def test_origin_calculation():
    """
    Test origin coordinate calculation.
    """
    coordinates = [0.0, 10.0, 0.0, 10.0]
    assert origin_calc(coordinates) == (5.0, 5.0)


def test_raster_bounds():
    """
    Tests raster bounding box calc
    :return:
    """

    path = '.\\tests\\test_data\\'
    raster_measurements = measurements.RasterMeasurements()
    results = raster_measurements.CalculateRasterBounds(path)

    assert results == (1, {'.\\tests\\test_data\\raster.tif': [-99.632,
                                                               31.564,
                                                               -99.628,
                                                               31.562
                                                               ]})


def test_get_pixel_value():
    path = 'tests\\test_data\\'
    raster_measurements = measurements.RasterMeasurements()
    pixel_value = raster_measurements.getPixelValue(raster=path,
                                                    in_x=-99.631408,
                                                    in_y=31.562316)
    assert pixel_value == (102, 120, 91)
