"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/27/21
"""
# coding: utf-8
import datetime


class Day(datetime.datetime):
    def __init__(self, year, month, day):
        # super().__init__(year, month, day)
        self.year_str = str(self.year).zfill(4)
        self.month_str = str(self.month).zfill(2)
        self.day_str = str(self.day).zfill(2)
        self.hour_str = str(self.hour).zfill(2)
        self.minute_str = str(self.minute).zfill(2)
        self.second_str = str(self.second).zfill(2)


class FirstDay(Day):
    def __str__(self):
        s = f"FirstDay<{id(self)}> : {self.year_str}-{self.month_str}-{self.day_str} " \
            f"{self.hour_str}:{self.minute_str}:{self.second_str}"
        return s


class LastDay(Day):
    def __str__(self):
        s = f"LastDay<{id(self)}> : {self.year_str}-{self.month_str}-{self.day_str} " \
            f"{self.hour_str}:{self.minute_str}:{self.second_str}"
        return s


def get_week_data(first_day: datetime.datetime, last_day: datetime.datetime):
    week = list()

    head_of_week = first_day
    flag = True
    while flag:
        days_of_week = list()

        # find Monday in that week
        week_day = head_of_week.isoweekday()
        if week_day != 1:
            back_days = 1 - week_day
            head_of_week += datetime.timedelta(days=back_days)

        days_of_week.append(head_of_week)
        for _ in range(6):
            head_of_week = head_of_week + datetime.timedelta(days=1)
            days_of_week.append(head_of_week)

        print(days_of_week[0].isoweekday(), days_of_week[-1].isoweekday())

        if head_of_week < last_day:
            head_of_week += datetime.timedelta(days=1)
        else:
            flag = False


fd = datetime.datetime(2021, 2, 25)
ld = datetime.datetime(2021, 7, 31)

get_week_data(fd, ld)