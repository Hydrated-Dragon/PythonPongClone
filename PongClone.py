#Imports
import turtle
import keyboard
import time

start = 1

#Classes
class Player:
    def __init__(self, x, y, name, keyup, keydown, rotToUp, score):
        self.x = x
        self.y = y
        self.name = name
        self.keyup = keyup
        self.keydown = keydown
        self.score = score
        self.turt = turtle.Turtle()
        self.turt.speed(1)
        self.turt.penup()
        self.turt.shape("square")
        self.turt.goto(x, y)
        self.turt.color("white")
        self.turt.shapesize(1, 6)
        self.turt.left(rotToUp)

    
    
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.turt = turtle.Turtle()
        self.turt.speed(1)
        self.turt.penup()
        self.turt.shape("square")
        self.turt.goto(x, y)
        self.turt.color("white")
    def move(self, difx, dify, xModif, yModif):
        self.turt.setx(self.turt.xcor() + (difx * xModif))
        self.turt.sety(self.turt.ycor() + (dify * yModif))
    
    
    
class TurText:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.turt = turtle.Turtle()
        self.turt.penup()
        self.turt.goto(x, y)
        self.style = ('Arial', 30, 'italic')
        self.turt.hideturtle()
    def writeDatText(self, text, col):
        self.turt.color(col)
        self.turt.write(text, font=self.style, align='center')
        
    
    
#Public vars
tur = turtle.Turtle()
screen = turtle.Screen()
moveStep = 10



#All functions
def setup():
    screen.setup(1280, 900)
    screen.cv._rootwindow.resizable(False, False)
    screen.title("Pong")
    screen.bgcolor("black")
    screen.tracer(0, 0)

def initPlayers():
    global p1
    global p2
    global ball
    global scoreTextP1
    global scoreTextP2
    p1 = Player(-600, 10, "Player 1", 'w', 's', 90, 0)
    p2 = Player(600, 10, "Player 2", 'up', 'down', 90, 0)
    ball = Ball(0, 0)
    scoreTextP1 = TurText(-300, 300)
    scoreTextP2 = TurText(300, 300)

def moveP1(upDown):
    newY = p1.turt.ycor() + (upDown * moveStep)
    p1.turt.sety(newY)
def moveP2(upDown):
    newY = p2.turt.ycor() + (upDown * moveStep)
    p2.turt.sety(newY)



#Main code/loop/vars
setup()
initPlayers()

dx = 2
dy = 2
xMod = 1
yMod = 1
change1 = 1
change2 = 1
paddleBorder1 = -640
paddleBorder2 = 640


scoreTextP1.writeDatText(p1.score, "white")
scoreTextP2.writeDatText(p2.score, "white")

while True:
    time.sleep(1 / 100)
    #Drawing/Calculations
    if start == 0:
        ball.move(dx, dy, xMod, yMod)
    
    if ball.turt.ycor() > 439:
        if dy > 0:
            yMod = -1
        else:
            yMod = 1
    if ball.turt.ycor() < -439:
        if dy < 0:
            yMod = -1
        else:
            yMod = 1
    if change1 == 1 and ball.turt.xcor() > 589 and ball.turt.xcor() < paddleBorder2 and ball.turt.ycor() < (p2.turt.ycor()+50) and ball.turt.ycor() > (p2.turt.ycor()-50):
        xMod = -1
        dx = dx + 1
        change1 = 0
        change2 = 1
        dy = int(((ball.turt.ycor()-p2.turt.ycor())/10)*yMod)
        if dy == 0:
            dy = 1
    if change2 == 1 and ball.turt.xcor() < -589 and ball.turt.xcor() > paddleBorder1 and ball.turt.ycor() < (p1.turt.ycor()+50) and ball.turt.ycor() > (p1.turt.ycor()-50):
        xMod = 1
        dx = dx + 1
        change1 = 1
        change2 = 0
        dy = int(((ball.turt.ycor()-p1.turt.ycor())/10)*yMod)
        if dy == 0:
            dy = 1
    
    if ball.turt.xcor() > paddleBorder2:
        scoreTextP1.writeDatText(str(p1.score), "black")
        p1.score = p1.score + 1
        scoreTextP1.writeDatText(str(p1.score), "white")
        ball.turt.goto(0, 0)
        start = 1
        dx = 2
        dy = 2
        xMod = 1
        yMod = 1
        p1.turt.goto(p1.x, p1.y)
        p2.turt.goto(p2.x, p2.y)
        change1 = 1
        change2 = 1
    if ball.turt.xcor() < paddleBorder1:
        scoreTextP2.writeDatText(str(p2.score), "black")
        p2.score = p2.score + 1
        scoreTextP2.writeDatText(str(p2.score), "white")
        ball.turt.goto(0, 0)
        start = 1
        dx = 2
        dy = 2
        xMod = 1
        yMod = 1
        p1.turt.goto(p1.x, p1.y)
        p2.turt.goto(p2.x, p2.y)
        change1 = 1
        change2 = 1
    
    #Input
    if keyboard.is_pressed(p1.keyup) and p1.turt.ycor() < 400:
        moveP1(1)
    if keyboard.is_pressed(p1.keydown) and p1.turt.ycor() > -400:
        moveP1(-1)
    if keyboard.is_pressed(p2.keyup) and p2.turt.ycor() < 400:
        moveP2(1)
    if keyboard.is_pressed(p2.keydown) and p2.turt.ycor() > -400:
        moveP2(-1)
    if(keyboard.is_pressed('esc')):
        screen.bye()
        break
    if keyboard.is_pressed('space') and start == 1:
        start = 0
    screen.update()
    