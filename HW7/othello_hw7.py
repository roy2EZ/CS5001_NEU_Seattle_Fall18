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


# game init----------------------------------------------------------------------
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

def draw_lines(turt, n):
    turt.hideturtle()
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()

def init_empty_position_set(n):
    global empty_position_set
    for i in range(int(n*n)):
        for y in range(1,n+1):
            for x in range(1,n+1):
                empty_position_set.add((x,y))
    return empty_position_set


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



# user input----------------------------------------------------------------
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


# draw operation-------------------------------------------------------------------------
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



def click_to_game():
    s = turtle.getscreen()
    s.onclick(draw_operation)
    turtle.done()

def draw_operation(i,j):
    global x
    global y
    global current_color_num
    global has_user_click
    

    SQUARE*(int(n/2))
    x=int(j/SQUARE+1+n/2)
    y=int(i/SQUARE+1+n/2)
    
    
    # Human vs Human mode
    if vs_mode == 2:
        
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


                   
    
    # Human vs Computer mode
    elif vs_mode == 1:
        # draw human (x,y)
        human_finish_flag = False
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

        # computer 
        if human_finish_flag == True:
            if check_legal_move() == True:
                (com_x,com_y) = get_computer_draw_pos()
                # com draw (x,y)
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

def color_change():
    global current_color_num
    if current_color_num == 1:
        current_color_num = 0
    elif current_color_num == 0:
        current_color_num = 1     
    

# AI ---------------------------------------------------------------------------------
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



# legal move--------------------------------------------------------------


def get_flip_position(x,y):
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

def get_legal_move_set():
    legal_set = set()
    for (x,y) in empty_position_set:
        flip_set = get_flip_position(x,y)
        if len(flip_set)>0:
            legal_set.add((x,y))
    return legal_set



def is_in_empty_set(x,y):
    return (x,y) in empty_position_set
        

def check_inside_board(x,y):
    global n
    if x>=1 and x<=n and y>=1 and y<=n:
        return True
    else:
        return False





# update set---------------------------------------------------------------
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
        




# test------------------------------------------------------------------------------------------------
def print_test():
    print("Empty:")
    print(empty_position_set)
    print("black:")
    print(black_set)
    print("white:")
    print(white_set)
    print("current color number - 0 for black, 1 for white: ", current_color_num)
    print("user color: ", user_color)
    print("enemy color: ", enemy_color)
    
    

# operation when game over------------------------------------------------------
def is_game_over():
    if empty_position_set == set() or black_set == set() or white_set == set():
        game_over()
        return True
    else:
        return False

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

    #score file update-------------------------------------------------------------------
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
                

        
        


        









# main---------------------------------------------------------------------------------------------
def main():
    print("Welcome to Othello Game!")
    user_input_n()
    draw_board(n)
    user_choose_color()
    init_empty_position_set(n)
    init_four_tile(n)
    global vs_mode
    vs_mode = int(input("Please choose your enemy - 1 for computer, 2 for another player: "))
    click_to_game()
    turtle.done()
        



main()
