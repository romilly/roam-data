import json
from abc import ABC
from datetime import datetime
from typing import List

from roam_data.dates.dates import convert_millis, roam_date


class Graph:
    def __init__(self, pages: List['Page']):
        self.pages = pages
        self.created = {}
        self.page_titles = {}
        self.uids = {}
        for page in pages:
            self.created[page.create_time] = page
            self.page_titles[page.title] = page
            self.uids.update(page.uids)

    @classmethod
    def from_json(cls, json) -> 'Graph':
        pages = list(Page.from_json(page) for page in json)
        return Graph(pages)

    @classmethod
    def from_file(cls, file_name) -> 'Graph':
        with open(file_name) as graph_file:
            return Graph.from_json(json.load(graph_file))


class Entry(ABC):
    def __init__(self):
        self.create_time = None
        self.edit_time = None
        self.children = []
        self.uids = {}

    def convert_children(self, json):
        if 'children' in json:
            children = [Block.from_json(child) for child in json['children']]
            for child in children:
                self.uids.update(child.uids)
        else:
            children = []
        return children


    @classmethod
    def get_time(cls, json, key):
        result = None
        if key in json:
            result = convert_millis(int(json[key]))
        return result

    def insert(self, json: dict) -> 'Entry':
        ct = self.get_time(json, 'create-time')
        self.edit_time = self.get_time(json, 'edit-time')
        if ct:
            self.create_time = ct
        if self.create_time is None:
            self.create_time = self.edit_time
        self.children = self.convert_children(json)
        return self


class Page(Entry, ABC):
    def __init__(self, title: str):
        Entry.__init__(self)
        self.title = title

    @classmethod
    def from_json(cls, json) -> 'Page':
        title=json['title']
        note_date = roam_date(title)
        if note_date:
            result =  DailyNotesPage(title, note_date)
        else:
            result = OrdinaryPage(title)
        # noinspection PyTypeChecker
        # in this context, returns a subclass of page, not an entry!
        return result.insert(json)


class DailyNotesPage(Page):
    def __init__(self, title, note_date: datetime):
        Page.__init__(self, title)
        self.note_date = note_date
        self.create_time = note_date


class OrdinaryPage(Page):
    pass


class Block(Entry):
    def __init__(self, string: str, uid: str):
        Entry.__init__(self)
        self.string = string
        self.uid = uid
        self.uids = {uid: self}

    def __repr__(self):
        return 'Block(%s, %s)' % (self.string, self.uid)

    @classmethod
    def from_json(cls, json):
        return Block(string=json['string'], uid=json['uid']).insert(json)
