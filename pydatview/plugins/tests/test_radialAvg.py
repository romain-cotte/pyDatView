import unittest
import numpy as np
import os

from pydatview.plugins.base_plugin import demoGUIPlugin, HAS_WX
from pydatview.plugins.data_radialavg import *
from pydatview.plugins.data_radialavg import _DEFAULT_DICT

class TestRadialAvg(unittest.TestCase):

    def test_showGUI(self):
        if not HAS_WX or not os.environ.get("DISPLAY"):
            self.skipTest("[WARN] skipping test because wx or DISPLAY is not available.")

        demoGUIPlugin(RadialToolPanel, actionCreator=radialAvgAction, mainLoop=False, title='Radial Avg')

if __name__ == '__main__':
    unittest.main()

