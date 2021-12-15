import unittest
from datetime import datetime

from hamcrest import assert_that, equal_to, contains_string, is_in

from roam_data.roam.filter_entries import daily_entries_for_wc, find_retro_entries, merge_retro_entries
from roam_data.roam.read_json_export import import_json


class ImportTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.start = datetime(2021, 12, 12)
        cls.json_data = import_json('data/20211215/test01.json')

    def test_import(self):
        # j = import_json('data/roam/20200927/Pip.json')
        self.assertEqual(8, len(self.json_data))

    def test_select_entries_for_wc(self):
        entries = daily_entries_for_wc(self.json_data, self.start)
        self.assertEqual(1, len(entries))

    def test_find_retro_items(self):
        entries = daily_entries_for_wc(self.json_data, self.start)
        retro_entries = find_retro_entries(entries)
        self.assertEqual(1, len(retro_entries))

    def test_merge_retro_entries(self):
        retros = merge_retro_entries(find_retro_entries((daily_entries_for_wc(self.json_data, self.start))))
        self.assertEqual(3, len(retros))
        ww = retros['WW']
        assert_that(len(ww), equal_to(1))
        ww00 = ww[0][0]
        assert_that(ww00['string'], contains_string('local graph'))
        for key in ['WW','WDNW','WDD']:
            assert_that(key, is_in(retros))

    # def test_merge_handles_day_without_retro(self):
    #     entries = find_retro_entries((daily_entries_for_wc(self.json_data, datetime(2021, 12, 15))))
    #     assert_that(len(entries), equal_to(1))
    #     assert_that(entries['Test Page Two'], equal_to(([])))
    #     retros = merge_retro_entries(entries)
    #     self.assertEqual(3, len(retros))



if __name__ == '__main__':
    unittest.main()
