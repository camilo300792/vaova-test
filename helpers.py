import re

VALID_TITLE_REGEX = r'\d'
VALID_URL_REGEX = r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
VALID_EMAIL_REGEX = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'

def contain_numbers(string):
    if (re.fullmatch(VALID_TITLE_REGEX, string)):
        raise Exception('Invalid format string!');
    return string

def valid_url(url):
    if (re.fullmatch(VALID_URL_REGEX, url)):
        raise Exception('Invalid URL!');
    return url

def valid_email(email):
    if (re.fullmatch(VALID_EMAIL_REGEX, email)):
        raise Exception('Invalid email!');
    return email
