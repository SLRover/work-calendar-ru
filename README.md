# Russian work calendar

# Description
Simple library for checking current day as a holiday or weekend and current time as a working time or not.

## Setup
`pip install work_calendar_ru`

## Import package
`from work_calendar_ru import WCR`

## Using package
`wcr = WCR(start_hour=9, start_minutes=0, end_hour=19, end_minutes=30)`

Where `start_hour` and `start_minutes` is a time of the start of working day.

Therefore `end_hour` and `end_minutes` is a time of the end of working day.

* Work time now `wcr.is_work_time()`
* Holiday today `wcr.is_holiday()`
* Work day today `wcr.is_work_day()`
* Short work day today `wcr.is_short_work_day()`
* Work weekend day today `wcr.is_work_weekend()`
* Weekend day today `wcr.is_weekend()`

## License
MIT license