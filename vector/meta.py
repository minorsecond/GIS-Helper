class PolygonFunctions:
    """
    Contains the IO functions
    """

    def load_polygons(self, payload):
        """
        Loads polygons into memory
        :return:
        """

        self.input_file = payload[0]
        self.shapefile_directory = payload[1]
        self.output_directory = payload[2]

        shp = shapefile.Reader(self.shapefile_directory)
        self.shapes = shp.shapes()

    def get_polygon_vertices(self, payload):
        """
        Gets vertex locations for polygons
        :return:
        """

        self.vertices = []

        self.load_polygons(payload)

        for polygon in self.shapes:
            self.vertices.append(polygon.points)

        print(self.vertices)