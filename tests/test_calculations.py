from gh import *


def test_dd_to_dms():
    assert dd_to_dms(38.898556) == (38, 53, 54.802, True)
    assert dd_to_dms(-77.037852) == (-77, -2, 16.267, True)
    assert dd_to_dms(180.001) == (None, None, None, False)


def test_origin_calculation():
    coordinates = [0.0, 10.0, 0.0, 10.0]
    assert origin_calc(coordinates) == (5.0, 5.0)

if __name__ == '__main__':
    test_origin_calculation()