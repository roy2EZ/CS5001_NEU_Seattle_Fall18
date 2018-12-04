import turtle
import os
from turtle import Turtle, colormode
SQUARE = 50
color_list = ["B","W"]
empty_position_set = set()
black_set = set()
white_set = set()
user_color = None
enemy_color = None
current_color_num = 0


#1 Game initialize-----------------------------------------------------------

# Function: draw_board
# Parameters: n, an int for # of squares
# Signature: draw_board:: Integer => Void
# Returns: nothing
# Does: Draws an nxn board with a green background
# Example: draw_board(4) => a 4*4 board 
def draw_board(n):
    turtle.setup(n * SQUARE + SQUARE, n * SQUARE + SQUARE)
    turtle.screensize(n * SQUARE, n * SQUARE)
    turtle.bgcolor('white')

    # Create the turtle to draw the board
    othello = turtle.Turtle()
    othello.penup()
    othello.speed(0)
    othello.hideturtle()

    # Line color is black, fill color is green
    othello.color("black", "forest green")

    # Move the turtle to the upper left corner
    corner = -n * SQUARE / 2
    othello.setposition(corner, corner)

    # Draw the green background
    othello.begin_fill()
    for i in range(4):
        othello.pendown()
        othello.forward(SQUARE * n)
        othello.left(90)
    othello.end_fill()

    # Draw the horizontal lines
    for i in range(n + 1):
        othello.setposition(corner, SQUARE * i + corner)
        draw_lines(othello, n)

    # Draw the vertical lines
    othello.left(90)
    for i in range(n + 1):
        othello.setposition(SQUARE * i + corner, corner)
        draw_lines(othello, n)

    # Write coordinates for user easily to find row and column number
    for i in range(n):
        othello.setposition(corner+SQUARE/2+i*SQUARE,corner-18)
        othello.write("%d" % int(i+1), font=("Arial", 10, "normal"))
    for j in range(n):
        othello.setposition(corner-10,corner+SQUARE/3+j*SQUARE)
        othello.write("%d" % int(j+1), font=("Arial", 10, "normal"))

    turtle.hideturtle()

# Function: draw_lines
# Does: called to draw the lines in the board
def draw_lines(turt, n):
    turt.hideturtle()
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()

# Function: init_empty_position_set
# Parameters: n, an int for # of squares
# Signature: init_empty_position_set :: Integer => Set 
# Returns: Set
# Does: initialize a set of all empty positions on the board 
# Example: init_empty_position_set(2) =>
#{(1, 1), (1, 2), (2, 1), (2, 2)}
def init_empty_position_set(n):
    global empty_position_set
    for i in range(int(n*n)):
        for y in range(1,n+1):
            for x in range(1,n+1):
                empty_position_set.add((x,y))
    return empty_position_set

# Function: init_four_tile
# Parameters: n, an int for # of squares
# Signature: init_four_tile :: (Integer,Integer) => Void
# Returns: nothing
# Does: initialize to draw the first four tiles to start the game
# Example: init_four_tile(4) => 
# draw black tile at column 2 row 2, and column 3 row 3
# draw white tile at column 3 row 2, and column 2 row 3
def init_four_tile(n):
    global current_color_num
    a=int(n/2)
    b=int(n/2)
    draw_tile(a,b)
    draw_tile(a+1,b+1)
    if current_color_num == 0:
        current_color_num+=1
        draw_tile(a+1,b)
        draw_tile(a,b+1)
        current_color_num-=1
    if current_color_num == 1:
        current_color_num-=1
        draw_tile(a+1,b)
        draw_tile(a,b+1)
        current_color_num+=1



#2 User input-----------------------------------------------------------------------------------------

# Function: user_input_n
# Does: let user input the n for drawing n*n board
# Example: user_input_n => user will input the n
def user_input_n():
    while True:
        try:
            global n
            n = int(input("Please enter board size: "))
            if n % 2 != 0 or n <= 2:
                raise ValueError
        except ValueError:
            print("Valid size should be an positive even number and greater than 2.")
            continue
        else:
            break

