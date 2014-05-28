import functools
import sys
import requests
from requests import exceptions


def catch_exception(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except YotaError as e:
            print("Something went wrong with Yota" + str(e))
            sys.exit("Will retry after a wile")
        except requests.exceptions.Timeout:
            print("The request timed out")
        except requests.exceptions.RequestException as e:
            print(e)
        except Exception as e:
            print('Caught an exception in', f.__name__)
            print(e)
            sys.exit("Bye...")
    return func


class YotaError(Exception):
    def __init__(self, arg):
      self.args = arg