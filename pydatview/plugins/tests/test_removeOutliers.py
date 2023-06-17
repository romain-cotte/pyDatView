import unittest
import numpy as np
import os

from pydatview.plugins.base_plugin import demoPlotDataActionPanel, HAS_WX
from pydatview.plugins.plotdata_removeOutliers import *
from pydatview.plugins.plotdata_removeOutliers import _DEFAULT_DICT

class TestRemoveOutliers(unittest.TestCase):

    def test_showGUI(self):
        if not HAS_WX or not os.environ.get("DISPLAY"):
            self.skipTest("[WARN] skipping test because wx or DISPLAY is not available.")

        demoPlotDataActionPanel(RemoveOutliersToolPanel, plotDataFunction=removeOutliersXY, data=_DEFAULT_DICT, mainLoop=False, title='Remove Outliers')


if __name__ == '__main__':
    unittest.main()


