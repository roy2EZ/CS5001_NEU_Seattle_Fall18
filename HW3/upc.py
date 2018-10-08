#### Purpose
# This function prompt user enter a UPC code and calculate if the code is valid with UPC rules
#### Signature
# upc():: String => String
#### Template
# def upc(given...):
#   return returns...
#### Examples
# Test case #1: Meadowoods Air Fresshener
#4973258253 -- valid
#4973259253 -- invalid -- mistyped 8 instead of 9
#4972358253 -- invalid -- transposed two digits
# Test case #2: FredMeyer Purified Drinking Water 
#924187053904 -- valid
#924187054904 -- invalid -- mistyped 3 instead of 4
#924178053904 -- invalid -- transposed two digits
# Test case #3: Head First Python 2nd Edition
#781421916537 -- valid
#781521916537 -- invalid -- mistyped 4 instead of 5
#781421196537 -- invalid -- transposed two digits

def upc():
    #Take user input string
    str_input=input("Enter the UPC code:\n")
    #reverse the user input string for read the UPC code from right end to left
    str_reverse=str_input[::-1]
    #set a initial result as 0
    result = 0
    #get the length for using as the max range in condition 
    length = len(str_reverse)
    #initial i as 0
    i = 0
    while i < length:
        #Digits in even positions: add it to result
        if i % 2 == 0:
            result += int(str_reverse[i])
            i+=1
        #Digits in odd positions: multiply it by 3 and add it to result    
        else:
            result += 3*int(str_reverse[i])
            i+=1
    
    #if this result is a multiple of 10, then it is valid UPC, output valid notification
    if result % 10 == 0:
        return "Valid UPC!!"
    #if it is not, output not valid notification
    else:
        return "Not valid UPC code."
    
#test the function    
print(upc())