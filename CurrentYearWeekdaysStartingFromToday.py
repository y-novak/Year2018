# https://repl.it/@YaroslavNovak/CurrentYearWeekdaysStartingFromToday

import datetime

today = datetime.date.today()
last_day = today.replace(month=12, day=31)


def is_weekday(day):
    return day.weekday() < 5


nextday = today
while nextday <= last_day:
    print(nextday.strftime("%m/%d/%Y") if is_weekday(nextday) else '')
    nextday += datetime.timedelta(days=1)
