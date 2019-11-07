# -*- coding: utf-8 -*-

import datetime
from work_calendar_ru.data import holidays


class WCR:
    """Checking current day or time methods"""

    def __init__(self, start_hour, start_minutes, end_hour, end_minutes):
        self.start_hour = start_hour
        self.start_minutes = start_minutes
        self.end_hour = end_hour
        self.end_minutes = end_minutes
        self.current_day = datetime.date.today()
        self.current_time = datetime.datetime.now().time()

    def is_work_time(self):
        work_hours = (
            datetime.time(self.start_hour, self.start_minutes, 0),
            datetime.time(self.end_hour, self.end_minutes, 0)
        )

        if self.current_day not in holidays.holidays and self.current_day.weekday() not in (5, 6) \
                and work_hours[0] <= self.current_time <= work_hours[1]:
            return True
        else:
            return False

    def is_holiday(self):
        if self.current_day in holidays.holidays:
            return True
        else:
            return False

    def is_work_day(self):
        if (self.current_day not in holidays.holidays and self.current_day.weekday() not in (5, 6)) or \
                (self.current_day not in holidays.holidays and self.current_day in holidays.work_weekends):
            return True
        else:
            return False

    def is_short_work_day(self):
        if self.current_day in holidays.short_days:
            return True
        else:
            return False

    def is_work_weekend(self):
        if self.current_day in holidays.work_weekends:
            return True
        else:
            return False

    def is_weekend(self):
        if self.current_day.weekday() in (5, 6) and self.current_day not in holidays.work_weekends:
            return True
        else:
            return False
