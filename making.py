#!/usr/bin/python
"""--no--"""
from random import randint
import turtle as t
import math,cmath
import os,sys,time

def init():
	t.setup(600,600)
	t.pensize(1)
	t.colormode(255)

def main():
	init()
	bg()
	ground()

	t.goto(0,0)
	tree(-30,-165,100)
	t.right(60)
	tree(153,-100,100)
	t.right(60)
	tree(0,-185,100)
	river()
	pass

def bg():
	"""Draw Background"""
	#Sky
	t.penup()
	t.goto(-300,100)
	t.pencolor(153,217,234)
	t.fillcolor(153,217,234)
	t.pendown()
	t.begin_fill()
	t.fd(600)
	t.left(90)
	t.fd(200)
	t.left(90)
	t.fd(600)
	t.left(90)
	t.fd(200)
	t.end_fill()
	#Sea
	t.pencolor(0,162,232)
	t.fillcolor(0,162,232)
	t.begin_fill()
	t.goto(-300,-300)
	t.goto(300,-300)
	t.goto(300,100)
	t.goto(-300,100)
	t.end_fill()
	t.penup()
	t.goto(300,100)

def turtles():
	t.shape("turtle")
	t.color(0,200,0)
	t.penup()
	for i in range(5):
		tx = randint(-300,300)
		ty = randint(-300,0)
		t.goto(tx,ty)
		t.stamp()
		
def tree(cx,cy,size):
	t.penup();
	t.goto(cx,cy);
	t.pensize(13);
	t.pencolor(121,69,34);
	t.pendown();
	t.circle(size,60);
	lfpos = t.pos();
	t.pencolor("darkgreen");
	for leaf in range(5):
		t.left(360/5);
		t.pendown();
		si = 3;
		t.pensize(si);
		for s in range(5):t.pensize(si);t.fd(10);si += 2;
		t.penup()
		t.goto(lfpos)


def river():
	pass

def ground():
	t.pendown()
	t.fd(100)
	t.pencolor(255,249,128)
	t.fillcolor(255,249,128)
	t.left(180)
	t.begin_fill()
	def beach():
		t.circle(20,180)
		t.left(180)
	for k in range(15):
		beach()
	t.goto(-300,-300)
	t.goto(300,-300)
	t.goto(300,0)
	t.end_fill()
	t.penup()

if __name__ == "__main__":
	main()
	"""
	while True:
		try:
			main()
		except KeyboardInterrupt:
			print ("Control-C")
		except:
			print("There is an Error while running!")
			print("Program will restart in 5 seconds.")
			time.sleep(1)
			os.system("cls")
			print("Program will restart in 4 seconds.")
			os.system("cls")
			time.sleep(1)
			print("Program will restart in 3 seconds.")
			os.system("cls")
			time.sleep(1)
			print("Program will restart in 2 seconds.")
			os.system("cls")
			time.sleep(1)
			print("Program will restart in 1 seconds.")
			os.system("cls")
			time.sleep(1)
			continue"""
	input()
	sys.exit()