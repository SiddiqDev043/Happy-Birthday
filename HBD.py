import turtle
import pygame
from random import randint


pygame.mixer.init()
t = turtle.Turtle()

#screen 
s = turtle.Screen()
s.bgcolor("black")
#s.tracer(0)


pygame.mixer.music.load("BeautyAndABeat.mp3")
pygame.mixer.music.play(-1, 0, 5000)

t.penup()
t.goto(-150, -100)
t.pendown()
t.pensize(2)

#ractangle for kue
t.color("pink")
t.begin_fill()
for i in range(3):
    t.forward(300)
    t.left(90)
    t.forward(125)
    t.left(90)
        
t.end_fill()
t.forward(300)
t.left(90)



#Lingkaran
t.color("yellow")
t.begin_fill()
t.circle(25, 180)
for i in range(5):
    t.left(180)
    t.circle(25, 180)
t.end_fill()


t.left(90)
t.forward(70)
t.right(90)

t.color("pink")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(90)
    t.forward(160)
    t.left(90)
t.end_fill()

#lingkaran 2
t.color("yellow")
t.begin_fill()
for i in range(3):
    t.circle(26, 180)
    t.left(180)
t.end_fill()

t.right(90)
t.forward(155)
t.left(90)
t.forward(100)
t.right(90)
t.forward(70)

#lilin
def lilin(x,y):
    t.color("brown")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(7)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.end_fill()
    
    t.color("grey", "yellow")
    t.begin_fill()
    for i in range(2):
        t.forward(7)
        t.right(90)
        t.forward(10)
        t.right(90)
    t.end_fill()
    
lilin(55, 150)
lilin(5, 150)
lilin(-50, 150)



#HAPPY BIRTHDAY FOR YOU BROH
t.color('red')
t.penup()
t.goto(0, -175)
t.write('🥳HAPPY BIRTHDAY BROOOO🎂', align='center', font=("algerian 20 italic"))

t.color('white')
t.penup()
t.goto(0, -210)
t.write('SELAMAT KARENA SEMAKIN TUA ^_^', align='center', font=("algerian 20 italic"))

#star
t.color("yellow")
t.speed(0)

def draw_star():
    turns = 5
    t.begin_fill()
    while turns > 0:
        t.forward(25)
        t.left(145)
        turns = turns - 1
    t.end_fill()
    
#multiple star
num_stars = 0
while num_stars < 50:
    x = randint(-400, 400)
    y = randint(-250, 250)
    draw_star()
    t.penup()
    t.goto(x, y)
    t.pendown()
    num_stars = num_stars + 1

turtle.done()