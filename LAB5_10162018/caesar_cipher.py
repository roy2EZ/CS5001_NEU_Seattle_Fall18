# To generate a list with alphabet order 
# For example "a" at position 0, "b" at position 1 ... "z" at position 25 in the list
list_alphabet = [chr(i) for i in range(97,123)]

# Part 1: To create a encryption function
def caesar_cipher_encryption(plaintext,shift):
    valid_shift = int(shift) % 26
    length = len(plaintext)
    # To create a empty ciphertext list for carrying future output
    ciphertext = [list() for j in range(length)]
    # Transfer each letter in plaintext to ciphertext 
    for i in range(length):
        if plaintext[i].lower() in list_alphabet: 
            j = (int(list_alphabet.index(plaintext[i].lower())) + valid_shift) % 26
            ciphertext[i] = list_alphabet[j]
        else:
            ciphertext[i] = plaintext[i].lower()
    # Join each letter in the ciphertext list to make it as a string to output
    ciphertext_str = str("".join(ciphertext))
    return ciphertext_str
    # Output all information to user
    

# Part 2: To create a decryption function
def caesar_cipher_decryption(ciphertext,shift):
    valid_shift = int(shift) % 26
    length = len(ciphertext)
    # To create a empty plaintext list for carrying future output
    plaintext = [list() for j in range(length)]
    # Transfer each letter in ciphertext to plaintext 
    for i in range(length):
        if ciphertext[i].lower() in list_alphabet: 
            j = (int(list_alphabet.index(ciphertext[i].lower())) - valid_shift) % 26
            plaintext[i] = list_alphabet[j]
        else:
            plaintext[i] = ciphertext[i].lower()
    # Join each letter in the ciphertext list to make it as a string to output
    plaintext_str = str("".join(plaintext))
    return plaintext_str
    # Output all information to user



def main():
    plaintext = input("Please enter a plaintext: \n")
    shift = input("Please enter a shift number: \n")
    print("The encrypted ciphertext is: %s" % caesar_cipher_encryption(plaintext,shift))
    print("")
    print("... decrypting ciphertext now ...")
    print("The decrypted plaintext is: %s" % caesar_cipher_decryption(caesar_cipher_encryption(plaintext,shift),shift))



# Part 3: To create a decryption function with shift and slide

# Part 3.1: Shift
def decryption_shift(ciphertext):
    length = len(ciphertext)
    # To create a empty plaintext list for carrying future output
    plaintext = [list() for j in range(length)]
    # Try all shift from 0 to 25 to show every plaintext result at the output
    for shift in range(26):
        # Transfer each letter in ciphertext to plaintext 
        for i in range(length):
            if ciphertext[i].lower() in list_alphabet: 
                j =  (int(list_alphabet.index(ciphertext[i].lower())) - shift) % 26
                plaintext[i] = list_alphabet[j]
            else:
                plaintext[i] = ciphertext[i].lower()
        print(str(shift) + ": " + str("".join(plaintext)))
         


