import sys
import os
import unittest
import pandas as pd
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from task import load_data, explore_data

class TestCase(unittest.TestCase):
    def test_load_data(self):

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'dataset.csv'))

        print("Dataset file path:", file_path)

        data = load_data(file_path)

        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

    @patch('sys.stdout', new_callable=StringIO)
    def test_explore_data_output(self, mock_stdout):

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'dataset.csv'))

        print("Dataset file path:", file_path)

        data = load_data(file_path)

        explore_data(data)

        output = mock_stdout.getvalue()

        self.assertIn(str(data.head()), output)
        self.assertIn('RangeIndex', output)


if __name__ == "__main__":
    unittest.main()
