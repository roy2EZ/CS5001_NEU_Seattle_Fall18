#### Purpose
# calculate how many bikes the shop owner can make for customer
# by customer input the amounts of wheels, frames and links which customer can provide
# and also calculate the amount of parts left
# Note: 2 wheels 1 frame and 50 links can form 1 bike.
#### Signature
# bikemaker :: (Number,Number,Number)=>Number
#### Template
# def bikemaker(given...):
#    return returns...
#### Examples
# Test input: 2 wheels, 1 frame, 50 links
# Expected output: 1 bike built. Leftover: nothing.
# Test input: 3 wheels, 10 frames, 500 links
# Expected output: 1 bike built. Leftover: 1 wheel, 9 frames, 450 links.
# Test input: 10 wheels, 7 frames, 250 links
# Expected output: 5 bikes built. Leftover: 0 wheels, 2 frames, 0 links.

def bikemaker(wheels, frames, links):
    cw=2 
    #The constant of how many wheels form a bike
    cf=1 
    #The constant of how many frames form a bike
    cl=50
    #The constant of how many links form a bike
    w = wheels//cw
    #The amount of how many bikes can be made by using customer provided wheels
    f = frames//cf
    #The amount of how many bikes can be made by using customer provided frames
    l = links//cl
    #The amount of how many bikes can be made by using customer provided links
    bikes_possible=min(w,f,l)
    #Calculate the real amount of bikes can be made by total
    w_left = wheels-cw*bikes_possible
    #Calculate how many wheels left 
    f_left = frames-cf*bikes_possible
    #Calculate how many frames left 
    l_left = links-cl*bikes_possible
    #Calculate how many links left 
    return "OK, you've got "+str(bikes_possible)+" bikes coming!\n"\
    +"I'm keeping the leftovers for myself:\n"\
    +str(w_left)+" wheels and "+str(f_left)+" frames and "+str(l_left)+" links"
    #return the final results

w_input = input("How many wheels do you have?\n")
#Let user input wheels amount
print("I can make "+str(int(w_input)//2)+" bikes with that.\n")
#calculate bikes amount using those wheels and print the result
f_input = input("How many frames do you have?\n")
#Let user input frames amount
print("I can make "+str(int(f_input)//1)+" bikes with that.\n")
#calculate bikes amount using those frames and print the result
l_input  = input("How many links do you have?\n")
#Let user input links amount
print("I can make "+str(int(l_input)//50)+" bikes with that.\n")
#calculate bikes amount using those links and print the result
print(bikemaker(int(w_input), int(f_input), int(l_input)))
#with all inputs, do the calculation and give final results