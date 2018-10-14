import random
#### Purpose
# To prompt the user to input rock, scissors or paper and
# and make a random throw of rock, scissors or paper to play the game with user
# output the win or lose result 
#### Signature
# rsp_game :: (String) => String
#### Template
# def rsp_game(given):
#    return returns...
#### Examples
#  R vs S => Rock smashes scissors! You win!
#  s vs S => OMG it's a tie!!!
#  paper vs S => Scissors cut paper! You lose!
#  ninja => That is not a rock, scissors, or paper, sorry, no game

#Welcome title
print("Let's play! RSP Human vs Machine EPIC SHOWDOWN.")

#set a list for the possible valid inputs for user
option_list = ["R","P","S","ROCK","SCISSORS","PAPER"]
#set a list for computer throws
computer_list = ["R","P","S"]
#set all user win and lose combinations as the conditions for final output
win_1=["P","R"]
win_2=["R","S"]
win_3=["S","P"]
lose_1=["R","P"]
lose_2=["S","R"]
lose_3=["P","S"]

def rsp_game(user_throw):
    #user upper() to make user input case-insensitive
    user_throw=user_throw.upper()
    #create a ramdon computer throw from the computer_list which is R, P or S
    computer_throw=random.choice(computer_list) 
    #if user input is invalid, give output
    if user_throw not in option_list:
        return "That is not a rock, scissors, or paper, sorry, no game"
    
    else:   
        #if user input is valid, print that user input and computer throw
        #if the user input is the whole word of rock,scissors, or paper, keep the initail to form that input into R,P or S
        print("Your threw: "+ user_throw[:1])
        print("Your enemy threw: "+computer_throw)
        #to compare the user and computer thrwo and give result
        if user_throw[:1] == computer_throw :
            return "OMG it's a tie!!!"
        elif [user_throw[:1],computer_throw] == win_1:
            return "Paper covers rock! You win!"
        elif [user_throw[:1],computer_throw] == win_2:
            return "Rock smashes scissors! You win!"
        elif [user_throw[:1],computer_throw] == win_3:
            return "Scissors cut paper! You win!"
        elif [user_throw[:1],computer_throw] == lose_1:
            return "Rock is covered by paper! You lose!"
        elif [user_throw[:1],computer_throw] == lose_2:
            return "Scissors is smashed by rock! You lose!"
        elif [user_throw[:1],computer_throw] == lose_3:
            return "Paper is cut by scissors! You lose!"
    
        
s = input("R,S,or P:\n")
print(rsp_game(s))