# Function: user_choose_color
# Does: let user input the color he wanna use for game
# Example: user_choose_color => user will input the color
def user_choose_color():
    while True:
        try:
            global user_color
            global enemy_color
            global current_color_num
            user_color = input("Please choose your color - B for Black, W for White: ").upper()
            if user_color not in color_list:
                raise ValueError
            # user choose black:
            if user_color == color_list[0]:
                enemy_color = color_list[1]
                current_color_num = color_list.index(user_color)
            # user choose white:
            elif user_color ==  color_list[1]:
                enemy_color = color_list[0]
                current_color_num = color_list.index(user_color)
        except ValueError:
            print("Please enter valid color input - B for Black, W for White:")
            continue
        else:
            break


# 3 Draw operation------------------------------------------------------------------------------------

# Function: draw_tile
# Parameters: x, y which are two integers for row and column number
# Signature: draw_tile :: (Integer,Integer) => Void
# Returns: nothing
# Does: draw a tile at row x column y
# Example: draw_tile(3,4) => 
# draw tile at row 3 column 4
def draw_tile(x,y):
    global current_color_num
    othello = turtle.Turtle()
    othello.hideturtle()
    othello.speed(0)
    othello.penup()
    corner = -n * SQUARE / 2
    othello.setposition(corner+SQUARE/2+(y-1)*SQUARE,corner+(x-1)*SQUARE+5)
    othello.pendown()
    othello.color('black')
    if current_color_num == 0:
        othello.fillcolor('black')
    elif current_color_num == 1:
        othello.fillcolor('white')
    othello.begin_fill()
    othello.circle(SQUARE/2-5)
    othello.end_fill()
    othello.penup()
    othello.hideturtle()
    update_set(x,y)


# Function: click_to_game
# Does: when user click the screen, do the draw_operation function
def click_to_game():
    s = turtle.getscreen()
    s.onclick(draw_operation)
    turtle.done()

# Function: draw_operation
# Parameters: i, j which are two numbers get from the point by mouse click on screen
# Signature: draw_operation :: (Integer,Integer) => Void
# Returns: nothing
# Does: will operate the draw tile function with different game situation
# Example: draw_operation(200,100) => will draw tile by condition 
def draw_operation(i,j):
    global x
    global y
    global current_color_num
    global has_user_click
    # transfer the i,j by mouse clicking 
    # into x row y column position on the board
    SQUARE*(int(n/2))
    x=int(j/SQUARE+1+n/2)
    y=int(i/SQUARE+1+n/2)
    
    # Human vs Computer mode-------------------------------
    if vs_mode == 1:
        # user(human) draw his tile
        human_finish_flag = False
        # check if it is legal move
        if check_legal_move() == True:
            flip_set = get_flip_position(x,y)
            if len(flip_set)>0:
                draw_tile(x,y)
                for (x,y) in flip_set:
                    draw_tile(x,y)
                if is_game_over():
                    os._exit(0)
                if current_color_num == 1:
                    current_color_num = 0
                    human_finish_flag = True
                elif current_color_num == 0:
                    current_color_num = 1
                    human_finish_flag = True
        # if it is not legal move
        elif check_legal_move() == False:
            if current_color_num == 0:
                current_color_num = 1
                if check_legal_move() == False:
                    game_over()
                    os._exit(0)
                elif check_legal_move == True:
                    print("Black has no move. It's White turn.")    
            elif current_color_num == 1:
                current_color_num = 0
                if check_legal_move() == False:
                    game_over()
                    os._exit(0)
                elif check_legal_move() == True:
                    print("White has no move. It's Black turn.") 

        # computer turn to draw 
        if human_finish_flag == True:
            if check_legal_move() == True:
                (com_x,com_y) = get_computer_draw_pos()
                # computer draw with calling the AI function
                flip_set = get_flip_position(com_x,com_y)
                if len(flip_set)>0:
                    draw_tile(com_x,com_y)
                    for (x,y) in flip_set:
                        draw_tile(x,y)
                    if is_game_over():
                        os._exit(0)
                    color_change()    

            elif check_legal_move() == False:
                color_change()
                if check_legal_move() == False:
                    game_over()
                    os._exit(0)

    # Human vs Human mode-------------------------------------------
    elif vs_mode == 2:
        
        if check_legal_move() == True:
            flip_set = get_flip_position(x,y)
            # if it's black turn
            if current_color_num == 0 and len(flip_set) > 0:
                # draw the tile
                draw_tile(x,y)
                #flip the tiles
                for (x,y) in flip_set:
                    draw_tile(x,y)
                    #check if game is over
                    if is_game_over():
                        os._exit(0)
                # go to enemy turn        
                current_color_num = 1
            #if it's white turn
            elif current_color_num == 1 and len(flip_set) > 0:
                draw_tile(x,y)
                for (x,y) in flip_set:
                    draw_tile(x,y)
                    if is_game_over():
                        os._exit(0)
                current_color_num = 0

        if check_legal_move() == False:
            if current_color_num == 0:
                current_color_num = 1
                if check_legal_move() == False:
                    game_over()
                    os._exit(0)
                elif check_legal_move == True:
                    print("Black has no move. It's White turn.")    
            
            elif current_color_num == 1:
                current_color_num = 0
                if check_legal_move() == False:
                    game_over()
                    os._exit(0)
                elif check_legal_move() == True:
                    print("White has no move. It's Black turn.") 

                
