import unittest
from datetime import datetime


from roam_data.roam.filter_entries import daily_entries_for_wc
from roam_data.roam.read_json_export import import_json


class ImportTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.start = datetime(2021, 12, 12)
        cls.json_data = import_json('data/20211215/test01.json')

    def test_import(self):
        self.assertEqual(10, len(self.json_data))

    def test_select_entries_for_wc(self):
        entries = daily_entries_for_wc(self.json_data, self.start)
        self.assertEqual(1, len(entries))






if __name__ == '__main__':
    unittest.main()
