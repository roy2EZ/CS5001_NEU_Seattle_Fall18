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
def racepace(distanceInKm,hour,min):
    distanceInMile = distanceInKm/1.61
    totalhour=hour+min/60
    totalmin=hour*60+min
    pacemin=math.floor(totalmin/distanceInMile)
    pacesec=math.floor((totalmin/distanceInMile-pacemin)*60)
    speed=round(distanceInMile/totalhour,2)
    return "You ran " + str(round(distanceInMile,2))+" miles.\n"\
    +"Your pace is "+str(pacemin)+":%02d"%(pacesec) +" per mile.\n"\
    +"Your speed is "+ str(speed)+" mph."

d = input("How many kilometers did you run?\n")
h = input("How many hours did it take you?\n")
m = input("How many minutes?\n")
print(racepace(float(d),float(h),float(m)))
