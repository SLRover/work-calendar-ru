# -*- coding: utf-8 -*-

import datetime
from work_calendar_ru.data import holidays
from work_calendar_ru.data.time import work_hours

# day_types = ('holiday', 'short_work_day', 'work_day', 'work_weekend', 'weekend')
# weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

current_day = datetime.date.today()
current_time = datetime.datetime.now().time()


def is_work_time():
    if current_day not in holidays.holidays and current_day.weekday() not in (5, 6) \
            and work_hours[0] <= current_time <= work_hours[1]:
        return True
    else:
        return False


def is_holiday():
    if current_day in holidays.holidays:
        return True
    else:
        return False


def is_work_day():
    if (current_day not in holidays.holidays and current_day.weekday() not in (5, 6)) or \
            (current_day not in holidays.holidays and current_day in holidays.work_weekends):
        return True
    else:
        return False


def is_short_work_day():
    if current_day in holidays.short_days:
        return True
    else:
        return False


def is_work_weekend():
    if current_day in holidays.work_weekends:
        return True
    else:
        return False


def is_weekend():
    if current_day.weekday() in (5, 6) and current_day not in holidays.work_weekends:
        return True
    else:
        return False
