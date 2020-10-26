def to_24(time):
        minutes = time.split(":")[1].split(" ")[0]
        day_time = time.split(":")[1].split(" ")[1]
        if day_time == "AM":
            hours = int(time.split(":")[0]) 
        else:
            hours = int(time.split(":")[0]) + 12
        return [hours, minutes]

def to_am_pm(hours, minutes):
    day_time=""
    if hours > 12:
        hours -=12
        day_time = "PM"
    else:
        daytime = "AM"
    return [hours, minutes, day_time]


def add_time(start, duration, day=""):
    start_hour = int(to_24(start)[0])
    start_min = int(to_24(start)[1])
    print(start_hour)
  
    dur_hours = int(duration.split(":")[0])
    dur_minutes = int(duration.split(":")[1])

    days = ["monday", "tuesday", "wednesday", 
            "thursday", "friday", "saturday", "sunday"]

    dur_day = day
    
    future_hour = start_hour + dur_hours
    future_minute = start_min + dur_minutes
    if future_minute > 60:
        future_hour +=1
        future_minute -=60
    
 
    newtime = to_am_pm(future_hour, future_minute)
    new_time = str(newtime[0]) + ':' + str(newtime[1]) + " " + newtime[2]

    print(new_time)
    return new_time

add_time("3:00 PM", "3:10")