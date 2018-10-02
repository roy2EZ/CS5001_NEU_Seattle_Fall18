#### Purpose
# To draw a i*j rectangle with a charactor  
# where the n and m will be input by user
# and user input that charactor for drawing
#### Signature
#  rectangle_draw :: (Integer, Integer)=>String
#### Template
# def rectangle(given...):
#    return returns...
#### Examples
# i=6, j=4, * =>
# ******
# *    *
# *    *
# *    *
# *    *
# ******

def rectangle_draw():
    i=int(input("Please give the width of rectangle:\n"))
    j=int(input("Please give the height of rectangle:\n"))
    brick=input("Please give the character that you wanna use to draw:\n")
    for m in range(j):
        for n in range(i):
            

