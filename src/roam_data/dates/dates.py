import calendar
from datetime import datetime, timedelta
import re

from num2words import num2words

month_names = list(calendar.month_name[month + 1] for month in range(12))
month_matches = '|'.join(month_names)
suffices = "(st|nd|rd|th)"
match_string = "^(%s) (\d\d?)%s, (\d\d\d\d)" % (month_matches, suffices)
roam_date_matcher = re.compile(match_string)


def convert_millis(millis: int) -> datetime:
    return datetime.fromtimestamp(millis / 1000)


def date_from(yyyymmdd :str):
    return datetime.strptime(yyyymmdd, '%Y%m%d')


def start_of_week_containing(day: datetime):
    return day - timedelta(days=day.isoweekday() % 7)


def dates_for_wc(day: datetime):
    wc = start_of_week_containing(day)
    return [wc + timedelta(days=i) for i in range(7)]


def roam_format(dt: datetime):
    raw= dt.strftime('%B/%d/%Y')
    month, day_num, year = raw.split('/')
    day_ordinal = num2words(int(day_num), to="ordinal_num")
    return '%s %s, %s' % (month, day_ordinal, year)


def roam_date(title: str):
    rd = roam_date_matcher.search(title)
    if not rd:
        return None
    month = 1+month_names.index(rd.group(1))
    day = int(rd.group(2))
    year = int(rd.group(4))
    return datetime(year, month, day)





