# 100daysofcode

## День 7

Дополнительные тонкости

```python
a, b = 1, 3
# a = 1
# b = 3

17 / 3 # 5.66... (всегда float)
17 // 3 # 5 (целая часть)

# string — immutable
'a' 'b' # 'ab', неявная конкатенация
str = (
    'hello'
    'world'
) # helloworld

3 * 'm' + 3 * '.' # 'mmm...'
word = 'Python'
word[-1] # n
word[2:] # thon
word[-2:] # on

range(5) # 0, 1, 2, 3, 4
range(0, 10, 4) # 0, 4, 8

def f(a, b=1, c=2):
    ...
f(a=1, c=10) # equal f(1, 1, 10)

def f(*arguments, **keywords):
    for arg in arguments:
        print(arg, end=',')
    for kw in keywords:
        print(kw, ":", keywords[kw])

f(1, 2, 3, a=1, b=2)
f(*[1, 2, 3], **{'a': 1, 'b': 2})
# 1,2,3
# a: 1
# b: 2

# https://docs.python.org/3/tutorial/controlflow.html#special-parameters
def f(pos1, /, pos_or_kwd, *, kwd1):
      ----     ----------     ----
        |          |            |
        |          |        Keyword only
        |  Positional or keyword 
   Positional only
```


## День 4

Структуры данных. https://docs.python.org/3/tutorial/datastructures.html

list — mutable

tuple — immutable

dict

```python
# list
list() == [] # <class 'list'>
list('hello') # ['h', 'e', 'l', 'l', 'o']
l = [1, 2, 3]
del l[0] # l == [1, 2]

[1, 2, 3].reverse() # return None / [3, 2, 1]
[3, 2, 1].sort() # return None / [1, 2, 3]
[1, 2, 3].pop() # return 3 / [1, 2]
[1, 2, 3].append(4) # return None / [1, 2, 3, 4]
[1, 2, 3].insert(0, 10) # return None / [10, 1, 2, 3]

for num in [1, 2, 3]:
    print(num, end=',')
# 1,2,3,

'-'.join(['a', 'b', 'c']) # '1-2-3'
```
```python
# tuple
t = tuple([1, 2, 3])
t[0] = 20 # ERROR
```
```python
# dict
fruits = {'apple': 10, 'orange': 15} or dict([('apple', 10), ('orange', 15)])

fruits['mango'] = 1 # {'apple': 10, 'orange': 15, 'mango': 1}
del fruits['mango'] # {'apple': 10, 'orange': 15}

fruits.keys() # dict_keys(['apple', 'orange'])
fruits.values() # dict_values([10, 15])
fruits.items() # dict_items([('apple', 10), ('orange', 15)])

for key, value in fruits.items():
    print(key, value)
# apple 10
# orange 15
```

## День 1-3

Изучение работы с датой и временем. 

Написание скрипта по замене символов в файле.

Дока по datetime: https://docs.python.org/3/library/datetime.html

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

date = datetime.strptime('10 Aug 2019', '%d %b, %Y') # return <class 'datetime.datetime'>
date.strftime('%m/%d/%Y') # return <class 'str'>
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

time.sleep(1) # sleep program 1 sec
```