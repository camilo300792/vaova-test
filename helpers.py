import re

VALID_URL_REGEX = r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
VALID_EMAIL_REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def contain_numbers(string):
    if (re.search(r'\d', string)):
        raise Exception("String can't contain numbers");
    return string

def valid_url(url):
    if (re.fullmatch(VALID_URL_REGEX, url)):
        raise Exception('Invalid URL!');
    return url

def valid_email(email):
    if (re.fullmatch(VALID_EMAIL_REGEX, email) is False):
        raise Exception('Invalid email!');
    return email
