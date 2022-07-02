"""Написати функцію, яка повертає поточний час. І обернути її у декоратор
  який відрахує 3 секунди."""

from datetime import datetime
from time import sleep


def counter(function):

    def wrap(*args, **kwargs):
        for sec in range(3, 0, -1):
            print(sec)
            sleep(1)
        function(*args, **kwargs)
    return wrap


@counter
def time_now():
    time = datetime.now().strftime('%H:%M')
    print(time)


if __name__ == '__main__':
    time_now()
