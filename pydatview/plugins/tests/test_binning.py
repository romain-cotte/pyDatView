import unittest
import numpy as np
import os

from pydatview.plugins.base_plugin import demoPlotDataActionPanel, HAS_WX
from pydatview.plugins.plotdata_binning import *
from pydatview.plugins.plotdata_binning import _DEFAULT_DICT

class TestBinning(unittest.TestCase):

    def test_showGUI(self):
        if not HAS_WX or not os.environ.get("DISPLAY"):
            self.skipTest("[WARN] skipping test because wx or DISPLAY is not available.")

        demoPlotDataActionPanel(BinningToolPanel, plotDataFunction=bin_plot, data=_DEFAULT_DICT, tableFunctionAdd=binTabAdd, mainLoop=False, title='Binning')


if __name__ == '__main__':
    unittest.main()
