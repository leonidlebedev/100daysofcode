# 100daysofcode

## День 1-3

Изучение работы с датой и временем. Написание скрипта по замене символов в файле.
Дока по datetime: https://docs.python.org/3/library/datetime.html
Полезные куски кода:
```python
# Работа с датой
from datetime import datetime
from datetime import date
from datetime import timedelta
import time

datetime.today()
# datetime.datetime(2019, 11, 29, 14, 38, 52, 133483)
# <class 'datetime.datetime'>

date.today()
# datetime.datetime(2019, 11, 29)
# <class 'datetime.date'>

todaydate.year # 2019
todaydate.month # 11
todaydate.day # 29

t = timedelta(days=4, hours=10) 
t.days # 4
t.hours # ERROR
t.seconds # 36000 (not include days)

date = datetime.strptime('10 Aug 2019', '%d %b, %Y') # return <datetime.datetime>
date.strftime('%m/%d/%Y') # return <string>
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

time.sleep(1) # sleep program 1 sec
```