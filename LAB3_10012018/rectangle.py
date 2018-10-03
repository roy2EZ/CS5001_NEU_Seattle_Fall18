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
# 6, 4, * =>
# ******
# *    *
# *    *
# ******

def rectangle_draw():
    i=int(input("Please give the width of rectangle: "))
    j=int(input("Please give the height of rectangle: "))
    brick=input("Please give the character that you wanna use to draw: ")
    m=1
    list1=list(brick*i)
    list2=list(brick+" "*(i-2)+brick)
    while m<=j:
        if m==1 or m==j:
            print("".join(list1))
        else:
            print("".join(list2))
        m += 1

rectangle_draw()


