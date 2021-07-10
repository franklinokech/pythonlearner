from datetime import datetime


def date_converter_date_first(date_str):
    """
    Function converts a string in the format Date Short Month, Year to its date equivalent
    date object
    :param date_str:str string representation of date
    :return:date date in YYYY-mm-dd format
    """
    datetime_obj = datetime.strptime(date_str, "%d %b, %Y")

    return datetime_obj

print(date_converter_date_first('08 Jul 2021'))
