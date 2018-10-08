#### Purpose
# This function takes a string as input and returns the uppercase version of the string
#### Signature
# to_upper :: (String) => String
#### Template
# def to_upper(given...):
# return returns...
#### Examples
# to_upper("test string 9000") => "TEST STRING 9000"
# to_upper("ThIs Is A sTrInG") => "THIS IS A STRING"
def to_upper(string):  
    #create a list of input string
    s1=list(string)
    #copy a list s2 from s1 and stand-by as an output
    s2=list(s1)
    #initial i as 0 
    i=0
    while i<len(s1):
        #in Unicode, the code point of lowercase a to z is from 97 to 122
        #if the input is in that range then transfer it to uppercase letter range by minus 32 
        if ord(s1[i]) >= 97 and ord(s1[i]) <= 122:
            s2[i]=str(chr(ord(s1[i]) - 32))   
        i += 1
    #join each element in the list s2 into a str as output    
    return "".join(s2)

#### Purpose
# This function takes a string as input and returns the lowercase version of the string
#### Signature
# to_lower :: String => String
#### Template
# def to_lower(given...):
# return returns...
#### Examples
# to_lower("SHOUTY STRING") => "shouty string"
# to_lower("ThIs Is A sTrInG") => "this is a string"
def to_lower(string): 
    #create a list s1 of input string  
    s1=list(string)
    #copy a list s2 from s1 and stand-by as an output
    s2=list(s1)
    #initial i as 0
    i=0
    while i<len(s1):
        #in Unicode, the code point of uppercase A to Z is from 65 to 90
        #if the input is in that range then transfer it to lowercase letter range by adding 32 
        if ord(s1[i]) >= 65 and ord(s1[i]) <= 90:
            s2[i]=str(chr(ord(s1[i]) + 32))  
        i += 1
    return "".join(s2)

#### Purpose
# This function takes a string as input and returns the reverse of
#that string, maintaining the case of the original string.
#### Signature
# in_reverse :: String => String
#### Template
# def in_reverse(given…):
# return returns...
#### Examples
# in_reverse("Tuesday 3:00 PM") => "MP 00:3 yadseuT"
# in_reverse("abcde") => "edcba"
def in_reverse(string): 
    #create a list s1 of input string  
    s1=list(string)
    #copy a list s2 from s1 and stand-by as an output
    s2=list(s1)
    #initial i as 0
    i=0
    while i<len(s1):
        #make the element s2[i] as same as the element on s1[-1-i] 
        s2[i]=s1[-1-i]    
        i += 1
    return  "".join(s2)

#### Purpose
# This function takes a string as input and returns palindrome using that user input, 
# with all uppercase or lowercase option for user to choose
#### Signature
# string_process :: (String,String) => String
#### Template
# def string_process(given…):
# return returns...
#### Examples
# Testcase1:
# Make Me A Palindrome! 
# U
# => MAKE ME A PALINDROME!!EMORDNILAP A EM EKAM
# Testcase2:
# 0123ABC
# L
# => MAKE ME A PALINDROME!!EMORDNILAP A EM EKAM
# Testcase1:
# STOP
# => OK, stopping.
def string_process():
    str_input = input("Please enter a string to convert:\n")
    str_palindrome = in_reverse(str_input)
    str_result = str_input + str_palindrome
    if str_input == "STOP":
        return "OK, stopping."
    else:    
        print("Would you like and uppercase or lowercase palindrome?") 
        case_user_requir = input("Enter U for uppercase and L for lowercase.\n")
        if case_user_requir == "U":
            print("Here is your uppercase palindrome:\n"+to_upper(str_result))
            return string_process()
        elif case_user_requir == "L":
            print("Here is your lowercase palindrome:\n"+to_lower(str_result))
            return string_process()
#run the function for test
print(string_process())