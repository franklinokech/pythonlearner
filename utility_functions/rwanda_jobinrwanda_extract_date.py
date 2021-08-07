import datetime
import re


def get_date_posted(s):
    """Get date posted from rwanda jobinrwanda"""
    match = re.search(r'\d{2}-\d{2}-\d{4}', s)
    post_date = datetime.datetime.strptime(match.group(), '%d-%m-%Y').date()

    return post_date
