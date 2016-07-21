from gh.py import GisHelper.dd_to_dms
def test_dd_to_dms():
	assert dd_to_dms(38.898556) == '38d, 53m, 55s'
	assert dd_to_dms(-77.037852) == '77d, 2m, 16s'
	assert dd_to_dms(100.123456) == 'Invalid entry'
