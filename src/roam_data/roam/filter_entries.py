from datetime import datetime
from typing import List, Optional

from roam_data.dates.dates import roam_format, dates_for_wc
from roam_data.roam.graph import Entry, Block, Page


def daily_entries_for_wc(entries: List, dt: datetime) -> List:
    dates = [roam_format(d) for d in dates_for_wc(dt)]
    return [entry for entry in entries if entry['title'] in dates]


def retro_in(entry: Entry) -> Block:
    for child in entry.children:
        if child.string  == '[[Retrospective]]':
            return child


def find_retro_entries(entries: List[Entry]) -> List[Block]:
    result = [retro_in(entry) for entry in entries if retro_in(entry)]
    return result


def retro_from(page: Page) -> Optional[Block]:
    for block in page.children:
        if block.string == '[[Retrospective]]':
            return block
    return None


def retros_in(notes: List[Page]) -> List[Block]:
    retros = [retro_from(page) for page in notes]
    return retros

