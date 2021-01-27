#!/usr/bin/python
"""sky.py--use turtle to draw stars"""

from turtle import *
from random import randint,random
import sys

def init():
	colormode(255)
	setup(600,600)
	pencolor("yellow")
	speed(10)
	penup()

def stars():
	for i in range(50):
		starx = randint(-300,300)
		stary = randint(-300,300)
		penup()
		goto(starx,stary)
		pensize(randint(2,10))
		pendown()
		fd(1)

def sky():
	goto(-300,-329)
	pensize(3)
	colormode(255)
	j = 255
	for i in range(-299,299,3):
		penup()
		goto(-300,i)
		j -= 1
		pencolor(0,0,j)
		pendown()
		fd(600)

init()
sky()
pencolor("yellow")
hideturtle()
stars()
