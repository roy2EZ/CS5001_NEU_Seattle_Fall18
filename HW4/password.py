def is_letter(password):
    return (password.isupper() or password.islower())
def test_is_letter():
    assert(is_letter("abcdefg") == True)
    assert(is_letter("ABCDEFG") == True)
    assert(is_letter("AbCdEfG") == True)
    assert(is_letter("!@#$%1234") == False)
    


def is_number(password):
    return any(char.isdigit() for char in password)
def test_is_number():
    assert(is_number("1234567") == True)
    assert(is_number("abcdef7") == True)
    assert(is_number("abcdefg") == False)




def is_spec_char(password):
    return (("!" in password) or ("@" in password) or ("#" in password) or ("$" in password))
def test_is_spec_char():
    assert(is_spec_char("chen.rongy@husky.neu.edu") == True)
    assert(is_spec_char("abcdEFG123") == False)



def length_tooshort(password):
    return (len(password) >= 6)
def test_length_tooshort():
    assert(length_tooshort("123456") ==  True)
    assert(length_tooshort("12345") == False)

def length_toolong(password):
    return (len(password) <= 12)
def test_length_toolong():
    assert(length_toolong("0123456789AB") ==  True)
    assert(length_toolong("0123456789ABC") == False)


def main():
    password = input("Please enter a password: \n")
   
    if is_letter(password) == False:
        print("Please enter valid password with at least 1 letter.")
        main()       
    elif is_number(password) == False:
        print("Please enter valid password with at least 1 number:0-9")
        main()                
    elif  is_spec_char(password) == False:
        print("Please enter valid password with at least 1 special character:$, #, @, !")
        main() 
    elif length_tooshort(password) == False:
        print("Please enter valid password with at least 6 characters.")
        main() 
    elif length_toolong(password) == False:
        print("Please enter valid password with at most 12 characters.")
        main() 
    else:
        print("This is a valid password.")
        
main()


    


