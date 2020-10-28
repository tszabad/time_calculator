def to_24(time):
        minutes = time.split(":")[1].split(" ")[0]
        day_time = time.split(":")[1].split(" ")[1]
        if day_time == "AM":
            hours = int(time.split(":")[0])%12
        else:
            hours = int(time.split(":")[0])%12 + 12
        return [hours, minutes, day_time]

def to_am_pm(hours, minutes):
    day_time=""
    hours %=24
    if hours > 12:
        hours %=12
        day_time = "PM"
    else:
        day_time = "AM"
    return [hours, minutes, day_time]


def add_time(start, duration, day=""):
    start_hour = int(to_24(start)[0])
    start_min = int(to_24(start)[1])
    start_daytime = start[2]
  
    dur_hours = int(duration.split(":")[0])
    dur_minutes = int(duration.split(":")[1])

    days = ["monday", "tuesday", "wednesday", 
            "thursday", "friday", "saturday", "sunday"]
    

    dur_days = (dur_hours *60 + dur_minutes)/60/24
    print(dur_days)
    suffix = ""
    
    future_minute = start_min + dur_minutes
    future_hour = start_hour + dur_hours 
    print(future_hour)
    
    
    if future_hour > 24 and dur_days <= 1:
        suffix= " (next day)"
    if dur_days > 1:
        dayslater = int((future_hour + future_minute/60)//24)
        suffix = " (" + str(dayslater) + " days later)"
    postition = ""
    futureday = ""
    if day != "":
        postition = days.index(day.lower())
        futureday = " " + days[postition+dayslater].capitalize()
    
    if future_minute > 60:
        future_hour +=1
        future_minute -=60
    
    newtime = to_am_pm(future_hour, future_minute)
    
    if newtime[1]<10:
        newtime[1] = "0" + str(newtime[1])
    new_time = str(newtime[0]) + ':' + str(newtime[1]) + " " + newtime[2] + futureday + suffix

    print(new_time)
    return new_time

add_time("2:59 AM", "24:00", "saturDay")