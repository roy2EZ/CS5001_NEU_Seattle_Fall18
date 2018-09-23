#### Purpose
# This function takes a total amount of the bill, the tip percentage and the amount of 
# people who wish to split the bill, and give the result of each person's final bill amount 
# 
#
#### Signature
# billCauculatorWithTip :: (Float, Float,Integer) => Float
#
#### Template
# def billCauculatorWithTip(given...):
#    return returns...
#
#### Examples
# billCauculatorWithTip(60, 0.2,3) => 24

def billCauculatorWithTip(bill,tip,personNo):
    return bill*(1+tip)/personNo

#Test case:
amt_owed = billCauculatorWithTip(60, 0.2,3)
print(round(amt_owed,2))

amt_owed = billCauculatorWithTip(56, 0.18,2)
print(round(amt_owed,2))

amt_owed = billCauculatorWithTip(274, 0.2,5)
print(round(amt_owed,2))