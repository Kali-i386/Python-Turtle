#!/usr/bin/python
"""--no--"""
from random import randint
import turtle as t
import math,cmath
import os,sys,time

def init():
	t.setup(600,600)
	t.pensize(1)

def main():
	bg()
	ground()
	river()
	pass

def bg():
	pass

def tree(size,leaf):
	pass

def river():
	pass

def ground():
	pass

if __name__ == "__main__":
	while True:
		try:
			main()
		except KeyboardInterrupt:
			print ("Control-C")
		except:
			print("There is an Error while running!")
			print("Program will restart in 5 seconds.")
			time.sleep(1)
			print("Program will restart in 4 seconds.")
			time.sleep(1)
			print("Program will restart in 3 seconds.")
			time.sleep(1)
			print("Program will restart in 2 seconds.")
			time.sleep(1)
			print("Program will restart in 1 seconds.")
			time.sleep(1)
			continue