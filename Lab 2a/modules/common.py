import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def myfunc(x):
  if x:
    a=[i for i in range (0,101,2)]
    print(a)
  else:
    a=[i for i in range(1,100,2)]
    print(a)









