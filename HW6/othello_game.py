import turtle
import os
from turtle import Turtle, colormode
SQUARE = 50
color_list = ["Black","White"]
empty_position_set = set()
black_set = set()
white_set = set()

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

def draw_lines(turt, n):
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()

# Function: init_empty_position_set
# Parameters: n, an int for # of squares
# Signature: init_empty_position :: Integer => Set 
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
 
# Function: init_first_four_tiles
# Parameters: n, an int for # of squares
# Parameters: color_number, an int for representing black or white
# Signature: init_first_four_tiles :: (Integer,Integer) => Void
# Returns: nothing
# Does: initialize the first four tiles to start the game
# Example: init_first_four_tiles(4,1) => 
# draw black tile at column 2 row 2, and column 3 row 3
# draw white tile at column 3 row 2, and column 2 row 3
def init_first_four_tiles(n):
    global color_number
    x=int(n/2)
    y=int(n/2)
    for y in range(int(n/2),int(n/2 + 2)):
        for x in range(int(n/2),int(n/2 + 2)):
            color = color_list[(color_number-1) % 2]
            draw_tile(n,x,y,color_number)
            color_number += 1
        # do same thing when x changed   
        color_number += 1    
    print()
    color = color_list[(color_number-1) % 2]
    print("You choose %s. Ready? Game starts!" % color)


# Function: draw_tile
# Signature: draw_tile :: (Integer,Integer,Integer,Integer) => Void
# Parameters: n, an int for # of squares
# Parameters: x, an int for row number
# Parameters: y, an int for column number
# Parameters: color_number, an int for representing black or white
# Returns: nothing
# Does: draw the tile with expected position and color
# Example: draw_tile(4,1,1,1) => draw a black tile at column 1 row 1          
def draw_tile(n,x,y,color_number):
    while (x>=1 and x<=n and y>=1 and y<=n):
        try:
            color = color_list[(color_number-1) % 2]
            othello = turtle.Turtle()
            othello.hideturtle()
            othello.speed(0)
            othello.penup()   
            corner = -n * SQUARE / 2
            othello.setposition(corner+SQUARE/2+(y-1)*SQUARE,corner+(x-1)*SQUARE+5)
            othello.pendown()
            othello.color('black')
            othello.fillcolor(color)
            othello.begin_fill()
            othello.circle(SQUARE/2-5)
            othello.end_fill()
            othello.penup() 
            update_lst(x,y,color_number) 
            is_game_over()
        except ValueError:
            continue
        else:
            break   




# function is_game_over() will check the empty_position_dict. 
# if that dict become empty, it will call result related function in HW7     
def is_game_over():
    if empty_position_set == set():
        # In home work 7 here will be calling result related function
        print("No more position.")
        os._exit(0)


# Function update_dict: initialize the first four tiles to start the game
def update_lst(x,y,color_number): 
    global black_set
    global white_set
    global empty_position_set
    if color_list[(color_number-1) % 2] is "Black":
        black_set.add((x,y)) 
        empty_position_set.remove((x,y))
    elif color_list[(color_number-1) % 2] is "White":
        white_set.add((x,y))
        empty_position_set.remove((x,y))
    print("White positions:\n %s " %white_set) 
    print("Black positions:\n %s " %black_set) 
    print("Empty positions:\n %s " %empty_position_set)

               

# Function: get_pos_to_draw
# Signature: get_pos_to_draw :: (Integer,Integer) => Void
# Parameters: x, an int for row number
# Parameters: y, an int for column number
# Returns: nothing
# Does: got the position when the mouse click on the board
#       and draw a tile on that position with the current color       
def get_pos_to_draw(i,j):
    global x
    global y
    global color_number
    x=int(i/SQUARE+1+n/2)
    y=int(j/SQUARE+1+n/2)
    if x <= n and y <= n:
        draw_tile(n,y,x,color_number)
        color_number+=1   

# main function for running the game
def main():
    print("Welcome to Othello Game!")
    # Prompt user to enter the size of board
    while True:
        try:
            global n 
            n = int(input("Please enter board size: "))
            if n % 2 != 0:
                raise ValueError
        except ValueError:
            print("Valid size should be an even number.")
            continue
        else:
            break
    
    draw_board(n)

    init_empty_position_set(n)

    # Prompt user to choose color
    while True:
        try:
            global color_number
            color_number = int(input("Please choose your color by entering: \"1\" for Black, \"2\" for White: "))
            if color_number not in [1,2]:
                raise ValueError
        except ValueError:
            print("Valid color should be \"1\" for Black or \"2\" for White.")
            continue
        else:
            break
    init_first_four_tiles(n)
    # click on position on the board to draw tile
    s = turtle.getscreen()
    s.onclick(get_pos_to_draw)
    turtle.hideturtle()
    


main()
turtle.done()