# Function: color_change
# Does: to change the current color from black to white 
# or from white to black after draw tile
def color_change():
    global current_color_num
    if current_color_num == 1:
        current_color_num = 0
    elif current_color_num == 0:
        current_color_num = 1     
    

# 4 AI ---------------------------------------------------------------------------------

# Function: get_computer_draw_pos
# Returns: x,y as two integer for row and column number
# Does: get the best location for computer to draw 
#       which computer can get most flip tiles in its round
def get_computer_draw_pos():
    length_flip_set = 0
    pos = ()
    legal_set = get_legal_move_set()
    for (x,y) in legal_set:
        flip_set = get_flip_position(x,y)
        temp_len = len(flip_set)
        if temp_len > length_flip_set:
            length_flip_set = temp_len
            pos = (x,y)
    return x,y



# 5 legal move--------------------------------------------------------------------

# Function: get_flip_position
# Parameters: x,y as two integer for row and column number
# Returns: Set
# Signature: get_flip_position:: (Integer, Integer)=>Set
# Does: get the flip positions for the legal position which tile will be draw
def get_flip_position(x,y):
    # dirs are the 8 directions: 
    # up, down, left, right, upright,upleft, downright,downleft
    dirs = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    set_cur = set()
    set_oppsite = set()
    global black_set
    global white_set
    global current_color_num
    flip_set = set()
    
    if current_color_num == 0:
        set_cur = black_set
        set_oppsite = white_set
    elif current_color_num == 1:
        set_cur = white_set
        set_oppsite = black_set

    for dir in dirs:
        temp_set = set()
        cur_x = x + dir[0];
        cur_y = y + dir[1];
        if check_inside_board(cur_x,cur_y) == False:
            continue
        elif is_in_empty_set(cur_x,cur_y) == True:
            continue
        elif (cur_x,cur_y) in set_cur:
            continue
        temp_set.add((cur_x,cur_y))

        sameColorFoundFlag = False

        while not sameColorFoundFlag:  
            
            cur_x = cur_x + dir[0]
            cur_y = cur_y + dir[1]
            if check_inside_board(cur_x, cur_y) == False:
                break
            elif is_in_empty_set(cur_x,cur_y) == True:
                break
            elif (cur_x,cur_y) in set_oppsite:
                temp_set.add((cur_x,cur_y))

            elif (cur_x,cur_y) in set_cur:    
                sameColorFoundFlag = True
                break
        if sameColorFoundFlag == True:        
            for position in temp_set:
                flip_set.add(position)
    return flip_set

