import unittest
import numpy as np
import os

from pydatview.plugins.base_plugin import demoPlotDataActionPanel, HAS_WX
from pydatview.plugins.plotdata_sampler import *
from pydatview.plugins.plotdata_sampler import _DEFAULT_DICT

class TestSampler(unittest.TestCase):

    def test_showGUI(self):
        if not HAS_WX or not os.environ.get("DISPLAY"):
            self.skipTest("[WARN] skipping test because wx or DISPLAY is not available.")

        demoPlotDataActionPanel(SamplerToolPanel, plotDataFunction=samplerXY, data=_DEFAULT_DICT, tableFunctionAdd=samplerTabAdd, mainLoop=False, title='Sampler')

if __name__ == '__main__':
    unittest.main()

