from datetime import datetime

SHUTDOWN_EVENT = 'Shutdown initiated'

with open('tmp/log.txt') as f:
    loglines = f.readlines()

def convert_to_datetime(line):
    date = line.split(' ')[1]
    result = datetime.strptime(date, '%Y-%m-%dT%X')
    return result

def time_between_shutdowns(loglines):
    first_index = -1
    last_index = -1
    for index, line in enumerate(loglines):
        if (SHUTDOWN_EVENT in line):
            if (first_index == -1):
                first_index = index

            last_index = index

    first_time = convert_to_datetime(loglines[first_index])
    last_time = convert_to_datetime(loglines[last_index])

    return last_time - first_time