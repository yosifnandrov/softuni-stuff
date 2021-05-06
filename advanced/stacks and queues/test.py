from datetime import datetime, timedelta, time

start_time = datetime.strptime(input(),"%H:%M:%S")

current_time = 30

time_to_str = (start_time + timedelta(hours=1,minutes=20,seconds=55)).strftime("%H:%M:%S")
print(time_to_str)
print(start_time)