# 100daysofcode

## День 9-10

Новые структуры данных

deque - https://docs.python.org/3/library/collections.html#collections.deque
```python
from collections import deque
queue = deque([1, 2, 3])
queue.append(4) # None / deque([1, 2, 3, 4])
queue.appendleft(0) # None / deque([0, 1, 2, 3, 4])
queue.rotate(1) # None / deque([4, 0, 1, 2, 3])
queue.popleft() # 4 / deque([0, 1, 2, 3])
```

list comprehensions — https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
```python
[(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

sets — https://docs.python.org/3/tutorial/datastructures.html#sets
```python
nums = {1, 2, 3, 2, 4, 5, 2, 1, 4} # {1, 2, 3, 4, 5}
set = {} # создаст словарь, надо использовать set() для пустого значения
type(set) # <class 'dict'>

a = set('abracadabra') # {'a', 'r', 'b', 'c', 'd'}
b = set('alacazam') # {'a', 'l', 'c', 'z', 'm'}
a - b # letters in a but not in b      | {'r', 'd', 'b'}
a | b # letters in a or b or both      | {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b # letters in both a and b        | {'a', 'c'}
a ^ b # letters in a or b but not both | {'r', 'd', 'b', 'm', 'z', 'l'}

{x for x in 'abracadabra' if x not in 'abc'} # {'r', 'd'}
```

namedtuple — https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
p[0] + p[1] # 33
p._asdict() # {'x': 11, 'y': 22}
p._fields # ('x', 'y')

t = [1, 2]
Point._make(t) # Point(x=1, y=2)
```

defaultdict — https://docs.python.org/3/library/collections.html#defaultdict-objects
```python
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v) # с объектом такое не прокатит, будет ошибка KeyError

d # defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
```

Counter — https://docs.python.org/3/library/collections.html#counter-objects
```python
from collections import Counter
cntr = Counter('sadqwdcxcvdfecdxcd')
cntr.most_common(5) # [('d', 5), ('c', 4), ('x', 2), ('s', 1), ('a', 1)]
```

## День 7-8

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
```
```python
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

lambda a: a + 1
# equal
def f(a):
    return a + 1

f.__doc__ # https://docs.python.org/3/tutorial/controlflow.html#documentation-strings
f.__annotations__ # https://docs.python.org/3/tutorial/controlflow.html#function-annotations
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
del a[:] # l == []

[1, 2, 3].reverse() # return None / [3, 2, 1]
[3, 2, 1].sort() # return None / [1, 2, 3]
[1, 2, 3].pop() # return 3 / [1, 2]
[1, 2, 3].append(4) # return None / [1, 2, 3, 4]
[1, 2, 3].insert(0, 10) # return None / [10, 1, 2, 3]
[1, 2, 3].count(2) # 1
[1, 2, 3].index(3) # 2

for num in [1, 2, 3]:
    print(num, end=',')
# 1,2,3,

'-'.join(['a', 'b', 'c']) # '1-2-3'
```
```python
# tuple
t = tuple([1, 2, 3])
# убогий вариант 
t = 1, 2, 3 # (1, 2, 3)
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