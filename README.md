# DECIMAL TIME

## About

In childhood, I tried to simplify computation of time for myself, so I
invented a decimal system for counting time.

1 year = 10 months
1 week = 10 days
1 day = 10 hours
1 hour = 100 minutes
1 minute = 100 seconds

=> 1 second = 0.864 standard SI seconds.
=> 1 month = 3~4 weeks.

Years start at 1970 Jan 1, midnight.

## Usage

```python
>>> from detime import Time
>>> Time(1970, 1, 1)
0000-01-01 00:00:0.00000

>>> Time(1977, 3, 5, 23, 55, 30)
0007-02-28 09:96:87.50000
```