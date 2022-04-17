import unittest

from get_rates import get_swans_rates


class TestDatabase(unittest.TestCase):
    """
    Class for testing parsing json
    """
    TEST_FILE_NAME = "../test_data.json"

    def test_get_swans_rates(self):
        result = get_swans_rates(TestDatabase.TEST_FILE_NAME)
        self.assertEqual(result, {"a": [0.1, 0.23], "b": [0.1, 0.24], "c": [0.1, 0.55], "d": [0.1, 0.90]})
