#!/usr/bin/python
"""
bash1.py--use turtle draw some turtles
last commit:2021-1-21-23:06
"""
from turtle import *
from random import random
import sys

setup(600,600,0,0)
shape("turtle")
color1 = random()
color2 = random()
color3 = random()

for i in range(100):
    color1 = random()
    color2 = random()
    color3 = random()
    stamp()
    color(color1,color2,color3)
    penup()
    fd(i)
    right(15)
    print(i)

done()
input()
sys.exit()
