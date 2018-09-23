#### Purpose
# This function takes a total amount of the house, 
# the annual salary and 
# the percentage of salary you can save per month
# and give the result of how long it takes to payoff the downpayment 
#
#### Signature
# houseDownPaymantTimeCaculator :: (float,float,float) =>  float and int within str
#
#### Template
# def houseDownPaymantTimeCaculator(given...):
#    return returns...
#
#### Examples
# houseDownPaymantTimeCaculator(75000,48000,0.3) => 
# If you save $1200.0 per month, it will take 1 year and 4 month to save enough for the down payment!

def houseDownPaymantTimeCaculator(houseprice,annualsalary,savepermonth):
    downpayment = houseprice*0.25
    amountsavepermonth = annualsalary/12*savepermonth
    totalmonth = downpayment/amountsavepermonth
    y = totalmonth//12
    m = totalmonth%12
    return "If you save $"+ str(round(amountsavepermonth,2)) + " per month, it will take "\
    + str(round(y))+" year and " + str(round(m))+ " month to save enough for the down payment!" 
    
#test cases:
message = houseDownPaymantTimeCaculator(75000,48000,0.3)
print(message)

message = houseDownPaymantTimeCaculator(100000,50000,0.25)
print(message)

message = houseDownPaymantTimeCaculator(175000,95400,0.21)
print(message)
