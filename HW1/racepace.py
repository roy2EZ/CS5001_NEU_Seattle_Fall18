#### Purpose
# calculate runner's distance in miles, running pace and speed 
# by user input the distance in km and total time of hours and minutes
#### Signature
# racepace :: (Number,Number,Number)=>Number,Number,Number
#### Template
# def racepace(given...):
#    return returns...
#### Examples
#  racepace(10,1,11)=> 6.21 miles, 11:25, 5.25 mph
#  racepace(20,2,35)=>12.42 miles, 12:28. 4.81 mph
#  racepace(5,0,31) => 3.11 miles,  9:58, 6.01 mph

import math
def racepace(distance_in_km,hour,min):
    distance_in_mile = distance_in_km/1.61
    #convert kilometers to miles
    total_hour=hour+min/60
    #calculate total time in hours
    total_min=hour*60+min
    #calculate total time in minutes
    pace_min=math.floor(total_min/distance_in_mile)
    #calculate the minute part in final result of pace of fomation mm:ss
    pace_sec=math.floor((total_min/distance_in_mile-pace_min)*60)
    #calculate the second part in final result of pace of fomation mm:ss
    speed=round(distance_in_mile/total_hour,2)
    #calculate the speed
    return "You ran " + str(round(distance_in_mile,2))+" miles.\n"\
    +"Your pace is "+str(pace_min)+":%02d"%(pace_sec) +" per mile.\n"\
    +"Your speed is "+ str(speed)+" mph."
    #return final result

d = input("How many kilometers did you run?\n")
#let user input distance in km
h = input("How many hours did it take you?\n")
#let user input the hour part of running time
m = input("How many minutes?\n")
#let user input the minute part of running time
print(racepace(float(d),float(h),float(m)))
#give final result