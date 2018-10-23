# To generate a list with alphabet order 
# For example "a" at position 0, "b" at position 1 ... "z" at position 25 in the list
list_alphabet = [chr(i) for i in range(97,123)]

# Part 3: To create a decryption function with shift and slide
def unknown_decryption_slide(ciphertext):
    list_slide = list()
    for i in range(1,6):
        ciphertext_slide_back = (ciphertext[i:]+ciphertext[:i])
        list_slide.append(ciphertext_slide_back)
    return list_slide

def unknown_decryption_shift(ciphertext):
    length = len(ciphertext)
    # To create a empty plaintext list for carrying future output
    plaintext_list = [list() for j in range(length)]
    list_shift = list()
    # Try all shift from 0 to 25 to show every plaintext result at the output
    for shift in range(1,6):
        # Transfer each letter in ciphertext to plaintext 
        for i in range(length):
            if ciphertext[i].lower() in list_alphabet: 
                j =  (int(list_alphabet.index(ciphertext[i].lower())) - shift) % 26
                plaintext_list[i] = list_alphabet[j]
            else:
                plaintext_list[i] = ciphertext[i].lower()
        plaintext_str = str("".join(plaintext_list))
        list_shift.append(plaintext_str)  
    return list_shift

def main():
    ciphertext = input("Please enter the cipher text you wanna decrypt: \n")
    print("Matrix of results: ")
    list_slide = unknown_decryption_slide(ciphertext)
    for i in range(len(list_slide)):
        print(unknown_decryption_shift(list_slide[i]))

#### Tests
# Cipher texts:
# *.glygo rsvvmw'w gshi avmxiw gsqqirxw efsyx *lmq
# aqwuvwem, kp cp kphkpkvg nqqr, ykvj
# .sjajw ywzxy f htruzyjw dtz hfs’y ymwtb tzy f bnsitb..
# yko.vjg swguvkqp qh yjgvjgt eqorwvgtu ecp vjkpm ku nkmg vjgswguvkqp qh yjgvjgt uwdoctkpgu ecp u
# .ejwem pqttku ytkvgu dqqngcp gzrtguukqpu vjcv ctg dqvj vtwg cpfhcnug

#### Results
# chuck norris's code writes comments about *him*.
# stuck, in an infinite loop, withyou
# never trust a computer you can’t throw out a window...
# the question of whether computers can think is like thequestion of whether submarines can swim.
# chuck norris writes boolean expressions that are both true andfalse.



    