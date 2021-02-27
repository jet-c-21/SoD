"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/27/21
"""
# coding: utf-8
import datetime


def get_week_data(first_day: datetime.datetime, last_day: datetime.datetime) -> list:
    result = list()

    head_of_week = first_day

    week_type = 'single'
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

        record = {
            'week_type': week_type,
            'head': days_of_week[0],
            'tail': days_of_week[-1],
            'days': days_of_week
        }
        result.append(record)

        if head_of_week < last_day:
            head_of_week += datetime.timedelta(days=1)

            if week_type == 'single':
                week_type = 'dual'
            else:
                week_type = 'single'

        else:
            flag = False

    return result


def s_or_d(week_data: list):
    curr_time = datetime.datetime.now()
    curr_y = curr_time.year
    curr_m = curr_time.month
    curr_d = curr_time.day
    for d in week_data:
        week_type = d['week_type']
        week_of_head = d['head']
        week_of_tail = d['tail']

        y = week_of_head.year
        m = week_of_head.month

        hd = week_of_head.day
        td = week_of_tail.day

        if (curr_y, curr_m) == (y, m):
            if hd <= curr_d <= td:
                return week_type

    msg = 'queried date is out of range'
    print(msg)


fd = datetime.datetime(2021, 2, 25)
ld = datetime.datetime(2021, 7, 31)

wd = get_week_data(fd, ld)
x = s_or_d(wd)
print(x)
