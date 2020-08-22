from math import modf


def origin_calc(coords):
    """
    Calculates the origin of a bounding box
    :param coords: List of tuples containing coordinates in (x,y),(x,y) format
    :return: A list of xy coords denoting origin, false if coordinate entry is
    invalid
    """

    invalid_entry = False

    for i in coords:
        if not isinstance(i, float) and not isinstance(i, int):
            print(type(i))
            invalid_entry = True

    if not invalid_entry:
        try:
            coords[0] = float(coords[0])
            coords[1] = float(coords[1])
            coords[2] = float(coords[2])
            coords[3] = float(coords[3])

            x_coord = [coords[2], coords[3]]
            y_coord = [coords[0], coords[1]]

            centroid = (sum(x_coord) / 2, sum(y_coord) / 2)
            return centroid

        except ValueError:
            return False

    return False


class Convert:
    """
    Contains methods for converting things.
    """

    @staticmethod
    def dd_to_dms(coords):
        """
        Calculates decimal degrees to degrees, minutes, seconds
        :param coords: a float (DD)
        :return: DMS coordinates
        """
        degrees = None
        minutes = None
        seconds = None
        valid = True

        try:
            input_coord = float(coords)
            if -180 <= input_coord <= 180:
                number_list = modf(input_coord)
                integer = number_list[1]
                decimal = number_list[0]

                degrees = int(integer)
                minutes = int(60 * decimal)
                seconds = abs(round(((decimal - (minutes / 60)) * 3600), 3))
            else:
                valid = False

        except TypeError as type_error:
            print(type_error)

        return degrees, minutes, seconds, valid

    @staticmethod
    def dms_to_dd(coords):
        """
        Convert dms to decimal degrees
        :return: dd
        """
        decimal_degrees = None

        try:
            coords = [int(v) if float(v).is_integer() else float(v)
                      for v in coords.split()]

            degrees = coords[0]
            minutes = coords[1]
            seconds = coords[2]

            decimal_degrees = round((degrees + (minutes / 60) +
                                     (seconds / 3600)), 8)
        except IndexError as index_error:
            print("User entered an invalid value: {}".format(coords))

        return decimal_degrees
