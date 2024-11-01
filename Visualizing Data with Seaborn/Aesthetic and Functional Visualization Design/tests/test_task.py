import sys
import os
import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import load_data, data_visualization

class TestCase(unittest.TestCase):

    @patch('matplotlib.pyplot.show')
    def test_data_visualization_with_theme_and_legend(self, mock_show):
        sns.set_theme(style="darkgrid")

        print("Current Working Directory:", os.getcwd())

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'dataset.csv'))

        print("Dataset file path:", file_path)

        data = load_data(file_path)

        self.assertIsInstance(data, pd.DataFrame, "Loaded data should be a pandas DataFrame")
        self.assertFalse(data.empty, "The dataset should not be empty")

        data_visualization(data)

        ax = plt.gca()
        legend = ax.get_legend()

        self.assertIsNotNone(legend, "Legend should exist")
        self.assertEqual(legend.get_title().get_text(), 'genre', "Legend title should be 'genre'")

        bbox = legend.get_window_extent()
        bbox_normalized = bbox.transformed(ax.transAxes.inverted())

        tolerance = 0.01
        self.assertAlmostEqual(bbox_normalized.x0, 1, delta=tolerance, msg="Legend should be positioned at x=1")

        self.assertGreater(bbox_normalized.y0, 0, msg="Legend y-position should be greater than 0")
        self.assertLess(bbox_normalized.y0, 1, msg="Legend y-position should be less than 1")

        self.assertAlmostEqual(legend.get_frame().get_facecolor()[0], 1.0, msg="Legend background color should be white")
        self.assertAlmostEqual(legend.get_frame().get_facecolor()[1], 1.0, msg="Legend background color should be white")
        self.assertAlmostEqual(legend.get_frame().get_facecolor()[2], 1.0, msg="Legend background color should be white")
        self.assertAlmostEqual(legend.get_frame().get_facecolor()[3], 0.8, msg="Legend should have an alpha of 0.8")

        mock_show.assert_called_once()

if __name__ == "__main__":
    unittest.main()
