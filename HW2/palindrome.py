#### Purpose
# To prompt the user for a string and reports whether it is a palindrome
# The input is case-insensitive and space-insensitive
#### Signature
# palindrome_check :: (String) => String
#### Template
# def palindrome_check(given):
#    return returns...
#### Examples
#  Madam Im Adam         => Palindrome!
#  上海自来水来自海上      => Palindrome!
#  Taco cat              => Palindrome!
#  ?Was it a cat I saw?  => Palindrome!
#  Yo r "Sex at noon taxes" Roy  => Palindrome!
#  Madam, I'm Adam.      => Not a palindrome :(
#  taco cat!             => Not a palindrome :(
#  Not nil: Clinton!     => Not a palindrome :(
#  No x in Nixon.        => Not a palindrome :(
#  自我突破，突破自我      => Not a palindrome :(
def palindrome_check(string):
    #make the string as a list and use replace() to remove space and upper() for case-insensitive
    string = list(string.replace(' ', '').upper())
    #make variable length as the length of the string
    length = len(string)
    #set up the start charactor of left and right of that string
    left = 0
    right = length - 1
    while left < right:
        if string[left] != string[right]:
            return "Not a palindrome :("
        left += 1
        right -= 1
    return "Palindrome!"

s = input("Please enter a word to check if it is palindrome:\n")
print(palindrome_check(s))