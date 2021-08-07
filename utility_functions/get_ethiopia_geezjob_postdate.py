from datetime import timedelta, date
import re

# Using current time
ini_time_for_now = date.today()

# month to days converter
year_to_day = 365
month_to_days = 30
week_to_days = 7
yesterday_to_days = 1


def get_number_from_str(date_str):
    """

    :param date_str: string containing timedelta
    :return x: int number in the timedelta
    """
    x = int(re.findall('[0-9]+', date_str)[0])
    return x


def get_past_date(past_date):
    # retrieve the time elapsed from the datetime string
    try:
        past_time = get_number_from_str(past_date.lower())
    except:
        past_time = yesterday_to_days

    # check if 'day' in past date
    if 'day' in past_date:
        past_date = ini_time_for_now - timedelta(days=past_time)

    elif 'hour' in past_date:
        past_date = ini_time_for_now - timedelta(hours=past_time)

    elif 'yesterday' in past_date:
        past_date = ini_time_for_now - timedelta(days=past_time)

    elif 'week' in past_date:
        past_time *= week_to_days
        past_date = ini_time_for_now - timedelta(days=past_time)

    elif 'month' in past_date:
        # convert months to days
        past_time *= month_to_days
        past_date = ini_time_for_now - timedelta(days=past_time)

    elif 'year' in past_date:
        # convert months to days
        past_time *= year_to_day
        past_date = ini_time_for_now - timedelta(days=past_time)

    else:
        past_date = ini_time_for_now

    return past_date


print(get_past_date('3 hours'))
