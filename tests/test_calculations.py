from gh import *


def test_dd_to_dms():
    assert dd_to_dms(38.898556) == (38, 53, 55)
    assert dd_to_dms(-77.037852) == (77, 2, 16)
    assert dd_to_dms(100.123456) == False


def test_origin_calculation():
    coordinates = [43.7291, 26.2946, 43.8058, 26.3759]
    assert origin_calc(coordinates) == '43.76745, 26.33525'
