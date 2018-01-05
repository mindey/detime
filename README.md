# DECIMAL TIME

## Usage

```bash
>>> from detime import Date
>>> Date(1970, 1, 1)
0000-01-01 00:00:0.00000

>>> Date(1977, 3, 5, 23, 55, 30)
0007-02-28 09:96:87.50000
```
[Demo (1.8M) (MP4)](https://github.com/mindey/detime/blob/master/media/about.mp4?raw=true).

## About

In childhood, I tried to simplify computation of time for myself, so I
invented a decimal system for counting time.

1 year = 10 months<br>
1 week = 10 days<br>
1 day = 10 hours<br>
1 hour = 100 minutes<br>
1 minute = 100 seconds

=> 1 second = 0.864 standard SI seconds.<br>
=> 1 month = 3~4 weeks.

Years start at 1970 Jan 1, midnight.
