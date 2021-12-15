from collections import defaultdict
from datetime import datetime
from typing import List

from roam_data.dates.dates import roam_format, dates_for_wc


def daily_entries_for_wc(entries: List, dt: datetime) -> List:
    dates = [roam_format(d) for d in dates_for_wc(dt)]
    return [entry for entry in entries if entry['title'] in dates]


def find_retro_entries(entries: List):
    result = {}
    for entry in entries:
        children = entry['children']
        retro = [child for child in children if child['string'] == '[[Retrospective]]']
        result[entry['title']] = retro
    return result


def merge_retro_entries(entries: List):
    keys = ['WW','WDNW', 'WDD']
    result = defaultdict(list)
    for entry_date in entries:
        entry = entries[entry_date]
        if entry:
            children = entry[0]['children'][:3]
            for (key, item) in zip(keys, children):
                if 'children' in item:
                    kids = item['children']
                    result[key].append(kids)
    return result


