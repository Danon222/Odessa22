"""У додатку є json файл. Написати програму, яка прочитає його та порахує загальну тривалість всіх треків в альбомі.
  Базовий кейс - поверне кількість секунд.
  * Дод. ускладнення повернути у вигляді рядка години:хвилини:секунди, прик. 0:41:39"""

import json
from time import strftime, gmtime

with open('acdc.json') as f:
    music = json.load(f)
    time = sum(int(i["duration"]) for i in music["album"]["tracks"]["track"])
    print("Total time in sec: ", time)
    print("Total time in Hr:", strftime('%H:%M:%S', gmtime(time)))