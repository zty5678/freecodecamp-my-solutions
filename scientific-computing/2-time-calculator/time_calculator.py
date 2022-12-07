'''
11:30  -> 11:30 AM
18:10 -> 6:10 PM
'''


def format_hour(hour_or_minute: int) -> str:
    # if hour_or_minute<10:
    #     return "0"+str(hour_or_minute);
    # else :
    #     return str(hour_or_minute);
    return str(hour_or_minute);


def format_minute(hour_or_minute: int) -> str:
    if hour_or_minute < 10:
        return "0" + str(hour_or_minute);
    else:
        return str(hour_or_minute);


def time_24_hour_to_12_hour(time_str: str) -> str:
    time_array = time_str.split(":")
    hour = int(time_array[0])
    minute = int(time_array[1])
    if hour == 12:
        return format_hour(hour) + ":" + format_minute(minute) + " " + "PM"
    elif hour == 0:
        return format_hour(12) + ":" + format_minute(minute) + " " + "AM"
    elif 0 < hour < 12:
        return format_hour(hour) + ":" + format_minute(minute) + " " + "AM"
    else:
        return format_hour(hour - 12) + ":" + format_minute(minute) + " " + "PM"

    return ""


'''
11:30 AM ->  11:30
6:10 PM -> 18:10
'''

def time_12_hour_to_24_hour(time_str: str):
    array1 = time_str.split(" ")
    time_str1 = array1[0]
    am_str = array1[1]
    time_array = time_str1.split(":")
    hour = time_array[0]
    minute = time_array[1]
    if am_str == "AM":
        if hour == "12":
            return "00:" + minute
        else:
            return hour + ":" + minute
    elif am_str == "PM":
        if hour == "12":
            return hour + ":" + minute
        else:
            return str(int(hour) + 12) + ":" + minute

    return "";


WEEKDAY_ARRAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def find_day(day_str: str) -> int:
    day_str = day_str.lower();
    for idx, x in enumerate(WEEKDAY_ARRAY):
        if day_str == x.lower():
            return idx;
    return -1;


def add_time(start: str, duration: str, day: str = ""):
    time_24 = time_12_hour_to_24_hour(start);
    time_array = time_24.split(":")
    hour = int(time_array[0])
    minute = int(time_array[1])

    duration_array = duration.split(":")
    hour_dur = int(duration_array[0])
    minute_dur = int(duration_array[1])

    hour += hour_dur
    minute += minute_dur
    if minute >= 60:
        hour += int(minute / 60);
        minute = minute % 60;

    day_count = 0;
    if hour >= 24:
        day_count = int(hour / 24);
        hour = hour % 24;

    if day == "":
        time_str = time_24_hour_to_12_hour(format_hour(hour) + ":" + format_minute(minute));
        if day_count == 0:
            return time_str
        else:
            day_str = "(" + str(day_count) + " days later)" if day_count > 1 else "(next day)";
            return time_str + " " + day_str
    else:
        index = find_day(day)
        time_str = time_24_hour_to_12_hour(format_hour(hour) + ":" + format_minute(minute));
        if day_count == 0:
            return time_str + ", " + day
        else:
            day_str = "(" + str(day_count) + " days later)" if day_count > 1 else "(next day)";
            return time_str + ", " + WEEKDAY_ARRAY[(day_count + index) % 7] + " " + day_str;
