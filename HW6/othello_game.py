import turtle
from turtle import Turtle, colormode
SQUARE = 50
color_list = ["Black","White"]
empty_position_dict = {}
occupied_position_dict = {}


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

# Function: init_empty_position_dict (for future use in HW7)
# Parameters: n, an int for # of squares
# Signature: init_empty_position_dict :: Integer => Dictionary  
# Returns: Dictionary
# Does: initialize a dictionary of all positions on the board with color as None
#       the dictionary can be use to restore all tiles color and position info for future use  
# Example: init_empty_position_dict(2) =>
# {(1, 1): None, (1, 2): None, (2, 1): None, (2, 2): None}
def init_empty_position_dict(n):
    count = 0
    color = None
    for y in range(1,n+1):
        for x in range(1,n+1):
            empty_position_dict[y,x] = color
    return empty_position_dict     
 
# Function: init_first_four_tiles
# Parameters: n, an int for # of squares
# Parameters: color_number, an int for representing black or white
# Signature: init_first_four_tiles :: (Integer,Integer) => Void
# Returns: nothing
# Does: initialize the first four tiles to start the game
# Example: init_first_four_tiles(4,1) => 
# draw black tile at column 2 row 2, and column 3 row 3
# draw white tile at column 3 row 2, and column 2 row 3
def init_first_four_tiles(n,color_number):
    x=int(n/2)
    y=int(n/2)
    for x in range(int(n/2),int(n/2 + 2)):
        for y in range(int(n/2),int(n/2 + 2)):
            draw_tile(n,x,y,color_number)
            color = color_list[(color_number+1) % 2]
            empty_position_dict[y,x] = color
            # pop that tile into occupied_position_dict
            occupied_position_dict[y,x] = empty_position_dict.pop((y,x))
            # change tile color
            color_number += 1
        # do same thing when x changed   
        empty_position_dict[y,x] = color
        occupied_position_dict[y,x] = empty_position_dict.pop((y,x))
        color_number += 1
    print()   
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
    color = color_list[color_number % 2]
    othello = turtle.Turtle()
    othello.hideturtle()
    othello.speed(0)
    othello.penup()   
    corner = -n * SQUARE / 2
    othello.setposition(corner+SQUARE/2+(y-1)*SQUARE, corner+(x-1)*SQUARE)
    othello.pendown()
    othello.color('black')
    othello.fillcolor(color)
    othello.begin_fill()
    othello.circle(SQUARE/2)
    othello.end_fill()
    # Restore the tile color at column y row x into empty_position_dict
    empty_position_dict[y,x] = color
    # pop that tile into occupied_position_dict
    occupied_position_dict[y,x] = empty_position_dict.pop((y,x))
    
    
# main function for running the game
def main():
    print("Welcome to Othello Game!")
    # Prompt user to enter the size of board
    while True:
        try:
            n = int(input("Please enter board size: "))
            if n % 2 != 0:
                raise ValueError
        except ValueError:
            print("Valid size should be an even number.")
            continue
        else:
            break
    # To draw the board        
    draw_board(n)
    # To iniinitialize a dictionary of all legal positions for future use
    init_empty_position_dict(n)
    # To prompt user to choose a color for his tile
    while True:
        try:
            color_number = int(input("Please choose your color by entering: \"1\" for Black, \"2\" for White: "))
            if color_number not in [1,2]:
                raise ValueError
        except ValueError:
            print("Valid color should be \"1\" for Black or \"2\" for White.")
            continue
        else:
            break
      
    # To initialize the first four tiles to start the game        
    init_first_four_tiles(n,color_number)
    # To let user input column number of expected tile position
    while True:
        while True:
            try:
                y = int(input("Please enter the column number (1 to %d as left to right) to set your tile: " %n))
                if y < 1 or y > n:
                    raise ValueError
            except ValueError:
                print("Valid range should be 1~%d." %n)
                continue
            else:
                break 
        # To let user input row number of expected tile position        
        while True:
            try:
                x = int(input("Please enter the row number (1 to %d as bottom to top) to set your tile: " %n))
                if x < 1 or x > n:
                    raise ValueError
            except ValueError:
                print("Valid range should be 1~%d." %n)
                continue
            else:
                break   
        # To draw the tile
        color_number += 1          
        draw_tile(n,x,y,color_number)
        color = color_list[(color_number+1) % 2]
        print()
        print("Now it's turn of %s to go: " % color)
       

# Run the main function to start the game        
main()

turtle.done()