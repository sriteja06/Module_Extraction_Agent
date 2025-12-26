import re

def is_valid_url(url):
    url_pattern = r"https?://[A-Za-z0-9\./\-\_]+"
    return bool(re.match(url_pattern, url))
