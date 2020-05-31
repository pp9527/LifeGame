"""
check
"""


def check_int(date):
    """
    :param date:str
    :return: int
    """
    try:
        int(date)
    except ValueError:
        return -1
    date = int(date)
    if date < 1:
        return -1
    else:
        return date
