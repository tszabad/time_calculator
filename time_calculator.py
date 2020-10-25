def to_24(time):
        minutes = time.split(":")[1].split(" ")[0]
        day_time = time.split(":")[1].split(" ")[1]
        if day_time == "AM":
            hours = int(time.split(":")[0]) 
        else:
            hours = int(time.split(":")[0]) + 12
        return [hours, minutes]

def add_time(start, duration, day=""):
    start_hour = to_24(start)[0]
    start_min = to_24(start)[1]
    print(start_hour)
  
    dur_hours = int(duration.split(":")[0])
    dur_minutes = int(duration.split(":")[1])

    days = ["monday", "tuesday", "wednesday", 
            "thursday", "friday", "saturday", "sunday"]

    





    return new_time

add_time("3:00 PM", "3:10")