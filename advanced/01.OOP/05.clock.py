from datetime import datetime,timedelta



class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        time_string = f"{self.hours}:{self.minutes}:{self.seconds}"
        clock = datetime.strptime(time_string,"%H:%M:%S").time()
        return f"{clock}"

    def next_second(self):
        time_string = f"{self.hours}:{self.minutes}:{self.seconds}"
        clock = datetime.strptime(time_string,"%H:%M:%S")
        clock_new = (clock + timedelta(seconds=1)).time()
        return f"{clock_new}"
