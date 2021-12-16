import json
import unittest

from hamcrest import assert_that, equal_to, instance_of, greater_than

from roam_data.roam.graph import Page, DailyNotesPage, OrdinaryPage, Graph
from test_helpers.helpers import page_01, page_02


class PageTestCase(unittest.TestCase):
    def test_page_can_convert_daily_notes(self):
        page = Page.from_json(json.loads(page_01))
        # noinspection PyTypeChecker
        assert_that(page, instance_of(DailyNotesPage))
        assert_that(page.title, equal_to('September 27th, 2020'))
        assert_that(len(page.children), equal_to(8))

    def test_page_can_convert_ordinary_page(self):
        page = Page.from_json(json.loads(page_02))
        # noinspection PyTypeChecker
        assert_that(page, instance_of(OrdinaryPage))
        assert_that(page.title, equal_to('weekly plan'))

    def test_page_can_convert_export(self):
        with open('data/20211215/test01.json') as pip:
            export = json.load(pip)
            graph = Graph.from_json(export)
            assert_that(len(graph.pages), equal_to(10))
            assert_that(len(graph.uids), equal_to(49))


if __name__ == '__main__':
    unittest.main()
