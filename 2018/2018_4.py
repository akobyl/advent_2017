from datetime import datetime
from datetime import timedelta

GUARD_START = 0
WAKE_UP = 1
FALL_ASLEEP = 2
UNKNOWN = 3


def parse_log_line(in_str: str):
    date_string = in_str[:in_str.find(']') + 1]
    date = datetime.strptime(date_string, '[%Y-%m-%d %H:%M]')

    if in_str[19] == 'G':
        log_type = GUARD_START
    elif in_str[19] == 'w':
        log_type = WAKE_UP
    elif in_str[19] == 'f':
        log_type = FALL_ASLEEP
    else:
        log_type = UNKNOWN

    if log_type == GUARD_START:
        guard_id = int(in_str[in_str.find('#') + 1:in_str.find('b')].rstrip())
    else:
        guard_id = None
    return log_type, date, guard_id


# scan for guard shift beginnings
guard_log = []
with open('input/day4_in.txt') as file:
    for line in file:
        log_type, timestamp, guard_id = parse_log_line(line)
        assert log_type != UNKNOWN
        guard_log.append((timestamp, log_type, guard_id))

# sort by date
guard_log.sort(key=lambda log_entry: log_entry[0])

# create a minute-by-minute array for each day
# each day starts with a guard begin shift then sleep/wake
sleepy_log = []
for log_entry in guard_log:
    log_datetime = log_entry[0]
    log_type = log_entry[1]
    guard_id = log_entry[2]

    if log_type == GUARD_START:
        sleepy_date = datetime.date(log_datetime)
        if log_datetime.hour >= 1:
            sleepy_date += timedelta(days=1)
        sleepy_schedule = [False] * 60
        sleepy_log.append([sleepy_date, guard_id, sleepy_schedule])

    if log_type == FALL_ASLEEP:
        sleep_start = log_datetime.minute
        assert log_datetime.hour == 0
        sleepy_log[-1][2][sleep_start:] = [True] * (60 - sleep_start)

    if log_type == WAKE_UP:
        wake_start = log_datetime.minute
        assert log_datetime.hour == 0
        sleepy_log[-1][2][wake_start:] = [False] * (60 - wake_start)

    assert len(sleepy_log[-1][2]) == 60

# make a list of how much each guard is sleeping
guard_sleep_total = {}
minute_sleep_count = {}
sleepiest_guard_total = 0
sleepiest_guard = None

for sleep_log in sleepy_log:
    guard_id = sleep_log[1]
    sleepy_minutes = sleep_log[2].count(True)

    if guard_id in guard_sleep_total:
        guard_sleep_total[guard_id] += sleepy_minutes
    else:
        guard_sleep_total[guard_id] = sleepy_minutes
        minute_sleep_count[guard_id] = [0] * 60

    for minute, asleep in enumerate(sleep_log[2]):
        if asleep:
            minute_sleep_count[guard_id][minute] += 1

    if guard_sleep_total[guard_id] > sleepiest_guard_total:
        sleepiest_guard_total = guard_sleep_total[guard_id]
        sleepiest_guard = guard_id

# Find the minute in which the sleepiest guard sleeps the most
sleep_minutes = [0] * 60
sleepy_guard_log = [x for x in sleepy_log if x[1] == sleepiest_guard]

for log_entry in sleepy_guard_log:
    for minute, asleep in enumerate(log_entry[2]):
        if asleep:
            sleep_minutes[minute] += 1

result = sleepiest_guard * sleep_minutes.index(max(sleep_minutes))
print(f'Part 1: {result}')

sleepiest_minute_count = 0
sleepiest_minute_guard = None
sleepiest_minute_minute = 0

for guard_id, guard_minute_entry in minute_sleep_count.items():
    guard_sleepiest_minute_count = max(guard_minute_entry)
    if guard_sleepiest_minute_count > sleepiest_minute_count:
        guard_sleepiest_minute = guard_minute_entry.index(max(guard_minute_entry))
        sleepiest_minute_guard = guard_id
        sleepiest_minute_count = guard_sleepiest_minute_count

result = sleepiest_minute_guard * guard_sleepiest_minute
print(f'Part 2: {result}')
print('done')
