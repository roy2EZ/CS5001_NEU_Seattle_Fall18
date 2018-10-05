#### Purpose
# This function takes a string as input and returns the uppercase version of the string
#### Signature
# to_upper :: String => String
#### Template
# def to_upper(given...):
# return returns...
#### Examples
# to_upper(“test string 9000”) => “TEST STRING 9000”
# to_upper(“ThIs Is A sTrInG”) => “THIS IS A STRING”

def to_upper(string):  
    s1=list(string)
    s2=list(s1)
    i=0
    while i<len(s1):
        if ord(s1[i]) >= 97 and ord(s1[i]) <= 122:
            s2[i]=str(chr(ord(s1[i]) - 32))   
        i += 1
    return "".join(s2)


#### Purpose
# This function takes a string as input and returns the lowercase version of the string
#### Signature
# to_lower :: String => String
#### Template
# def to_lower(given...):
# return returns...
#### Examples
# to_lower(“SHOUTY STRING”) => “shouty string”
# to_lower(“ThIs Is A sTrInG”) => “this is a string”
def to_lower(string):   
    s1=list(string)
    s2=list(s1)
    i=0
    while i<len(s1):
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
# in_reverse(“Tuesday 3:00 PM”) => “MP 00:3 yadseuT”
# in_reverse(“abcde”) => “edcba”
def in_reverse(string): 
    s1=list(string)
    s2=list(s1)
    i=0
    while i<len(s1):
        s2[i]=s1[-i-1]    
        i += 1
    return  "".join(s2)


def string_process():
    str_input = input("Please enter a string to convert:\n")
    str_palindrome = in_reverse(str_input)
    str_result = str_input + str_palindrome
    print("Would you like and uppercase or lowercase palindrome?") 
    case_user_requir = input("Enter U for uppercase and L for lowercase.\n")
    if str_input == "STOP":
        return "OK, STOP"
    else:    
        if case_user_requir == "U":
            print(to_upper(str_result))
            return string_process()
        elif case_user_requir == "L":
            print(to_lower(str_result))
            return string_process()
    
        
            
        
    
print(string_process())  
    
