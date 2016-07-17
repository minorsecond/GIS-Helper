"""
Tools to help with various GIS tasks
Robert Ross Wardrup
"""

import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "gisHelperGui.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
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

        # Grab values from text entry boxes and convert to floats
        # TODO: Data validation
        north_y = float(self.northYEntry.text())
        south_y = float(self.southYEntry.text())
        east_x = float(self.eastXEntry.text())
        west_x = float(self.westXEntry.text())

        print(north_y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
