class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        # return f"{self.hours}:{self.minutes}:{self.seconds}"
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 00
            self.minutes += 1
        if self.minutes > Time.max_minutes:
            self.minutes = 00
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 00
        return self.get_time()

