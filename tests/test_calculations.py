from gh import GisHelper
GisHelper = GisHelper()

def test_dd_to_dms():
	assert GisHelper.dd_to_dms(38.898556) == '38d, 53m, 55s'
	assert GisHelper.dd_to_dms(-77.037852) == '77d, 2m, 16s'
	assert GisHelper.dd_to_dms(100.123456) == 'Invalid entry'

def test_origin_calculation():
	coordinates = [(43.7291, 26.2946), (43.8058, 26.3759)]
	assert GisHelper.calculate_origin(coordinates) == '43.76745, 26.33525'
