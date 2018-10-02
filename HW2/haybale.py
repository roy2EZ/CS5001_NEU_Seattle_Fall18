#### Purpose
# To prompt the user to input day, time, temperature, and whether it’s raining.
# To use default values if the user enters invalid information.
# To calculate the actual price after all that input is taken into consideration, 
# and print it out to the user in a currency format (e.g., “your final price is $10.00”).
#### Signature
# haybalemase_bill :: (Integer,String,Integer,String) => String
#### Template
# def haybalemase_bill(given):
#    return returns...
#### Examples
#  60,mon,8,n => Your final price for the maze is: $9
#  95,sat,19,y => Your final price for the maze is: $12.5
#  30,Fri,10,N => Your final price for the maze is: $8.5
#  -6,sunday funday,25,yes it is raining!=> Your final price for the maze is: $9

BASE_PRICE = 9
MAX_TEMP = 75
ABOVE_TEMP_RATE = 0.1
MIN_TEMP = 40
BELOW_TEMP_RATE = -0.05
WEEKEND_EXTRA = 1
WEEKDAY_START_TIME=0
WEKDAY_END_TIME=23
WEEKADY_LATE_TIME = 17
WEEKDAY_LATE_EXTRA = 2
RAIN_EXTRA = 0.5
WEEKDAY_LIST = ["mon","tue","wed","thu","fri"]
WEEKEND_LIST = ["sat","sun"]
DAY_LIST=WEEKDAY_LIST+WEEKEND_LIST

def haybalemase_bill(temp,day,time,if_rain):
    #set up inital variable in the final results 
    temp_extra = 0
    day_extra = 0
    weather_extra=0
    
    #when temperature input is invalid, force default it as the max temperature 75F
    if temp < 0 & temp > 99:
        temp=MAX_TEMP
        #when temperature is over max, every degree will charge an rate as ABOVE_TEMP_RATE
    if temp>=MAX_TEMP and temp<=99:
        temp_extra = (temp - MAX_TEMP)*ABOVE_TEMP_RATE
        #when temperature is below min, every degree will apply a discount rate as BELOW_TEMP_RATE    
    elif temp<=MIN_TEMP and temp>=0:
        temp_extra = (MIN_TEMP - temp)*BELOW_TEMP_RATE
    
    #when the day input is invalid, force default the input as "mon"
    if day not in DAY_LIST:
        day="mon"
        #when the day input is weekdays, continue to check the time
    if day in WEEKDAY_LIST:
        #when time input is invalid, force default it into 12:00
        if time <0 or time>23:
            time=12
            #when the time is over 17:00, charge an extra late fee as WEEKDAY_LATE_EXTRA
        if time >= WEEKADY_LATE_TIME and time<=23:
            day_extra = WEEKDAY_LATE_EXTRA
                #when the time is not over 17:00, no extra charge    
        else:
            day_extra = 0
        #when day is weekend, charge a weekend extra            
    elif day in WEEKEND_LIST:
        day_extra = WEEKEND_EXTRA
    
    #if it is raining, charge a weather extra fee
    if if_rain=="Y":
        weather_extra=RAIN_EXTRA
    #if it is not raining or user input is invalid, default the input as not raining
    # and don't charge weather extra fee    
    else:
        weather_extra=0
    #return the final price with base price adding all extra fees, round the result with 2 digits of
    return "Your final price for the maze is: $"+ str("%.2f" % (BASE_PRICE+temp_extra+day_extra+weather_extra))

temp= int(input("What is the temprature now?\n"))
day = input("What day of the week is it?\n").lower()
time= int(input("What hour of the day is it?\n"))
if_rain=input("Is it raining? Enter Y/N:\n").upper()
print(haybalemase_bill(temp,day,time,if_rain))
        