# Function: check_legal_move
# Returns: Boolean
# Signature: get_flip_position:: Void => Boolean
# Does: Check if current player has legal move
def check_legal_move():
    legal_set = set()
    for (x,y) in empty_position_set:
        flip_set = get_flip_position(x,y)
        if len(flip_set)>0:
            legal_set.add((x,y))
    
    if len(legal_set) > 0:
        return True
    else:
        return False

# Get the legal move sets for that legal position to draw
def get_legal_move_set():
    legal_set = set()
    for (x,y) in empty_position_set:
        flip_set = get_flip_position(x,y)
        if len(flip_set)>0:
            legal_set.add((x,y))
    return legal_set


# functions for checking if that position in empty set or if out of board

# Function: is_in_empty_set
# Does: check if the position x,y in the empty set which means there is no tile
# Signature: is_in_empty_set :: (Integer,Integer) => Boolean
def is_in_empty_set(x,y):
    return (x,y) in empty_position_set

# Function: check_inside_board
# Does: check if the position x,y is inside the n*n board
# Signature: check_inside_board :: (Integer,Integer) => Boolean        
def check_inside_board(x,y):
    global n
    if x>=1 and x<=n and y>=1 and y<=n:
        return True
    else:
        return False


# 6 Update tile position related set-----------------------------------------------

# Function: update_set
# Does: update the set for black or white or empty set, after each tile drawing
# Example: update_set(2,3) => if color is black, (2,3) will add into black_set
#          update_set(3,1) => if color is white, (3,1) will add into white_set
def update_set(x,y):
    if (x,y) in empty_position_set:
        empty_position_set.remove((x,y))
        if current_color_num == 0:
            black_set.add((x,y))
        elif current_color_num == 1:
            white_set.add((x,y))
    else:
        if current_color_num == 0:
            white_set.remove((x,y))
            black_set.add((x,y))
        elif current_color_num == 1:
            black_set.remove((x,y))
            white_set.add((x,y))
        



# 7 Game over operation--------------------------------------------------------------------------

# Function: is_game_over
# Does: judge if it is game over
# if game is over, do the related function 
# and return True, otherwise return false
def is_game_over():
    if empty_position_set == set() or black_set == set() or white_set == set():
        game_over()
        return True
    else:
        return False

# Function: game_over
# Does: output the game result and write high score into the file
def game_over():
    white_number = len(white_set)
    black_number = len(black_set)
    winner_score = 0
    winner_color = str()
    if white_number > black_number: 
        winner_color = "W"
        winner_score = white_number   
        print("White is the winner.")
        print("White: ", white_number)
        print("Black: ", black_number)
    elif black_number > white_number:
        winner_color = "B"
        winner_score = black_number
        print("Black is the winner.")
        print("Black: ", black_number)
        print("White: ", white_number)
    elif black_number == white_number:
        winner_color == user_color
        winner_score = black_number
        print("Game is tie.")
        print("Black: ", black_number)
        print("White: ", white_number)

    #high score file update
    if winner_color == user_color:
        name = str(input("Please enter your name: "))
        winner_str = name + " " + str(winner_score)
        file_path = "C:/Users/roych/Documents/CS5001/student_repo_roychen/HW7/scores.txt"
        file = open(file_path, "r")
        contents = file.readlines()
        file.close()
        if (contents is '') or (len(contents) == 0) or (contents[0] is '') or (contents[0] is None):
            file.write(winner_str)
        else:
            lst = contents[0].split(" ")
            score = int(lst[-1].strip())
            if winner_score >= score:
                contents.insert(0, winner_str+'\n')
            elif winner_score < score:
                contents.append(winner_str+'\n')
        file = open(file_path, "w")    
        for i in range(len(contents)):
            file.write(contents[i])
        file.close()
                

# 8 Main function----------------------------------------------------------------------------------
def main():
    print("Welcome to Othello Game!")
    user_input_n()
    draw_board(n)
    user_choose_color()
    init_empty_position_set(n)
    init_four_tile(n)
    # let user choose enemy is computer or another human
    global vs_mode
    vs_mode = int(input("Please choose your enemy - 1 for computer, 2 for another player: "))
    click_to_game()
    turtle.done()



# Run the game using main function        
main()



