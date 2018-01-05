#!/usr/bin/python3
"""
DECIMAL TIME
============

About
=====
1 year = 10 months
1 week = 10 days
1 day = 10 hours
1 hour = 100 minutes
1 minute = 100 seconds

=> 1 second = 0.864 standard SI seconds.
=> 1 month = 3~4 weeks.

Years start at 1970 Jan 1.

Usage
=====

$ python detime.py
0048-01-05 00:96:92.19870...

>>> from detime import Date
>>> Date(1970, 1, 1)
0000-01-01 00:00:0.00000

>>> Date(1977, 3, 5, 23, 55, 30)
0007-02-28 09:96:87.50000

"""

import copy
import datetime
import calendar


class Constants:
    origin_date = datetime.datetime(1970, 1, 1, 0, 0)
    year_length = 365
    month_lengths = [36, 37] * 5
    second_length = 0.864

constant = Constants()


class Date:

    def __init__(self, *args):

        self.origin = constant.origin_date
        self.get_current_date(*args)
        self.compute_date()

    def compute_date(self):
        self.year = (self.date.year - self.origin.year)
        self.yday = self.date.timetuple().tm_yday
        self.month = self.get_month()
        self.day = self.yday - sum(self.month_lengths[:self.month][:-1]) \
            or self.month_lengths[self.month]

        self.tseconds = self.get_day_seconds() / constant.second_length
        self.hour = int(self.tseconds/10000.)
        self.minute = int((self.tseconds - self.hour*10000.) / 100.)
        self.second = self.tseconds - (self.hour*10000. + self.minute*100)

    def get_current_date(self, *args):
        if args:
            self.date = datetime.datetime(*args)
        else:
            self.date = datetime.datetime.utcnow()
        return self.date

    def get_time_delta(self):
        self.delta = self.date - self.origin

    def get_month(self):
        for i, month_length in enumerate(self.get_month_lengths()):
            if sum(self.month_lengths[:i+1]) >= self.yday:
                break
        return i+1

    def get_year_length(self):
        year_length = constant.year_length

        if calendar.isleap(self.date.year):
            year_length += 1
        self.year_length = year_length
        return self.year_length

    def get_month_lengths(self):

        if calendar.isleap(self.date.year):
            self.month_lengths = copy.copy(constant.month_lengths)
            self.month_lengths[-1] += 1
            return self.month_lengths
        else:
            self.month_lengths = copy.copy(constant.month_lengths)
            return self.month_lengths

    def get_unix_seconds(self):
        self.get_time_delta()
        return self.delta.total_seconds()

    def get_day_seconds(self):
        midnight = self.date.replace(hour=0, minute=0, second=0, microsecond=0)
        return (self.date - midnight).total_seconds()

    def __repr__(self):
        return '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02.5f}'.format(
            self.year, self.month, self.day,
            self.hour, self.minute, self.second
        )


if __name__ == '__main__':
    import time
    while True:
        tm = time.gmtime()
        date = Date()
        print("[{:04d}-{:02d}-{:02d} =] {} [= {:02d}:{:02d}:{:02d}]".format(
            tm.tm_year, tm.tm_mon, tm.tm_mday, date, tm.tm_hour, tm.tm_min, tm.tm_sec
        ), end='\r', flush=True)
        del date
