import turtle

tt=turtle.Turtle()
turtle.bgcolor('black')
tt.pencolor('cyan')

tt.speed(0)
tt.penup()
tt.goto(0,200)
tt.pendown()


forDis=0 
dR=0

for i in range(210):
    tt.forward(forDis)
    tt.right(dR)
    forDis+=3
    dR+=1
    tt.hideturtle()

turtle.done()