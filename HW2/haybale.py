#### Purpose
# To prompt the user to input day, time, temperature, and whether it’s raining.
# To use default values if the user enters invalid information.
# To calculate the actual price after all that input is taken into consideration, 
# and print it out to the user in a currency format (e.g., “your final price is $10.00”).
#### Signature
# haybalemase_bill :: (Integer,String,Integer,String) => Float
#### Template
# def rsp_game(given):
#    return returns...
#### Examples
#  R vs S => Rock smashes scissors! You win!
#  s vs S => OMG it's a tie!!!
#  paper vs S => Scissors cut paper! You lose!
#  ninja => That is not a rock, scissors, or paper, sorry, no game
BASE_PRICE = 9
MAX_TEMP = 75
ABOVE_TEMP_RATE = 0.1
MIN_TEMP = 40
BELOW_TEMP_RATE = -0.05
WEEKEND_EXTRA = 1
WEEKDAY_START_TIME=0
WEKDAY_END_TIME=23
WEEKADY_LATE_TIME = 5
WEEKDAY_LATE_EXTRA = 2
RAIN_EXTRA = 0.5
WEEKDAY_LIST=["mon","tue","wed","thu","fri"]
WEEKEDN_LIST=["sat","sun"]

def haybalemase_bill(temp,day,time,if_rain):
    
    temp= int(input("What is the temprature now?\n"))
    day = input("What day of the week is it?\n").lower()
    time= int(input("What hour of the day is it?"))
    if_rain=input("Is it raining? Enter Y/N:\n").upper()
    temp_extra = 0
    day_extra=0
    if temp < 0 & temp > 99:
        temp=MAX_TEMP
        temp_extra = 0
    elif temp>=MAX_TEMP:
        temp_extra = (temp - MAX_TEMP)*ABOVE_TEMP_RATE
    elif temp<=MIN_TEMP:
        temp_extra = (MIN_TEMP - temp*BELOW_TEMP_RATE
    
    for day in WEEKDAY_LIST+WEEKEND_LIST：
        
        if day in WEEKDAY_LIST and time>=WEEKDAY_START_TIME && time<=WEKDAY_END_TIME:
            if time>=WEEKADY_LATE_TIME:
                return day_extra = WEEKDAY_LATE_EXTRA
            else:
                return day_extra = 0
        elif day in WEEKEND_LIST:
            return day_extra = WEEKEND_EXTRA
    elif:
        day="mon"

    if if_rain="Y":
        return weather_extra=RAIN_EXTRA
    else:
        return weather_extra=0
return final_price=BASE_PRICE+temp_extra+day_extra+weather_extra

print(haybalemase_bill())
        