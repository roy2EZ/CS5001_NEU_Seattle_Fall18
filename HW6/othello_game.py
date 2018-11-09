import turtle
from turtle import Turtle, colormode
SQUARE = 50
color_list = ["Black","White"]
position = list()
position_dict = {}
def draw_board(n):
    ''' Function: draw_board
        Parameters: n, an int for # of squares
        Returns: nothing
        Does: Draws an nxn board with a green background
    '''

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

def draw_lines(turt, n):
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()


def initPositionDict(n):
    count = 0
    for x in range(1,n+1):
        for y in range(1,n+1):
            position.append([x,y])
            count += 1
            position_dict["position %d"%(count)] = position[count-1]
    return position_dict    

def initFirstFourCircle(n,color_number):
    x=int(n/2)
    y=int(n/2)
    for x in range(int(n/2),int(n/2 + 2)):
        for y in range(int(n/2),int(n/2 + 2)):
            color_list = ["Black","White"]
            color = color_list[color_number % 2]
            othello = turtle.Turtle()
            othello.hideturtle()
            othello.penup()
            corner = -n * SQUARE / 2
            othello.setposition(corner+SQUARE/2+(y-1)*SQUARE, corner+(x-1)*SQUARE)
            othello.pendown()
            othello.speed(200)
            othello.color('black')
            othello.fillcolor(color)
            othello.begin_fill()
            othello.circle(SQUARE/2)
            othello.end_fill()
            othello.penup()
            color_number += 1
        color_number += 1
    print("Ready? Game starts!")
           
                  


def drawCircle(n,x,y,color_number):
    color = color_list[color_number % 2]
    othello = turtle.Turtle()
    othello.hideturtle()
    othello.penup()   
    corner = -n * SQUARE / 2
    othello.setposition(corner+SQUARE/2+(y-1)*SQUARE, corner+(x-1)*SQUARE)
    othello.pendown()
    othello.speed(200)
    othello.color('black')
    othello.fillcolor(color)
    othello.begin_fill()
    othello.circle(SQUARE/2)
    othello.end_fill()
    
    
    


def main():
    while True:
        try:
            n = int(input("Please enter your board size: "))
            if n % 2 != 0:
                raise ValueError
        except ValueError:
            print("Valid size should be an even number.")
            continue
        else:
            break
    draw_board(n)
    initPositionDict(n)
    while True:
        try:
            color_number = int(input("Please choose your color by entering: \"1\" for black, \"2\" for white: "))
            if color_number not in [1,2]:
                raise ValueError
        except ValueError:
            print("Valid color should be \"1\" for black or \"2\" for white.")
            continue
        else:
            break
    initFirstFourCircle(n,color_number)
    while True:
        while True:
            try:
                x= int(input("Please enter the row number (1 to %d as bottom to top) to set your piece: " %n))
                if x < 1 or x > 4:
                    raise ValueError
            except ValueError:
                print("Valid range should be 1~4.")
                continue
            else:
                break   
        while True:
            try:
                y= int(input("Please enter the column number (1 to %d as left to right) to set your piece: " %n))
                if x < 1 or x > 4:
                    raise ValueError
            except ValueError:
                print("Valid range should be 1~4.")
                continue
            else:
                break        
        drawCircle(n,x,y,color_number - 1)
        color_number+=1
        color = color_list[color_number % 2]
        print("Now it's turn of %s to go: " % color)
        

    
main()

turtle.done()