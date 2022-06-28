"""Написати функцію, яка повертає поточний час. І обернути її у декоратор
  який відрахує 3 секунди."""

from datetime import datetime
from time import sleep

def wait():
    for i in range(3, 0, -1):
        sleep(1)
        print(i)


wait()
time = datetime.now().strftime('%H:%M')
print(time)

