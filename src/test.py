"""
start_hour = 10
start_minute = 10

end_hour = 13
end_minute = 50

schedule = []

if start_hour != end_hour:
    schedule.append(f"{start_hour}:{start_minute} - {start_hour}:59")  # first time range
    schedule.append(f"{start_hour}:0 - {end_hour - 1}:59")  # middle time range
    schedule.append(f"{end_hour}:00 - {end_hour}:{end_minute}")  # last time range
else:
    schedule.append(f"{start_hour}:{start_minute} - {end_hour}:{end_minute}")  # only one time range


print(schedule)
"""
