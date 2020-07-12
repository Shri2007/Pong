import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
sa = 0
sb = 0

#Paddle A
pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.shapesize(stretch_wid=5, stretch_len=1)
pa.penup()
pa.goto(-350, 0)
#Paddle B
pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.shapesize(stretch_wid=5, stretch_len=1)
pb.penup()
pb.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 100
ball.dy = 100

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align = "center", font = ("Courier", 24, "normal"))

#Functions
def paup():
    y = pa.ycor()
    y += 20
    pa.sety(y)
def pado():
    y = pa.ycor()
    y -= 20
    pa.sety(y)
def pbup():
    y = pb.ycor()
    y += 20
    pb.sety(y)
def pbdo():
    y = pb.ycor()
    y -= 20
    pb.sety(y)

#Keyboard Bindings

wn.listen()
wn.onkeypress(paup, "w")
wn.onkeypress(pado, "s")
wn.onkeypress(pbup, "Up")
wn.onkeypress(pbdo, "Down")

while True:
    wn.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
 
    # Border checking
 
    # Top and bottom
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
        
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
 
    # Left and right
    if ball.xcor() > 350:
        sa += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(sa, sb), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
 
    elif ball.xcor() < -350:
        sb += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(sa, sb), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
 
    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < pa.ycor() + 50 and ball.ycor() > pa.ycor() - 50:
        ball.dx *= -1 
        
    
    elif ball.xcor() > 340 and ball.ycor() < pb.ycor() + 50 and ball.ycor() > pb.ycor() - 50:
        ball.dx *= -1

    

wn.mainloop()