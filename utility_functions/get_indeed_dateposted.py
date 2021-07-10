import re

regex = r"\d+"
if re.search(regex, date_posted_details):
    match = re.search(regex, date_posted_details)
    match_result = match.group(0)
    days_ago = int(match_result)
    date_posted = ini_time_for_now - timedelta(days=days_ago)
else:
    date_posted = ini_time_for_now