"""
Tools to help with various GIS tasks
Robert Ross Wardrup
"""

import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "gisHelperGui.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    entries_valid = False

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.originCalculateButton.clicked.connect(self.calculateOrigin)

    def calculateOrigin(self):
        """
        Calculates the origin, given bounding box coordinates
        :return: Origin
        """

        blank_entry = False

        # Grab values from text entry boxes and convert to floats
        # TODO: Data validation
        north_y = self.northYEntry.text()
        south_y = self.southYEntry.text()
        east_x = self.eastXEntry.text()
        west_x = self.westXEntry.text()

        coordinates = (north_y, south_y, east_x, west_x)

        for i in coordinates:
            if len(i) == 1:
                blank_entry = True

        if not blank_entry:
            north_y = float(coordinates[0])
            south_y = float(coordinates[1])
            east_x = float(coordinates[2])
            west_x = float(coordinates[3])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
