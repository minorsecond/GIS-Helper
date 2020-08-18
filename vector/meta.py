from matplotlib.collections import PatchCollection
from matplotlib import pyplot as plt
import shapefile
from shapely.geometry import MultiPolygon, shape
from descartes import PolygonPatch
from fiona import open as fiona_open

plt.style.use('ggplot')


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

    def display_shapefile(self, shapefile_path):
        """
        Display shape data on screen
        :return:
        """
        shp_path = shapefile_path.text()
        color_map = plt.get_cmap('RdBu')
        num_colors = 1000

        if len(shp_path) > 0:
            # try:

            # Open shape data
            shp = MultiPolygon(
                [shape(pol['geometry']) for pol in fiona_open(shp_path)]
            )

            print("Finished loading shape data")

            fig = plt.figure()
            print("Created the figure")

            # try:
            ax = fig.add_subplot(111)
            minx, miny, maxx, maxy = shp.bounds
            w, h = maxx - minx, maxy - miny
            ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
            ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
            ax.set_aspect(1)

            print("Created the plot")

            patches = []
            for idx, p in enumerate(shp):
                colour = color_map(1. * idx / num_colors)
                patches.append(PolygonPatch(p, fc=colour, ec='#555555', alpha=1., zorder=1))
                print("Adding {0} to plot.".format(idx))

            ax.add_collection(PatchCollection(patches, match_original=True))

            print("Built the graph")
            plt.show()