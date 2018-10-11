#### Purpose
# To prompt user to input a binary number and transfer it into decimal to output
#### Signature
#  binary_to_decimal :: (str)=>Integer
#### Template
# def binary_to_decimal(given...):
#    return returns...
#### Examples
# 110 => 6
# 110101 => 53
# 11111 => 31
# 001 => 1

def binary_to_decimal(binary):
    decimal=0
    i=0
    while i < len(binary):
        decimal += 2 ** (i) * int(binary[-i-1])
        i += 1
    return str(decimal)

def main():
    binary=input("Please enter a binary number:\n")
    print("The decimal of binary "+binary+" = "+binary_to_decimal(binary))

main()

