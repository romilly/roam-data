import unittest
from datetime import datetime

from hamcrest import assert_that, equal_to, contains_string, is_in

from roam_data.roam.filter_entries import find_retro_entries
from roam_data.roam.graph import Graph
from roam_data.roam.merge import merge_retros


class RetroTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.start = datetime(2021, 12, 12)
        cls.graph = Graph.from_file('data/20211215/test01.json')
        cls.entries = cls.graph.pages

        # TODO: replace with entries containing multiple retros

    def test_find_retro_items(self):
        retro_entries = find_retro_entries(self.entries)
        self.assertEqual(3, len(retro_entries))

    def test_merge_retro_entries(self):
        retros = merge_retros(find_retro_entries(self.entries))
        self.assertEqual(3, len(retros))
        ww = retros[0]
        assert_that(len(ww), equal_to(1))
        assert_that(ww[0].string, contains_string('local graph'))


if __name__ == '__main__':
    unittest.main()
