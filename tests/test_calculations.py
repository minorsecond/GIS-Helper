from gh import dd_to_dms, origin_calc
from raster import measurements

def test_dd_to_dms():
    assert dd_to_dms(38.898556) == (38, 53, 54.802, True)
    assert dd_to_dms(-77.037852) == (-77, -2, 16.267, True)
    assert dd_to_dms(180.001) == (None, None, None, False)


def test_origin_calculation():
    coordinates = [0.0, 10.0, 0.0, 10.0]
    assert origin_calc(coordinates) == (5.0, 5.0)


def test_raster_bounds():
    """
    Tests raster bounding box calc
    :return:
    """

    path = 'color_image.tif'
    raster_measurements = measurements.RasterMeasurements()
    results = raster_measurements.CalculateRasterBounds(path)
    print(results)

    #assert results == (1, {'color_image.tif': [-977500.0,  # ulX
    #                                            2422500.0,  # ulY
    #                                            1534500.0,  # lrX
    #                                            430500.0  # lrY
    #                                          ]})
