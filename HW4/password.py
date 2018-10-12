#### Purpose
# To check if a string contains at least upper letters A~Z or lower letters a~z:
# If the string does not contain any upper or lower letters, return False
# If the string contains at least 1 upper or lower letter, return True
#### Signature
# is_letter() :: (String) => Boolean
#### Template
# def is_letter(given...):
#     return returns...
#### Examples
# is_letter("abcdefg") => True
# is_letter("ABCDEFG") => True
# is_letter("ABCDefgh") => True
# is_letter("AbCd12&*") => True
# is_letter("12345678") => False
# is_letter("!@#$%^&*") => False
# is_letter("!@#$%1234") => False
#### Function Definition
def is_letter(password):
    return (password.upper().isupper() or password.lower().islower())
#### Tests
def test_is_letter():
    assert(is_letter("abcdefg") == True)
    assert(is_letter("ABCDEFG") == True)
    assert(is_letter("ABCDefgh") == True)
    assert(is_letter("AbCd12&*") == True)
    assert(is_letter("12345678") == False)
    assert(is_letter("!@#$%^&*") == False)
    assert(is_letter("!@#$%1234") == False)
    
#### Purpose
# To check if a string contains number in 0~9:
# If the string does not contain any number in 0~9, return False
# If the string contains at least 1 number in 0~9, return True
#### Signature
# is_number() :: (String) => Boolean
#### Template
# def is_number(given...):
#     return returns...
#### Examples
# is_number("1234567") => True
# is_number("abcd9efg") => True
# is_number("abcdEFGH") => False
# is_number("!@#$%^&*") => False
# is_number("abCD$%#^") => False
#### Function Definition
def is_number(password):
    return any(char.isdigit() for char in password)
#### Tests
def test_is_number():
    assert(is_number("1234567") == True)
    assert(is_number("abcd9efg") == True)
    assert(is_number("abcdEFGH") == False)
    assert(is_number("!@#$%^&*") == False)
    assert(is_number("abcd$%#^") == False)

#### Purpose
# To check if a string contains any special character of ! @ # $
# If the string does not contain any special character of ! @ # $, return False
# If the string contains at least 1 special character of ! @ # $, return True
#### Signature
# is_spec_char() :: (String) => Boolean
#### Template
# def is_spec_char(given...):
#     return returns...
#### Examples
# is_spec_char("!Q@w#e$R") => True
# is_spec_char("chen.rongy@husky.neu.edu") => True
# is_spec_char("abcdefg") => False
# is_spec_char("1234?*&^") => False
# is_spec_char("abcdEFG123") => False
#### Function Definition
def is_spec_char(password):
    return (("!" in password) or ("@" in password) or ("#" in password) or ("$" in password))
#### Tests
def test_is_spec_char():
    assert(is_spec_char("!Q@w#e$R") == True)
    assert(is_spec_char("chen.rongy@husky.neu.edu") == True)
    assert(is_spec_char("abcdefg") == False)
    assert(is_spec_char("1234?*&^") == False)
    assert(is_spec_char("abcdEFG123") == False)


#### Purpose
# To check if a string is too short which is less than 6 characters:
# If the string is less than 6 characters, return False
# If the string is with 6 or more characters, return True
#### Signature
# is_length_tooshort() :: (String) => Boolean
#### Template
# def is_length_tooshort(given...):
#   return returns...
#### Examples
# is_length_tooshort("123456") => True
# is_length_tooshort("12345") => False
#### Function Definition
def length_tooshort(password):
    return (len(password) >= 6)
#### Tests
def test_length_tooshort():
    assert(length_tooshort("!2cD56") ==  True)
    assert(length_tooshort("!2cD5") == False)

#### Purpose
# To check if a string is too long which is more than 12 characters.
# If the string is more than 12 characters, return False
# If the string is with 12 or less characters, return True
#### Signature
# is_length_toolong() :: (String) => Boolean
#### Template
# def is_length_toolong(given...):
#   return returns...
#### Examples
# is_length_toolong("0!23456789Ab") => True
# is_length_toolong("0!23456789Abc") => False
#### Function Definition
def length_toolong(password):
    return (len(password) <= 12)
#### Tests
def test_length_toolong():
    assert(length_toolong("0!23456789Ab") ==  True)
    assert(length_toolong("0!23456789Abc") == False)

#### Main Function Definition
def main():
    password = input("Please enter a password: \n")
    if is_letter(password) == False:
        print("Please enter valid password with at least 1 letter.")
        main()       
    elif is_number(password) == False:
        print("Please enter valid password with at least 1 number:0-9")
        main()                
    elif  is_spec_char(password) == False:
        print("Please enter valid password with at least 1 special character of $, #, @ or !")
        main() 
    elif length_tooshort(password) == False:
        print("Please enter valid password with at least 6 characters.")
        main() 
    elif length_toolong(password) == False:
        print("Please enter valid password with at most 12 characters.")
        main() 
    else:
        print("This is a valid password.")

#### Run the main function        



    


