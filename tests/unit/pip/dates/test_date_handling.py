import unittest
from datetime import datetime

from hamcrest import assert_that, equal_to, none

from roam_data.dates.dates import convert_millis, date_from, dates_for_wc, roam_format, roam_date


class DatesTestCase(unittest.TestCase):
    def test_convert_millis(self):
        expected = datetime(2020, 9, 27, 18, 3, 31, 424000)
        self.assertEqual(expected, convert_millis((1601226211424)))

    def test_date_parsing(self):
        expected = datetime(2020, 9, 27)
        self.assertEqual(expected, date_from('20200927'))

    def test_date_in_roam_format(self):
        dt = datetime(2020, 9, 27)
        self.assertEqual('September 27th, 2020', roam_format(dt))

    def test_days_for_wc(self):
        sunday = 20211205
        for i in range(7):
            day = date_from(str(sunday+i))
            actual_dates = dates_for_wc(day)
            expected_dates = [datetime(2021, 12, i+5) for i in range(7)]
            self.assertEqual(7, len(actual_dates))
            for (expected, actual) in zip(expected_dates, actual_dates):
                self.assertEqual(expected, actual)

    def test_is_roam_date(self):
        assert_that(roam_date('December 13th, 2021'), equal_to(datetime(2021, 12, 13)))
        assert_that(roam_date('W/c December 13th, 2021'), none())
        assert_that(roam_date('December 2021'), none())


if __name__ == '__main__':
    unittest.main()
