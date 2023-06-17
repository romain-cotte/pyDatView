import unittest
import numpy as np
import os

from pydatview.plugins.base_plugin import demoPlotDataActionPanel, HAS_WX
from pydatview.plugins.plotdata_filter import *
from pydatview.plugins.plotdata_filter import _DEFAULT_DICT

class TestFilter(unittest.TestCase):

    def test_showGUI(self):
        if not HAS_WX or not os.environ.get("DISPLAY"):
            self.skipTest("[WARN] skipping test because wx or DISPLAY is not available.")

        demoPlotDataActionPanel(FilterToolPanel, plotDataFunction=filterXY, data=_DEFAULT_DICT, tableFunctionAdd=filterTabAdd, mainLoop=False, title='Filter')



if __name__ == '__main__':
    unittest.main()


