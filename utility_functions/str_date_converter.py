from datetime import datetime


def date_converter_month_first(date_str):
    """
    Function converts a string in the format Short Month Date, Year to its date equivalent
    date object
    :param date_str:str string representation of date
    :return:date date in YYYY-mm-dd format
    """
    datetime_obj = datetime.strptime(date_str, "%b %d, %Y")

    return datetime_obj
