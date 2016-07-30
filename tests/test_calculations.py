from gh import *

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

    path = '/home/rwardrup/DEV/gis-helper/'
    results = CalculateRasterBounds(path)
    print(results)

    assert results == (1, {'/home/rwardrup/DEV/gis-helper/n19_ak13_106112_ndvi.tif': [-977500.0,  # ulX
                                                                                  2422500.0,  # ulY
                                                                                  1534500.0,  # lrX
                                                                                  430500.0  # lrY
                                                                                      ]})
