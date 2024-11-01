import sys
import os
import unittest
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import load_data, data_visualization

class TestCase(unittest.TestCase):

    @patch('matplotlib.pyplot.show')
    def test_data_visualization_with_csv(self, mock_show):

        print("Current Working Directory:", os.getcwd())

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'dataset.csv'))

        print("Dataset file path:", file_path)

        data = load_data(file_path)

        self.assertIsInstance(data, pd.DataFrame, "Loaded data should be a pandas DataFrame")
        self.assertFalse(data.empty, "The dataset should not be empty")

        data_visualization(data)

        fig = plt.gcf()
        self.assertEqual(fig.get_size_inches().tolist(), [12, 6],
                         "The figure size should be (12, 6)")

        ax = plt.gca()
        self.assertEqual(ax.get_xlabel(), 'platform', "x should be 'platform'")

        legend = ax.get_legend()
        self.assertIsNotNone(legend, "Legend should exist")
        self.assertEqual(legend.get_title().get_text(), 'genre', "hue should be 'genre'")

        mock_show.assert_called_once()

#if __name__ == "__main__":
#    unittest.main()
