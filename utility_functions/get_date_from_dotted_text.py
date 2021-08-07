from datetime import datetime


def date_converter_date_first_dotted(date_str):
    """
    Function converts a string in the format Date Date.Month.Year to its date equivalent
    date object
    :param date_str:str string representation of date
    :return:date date in YYYY-mm-dd format
    """
    datetime_obj = datetime.strptime(date_str, "%d.%m.%Y")

    return datetime_obj

print(date_converter_date_first_dotted('28.07.2021'))
