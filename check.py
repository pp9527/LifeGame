"""
check
"""
import sys


def check_int(date):
    """
    :param date:str
    :return: int
    """
    try:
        int(date)
    except ValueError:
        print('error')
        sys.exit(0)
    date = int(date)
    if date < 1:
        print('error')
        sys.exit(0)
    else:
        return date
