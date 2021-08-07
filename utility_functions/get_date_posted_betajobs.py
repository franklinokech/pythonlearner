from datetime import timedelta, date, datetime
import re

# Using current time
ini_time_for_now = date.today()


def get_number_from_str(date_str):
    """

    :param date_str: string containing timedelta
    :return x: int number in the timedelta
    """
    x = int(re.findall('[0-9]+', date_str)[0])
    return x


def get_past_date(past_date):
    past_date.lower()
    # retrieve the time elapsed from the datetime string
    past_time = get_number_from_str(past_date)

    if 'now' in past_date:
        past_date = ini_time_for_now

    elif 'minute' in past_date:
        past_date = ini_time_for_now - timedelta(hours=past_time)

    elif 'hour' in past_date:
        past_date = ini_time_for_now - timedelta(hours=past_time)

    elif 'yesterday' in past_date:
        past_date = ini_time_for_now - timedelta(days=1)

    elif 'day' in past_date:
        past_date = ini_time_for_now - timedelta(days=past_time)

    else:
        current_year = '2021'
        sep = ' '
        date_str = past_date + sep + current_year
        past_date = datetime.strptime(date_str, "%B %d %Y")

    return past_date

