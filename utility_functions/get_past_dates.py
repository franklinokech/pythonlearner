from datetime import timedelta, date
import re

# Using current time
ini_time_for_now = date.today()

print(ini_time_for_now)

# month to days converter
month_to_days = 30


def get_number_from_str(date_str):
    """
    Gets past date given a string representing past dates
    like 1day ago

    :param date_str: string containing timedelta
    :return x: int number in the timedelta
    """
    x = int(re.findall('[0-9]+', date_str)[0])
    return x


def get_number_from_str(date_str):
    """

    :param date_str: string containing timedelta
    :return x: int number in the timedelta
    """
    x = int(re.findall('[0-9]+', date_str)[0])
    return x


def get_past_date(past_date):
    # retrieve the time elapsed from the datetime string
    past_time = get_number_from_str(past_date)

    # check if 'd' in past date
    if 'd' in past_date:
        past_date = ini_time_for_now - timedelta(days=past_time)

    elif 'h' in past_date:
        past_date = ini_time_for_now - timedelta(hours=past_time)

    elif 'w' in past_date:
        past_date = ini_time_for_now - timedelta(weeks=past_time)

    elif 'mo' in past_date or 'mos' in past_date:
        # convert months to days
        past_time *= month_to_days

        past_date = ini_time_for_now - timedelta(days=past_time)

    return past_date


print(get_past_date('6mos'))
