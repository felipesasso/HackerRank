"""
Problem:
https://www.hackerrank.com/challenges/calendar-module/problem
"""

import calendar

month, day, year = list(map(int, input().split()))

print(list(calendar.day_name)[calendar.weekday(year, month, day)].upper())
