#### Purpose
# To prompt user to input a positive integer which is power of 2
# and calculate the logarithm base 2 of that integer
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

def log_calculator(power):
    power=int(power)
    result=power
    i = 0
    while result!=1:
        result =int(result/2)
        i += 1
    return str(i)

def main():
    power=input("Enter a positive power of 2:\n")
    print("log2("+power+") = " + log_calculator(power))

main()