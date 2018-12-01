import turtle
import os
from turtle import Turtle, colormode
SQUARE = 50
color_list = ["B","W"]
empty_position_set = set()
black_set = set()
white_set = set()

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
    a=int(n/2)
    b=int(n/2)
    draw_white(a,b)
    draw_white(a+1,b+1)
    draw_black(a+1,b)
    draw_black(a,b+1)
    

def init_test_tile(n):
    a=int(n/2-1)
    b=int(n/2-1)
    for i in range(3):
        for j in range(3):
            draw_white(a+i,b+j)
    white_set.remove((a+1,b+1))
    empty_position_set.add((a+1,b+1))
    draw_black(a+1,b+1)
    
    print(white_set)  
    print(black_set)   
    print(empty_position_set)
       
          
    


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
            user_color = input("Please choose your color - B for Black, W for White:").upper()
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
def draw_white(x,y):
    othello = turtle.Turtle()
    othello.hideturtle() 
    othello.speed(0)
    othello.penup()   
    corner = -n * SQUARE / 2
    othello.setposition(corner+SQUARE/2+(y-1)*SQUARE,corner+(x-1)*SQUARE+5)
    othello.pendown()
    othello.color('black')
    othello.fillcolor('white')
    othello.begin_fill()
    othello.circle(SQUARE/2-5)
    othello.end_fill()
    othello.penup()
    othello.hideturtle()
    update_white_set(x,y)
      

    
     
    
def draw_black(x,y): 
    othello = turtle.Turtle()
    othello.hideturtle() 
    othello.speed(0)
    othello.penup()   
    corner = -n * SQUARE / 2
    othello.setposition(corner+SQUARE/2+(y-1)*SQUARE,corner+(x-1)*SQUARE+5)
    othello.pendown()
    othello.color('black')
    othello.fillcolor('black')
    othello.begin_fill()
    othello.circle(SQUARE/2-5)
    othello.end_fill()
    othello.penup() 
    othello.hideturtle()
    update_black_set(x,y)
   

     

def draw_operation(i,j):
    global x
    global y
    global current_color_num
    global black_legal_flag
    black_legal_flag = False
    SQUARE*(int(n/2))
    x=int(j/SQUARE+1+n/2)
    y=int(i/SQUARE+1+n/2)
    if (x,y) in empty_position_set:
        if current_color_num == 0:
            draw_black(x,y)
            current_color_num = 1
        elif current_color_num == 1:
            draw_white(x,y)  
            current_color_num = 0 
    print_test()
    if is_game_over():
        os._exit(0)

def click_to_game():
    s = turtle.getscreen()
    s.onclick(draw_operation)        
    

#flip--------------------------------------------------------------------------------------------               
def flip(x,y):
    if (x,y) in black_set and current_color_num == 1:
        black_set.remove((x,y))
        empty_position_set.add((x,y))
        draw_white(x,y)
        
    elif (x,y) in white_set and current_color_num == 0:
        white_set.remove((x,y))
        empty_position_set.add((x,y))
        draw_black(x,y)
        



# update set---------------------------------------------------------------
def update_white_set(x,y):
    if (x,y) in empty_position_set:
        empty_position_set.remove((x,y))
    elif (x,y) in black_set:
        black_set.remove((x,y))
    white_set.add((x,y))  

def update_black_set(x,y):
    if (x,y) in empty_position_set:
        empty_position_set.remove((x,y))
    elif (x,y) in white_set:
        white_set.remove((x,y))
    black_set.add((x,y)) 


# test------------------------------------------------------------------------------------------------
def print_test():
    print("Empty:")
    print(empty_position_set)
    print("black:")
    print(black_set)
    print("white:")
    print(white_set)
    print(x,y)
    print(current_color_num)
    print(user_color)
    print(enemy_color)
    print(black_legal_flag)

def is_game_over():
    if empty_position_set == set():
        print("No more position.")
        return True    
    else:
        return False    
 

#main--------------------------------------------------------------------------------------------- 
def main():
    print("Welcome to Othello Game!")
    user_input_n()
    draw_board(n)
    init_empty_position_set(n)
    #init_four_tile(n)
    init_test_tile(n)
    user_choose_color()
    click_to_game()
    
            
main()
turtle.done()