import time
from datetime import datetime, timedelta

pomodoro_seconds = input('How long? ')

try:
    pomodoro_seconds = int(pomodoro_seconds)
except:
    print('There isn\'t number', pomodoro_seconds)
    exit()

start_time = datetime.today()
end_time = start_time + timedelta(seconds=pomodoro_seconds)
current_time = start_time

diff_seconds = (end_time - current_time).seconds

while True:
    if (diff_seconds <= 0):
        print('Finish!')
        exit()
    else:
        current_time = datetime.today()
        diff_seconds = (end_time - current_time).seconds
        print(diff_seconds, 'seconds left')

    time.sleep(1)
