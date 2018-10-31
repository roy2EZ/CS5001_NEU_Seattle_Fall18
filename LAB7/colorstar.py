import turtle
turt = turtle.Turtle()
turt.speed(200)
DISTANCE = 50
LAYER = 3
COLOR = ['red','yellow','green','blue','orange']

for j in range(LAYER):
    for i in range(5):
        turt.color(COLOR[i])      
        turt.fd(DISTANCE)
        turt.right(144)
        DISTANCE += 10
    
turtle.done()