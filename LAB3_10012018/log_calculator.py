#### Purpose
# To prompt user to input a positive integer which is power of 2
# and calculate calculate the logarithm base 2 of that integer
#### Signature
# log_calculator :: (Integer)=>Integer
#### Template
# def log_calculator(given...):
#    return returns...
#### Examples
# 1 => lg(1)=0
# 2 => lg(2)=1
# 4 => lg(4)=2
# 8 => lg(8)=3

def log_calculator():
    power=int(input("Enter a positive power of 2:\n"))
    result=power
    flag=0
    while result!=0:
        result =int(result/2)
        flag += 1
    return "lg("+str(power)+") = "+str(flag-1)

print(log_calculator())