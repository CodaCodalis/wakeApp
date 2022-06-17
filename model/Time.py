class Time:

    def __init__(self, arrival_time, duration, prep_time, delay):
        
        self.__arrival_time = self.__convert_time_to_int(arrival_time)
        self.__duration = self.__convert_time_to_int(duration)
        self.__prep_time = self.__convert_time_to_int(prep_time)
        self.__delay = self.__convert_time_to_int(delay)
        if self.__arrival_time < 0 or self.__duration < 0 or self.__prep_time < 0 or self.__delay < 0:
            raise ValueError


    def __convert_time_to_int(self, time):
        hours = float(time.split(':')[0])
        minutes_as_percent = float(time.split(':')[1]) / 60
        if minutes_as_percent < 0 or minutes_as_percent >= 1 or hours < 0 or hours > 23:
            raise ValueError
        return hours + minutes_as_percent

    def get_arrival_time(self):
        return self.__arrival_time

    def get_duration(self):
        return self.__duration

    def get_prep_time(self):
        return self.__prep_time

    def get_delay(self):
        return self.__delay
