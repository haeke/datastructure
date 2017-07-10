"""
    calculate the angle between the two hands on a clock

"""

def clockangle(hours, mins):
    #get the minute hand value
    minutehand = 6 * mins
    hourhand = 0.5 * ( 60 * hours + mins)
    #angle is the absolute value of hourhand - minutehand
    angle = abs(hourhand - minutehand)
    #subtract the angle from 360 if the angle is larger than 180 so that it is represented on the opposite side
    if angle > 180:
        return 360 - angle
    else:
        return angle

print "------------------"
print clockangle(2, 30)
