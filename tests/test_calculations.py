from gh import *


def test_dd_to_dms():
    print(dd_to_dms(38.898556))
    print(dd_to_dms(-77.037852))
    assert dd_to_dms(38.898556) == (38, 53, 54.802)
    assert dd_to_dms(-77.037852) == (-77, -2, 16.267)
    assert dd_to_dms(180.001) == False


def test_origin_calculation():
    coordinates = [43.7291, 26.2946, 43.8058, 26.3759]
    assert origin_calc(coordinates) == '43.76745, 26.33525'

if __name__ == '__main__':
    test_dd_to_dms()