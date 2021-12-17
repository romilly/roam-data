import json
import unittest

from hamcrest import assert_that, contains_string
from markdown_builder.document import MarkdownDocument

from roam_data.roam.graph import Page
from roam_data.roam.to_markdown import append_entry_to_markdown
from test_helpers.helpers import page_01


class MarkdownTestCase(unittest.TestCase):
    def test_can_append_entry_to_markdown(self):
        page = Page.from_json(json.loads(page_01))
        doc = MarkdownDocument()
        append_entry_to_markdown(page, doc)
        contents = doc.contents()
        assert_that(contents, contains_string('September 27th, 2020'))
        assert_that(contents, contains_string("I'm exploring Roam"))
        assert_that(contents, contains_string("Import\n        - [[planning]]"))


if __name__ == '__main__':
    unittest.main()
