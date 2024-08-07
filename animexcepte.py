import datetime

unix_time = 1627062591  # Replace this with your UNIX time
local_time = datetime.datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
print(local_time)
